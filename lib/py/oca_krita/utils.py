import time
import os
import krita # pylint: disable=import-error
from . import utils

def mkdir(directory):
    """Creates a directory if it doesn't exist"""
    if os.path.exists(directory):
        return
    try:
        os.makedirs(directory)
    except OSError as e:
        raise e

def intToStr(i, numDigits = 5):
    """Converts an integer to a string, prepending some 0 to get a certain number of digits"""
    s = str(i)
    while len(s) < numDigits:
        s = "0" + s
    return s

def setCurrentFrame(document, frameNumber):
    """Sets the current frame in the document and waits for the image to be cached."""
    document.setCurrentTime(frameNumber)
    document.refreshProjection()

def hasKeyframeAtTime(parentNode, frameNumber, visibleNodesOnly=True ):
    """Checks if the node or one of its children has a keyframe at the given frame number"""

    if visibleNodesOnly and not parentNode.visible():
        return False

    if parentNode.hasKeyframeAtTime(frameNumber):
        return True

    for node in parentNode.childNodes():
        if hasKeyframeAtTime(node, frameNumber):
            return True

    return False

def flattenNode(document, node, nodeIndex, parentNode):
    # create a layer right above the node to merge
    mergeNode = document.createNode(node.name(), 'paintlayer')
    parentNode.addChildNode(mergeNode, node)
    mergeNode.mergeDown()
    newNode = parentNode.childNodes()[nodeIndex]
    return newNode

def disableNodes(parentNode, disable=True, tag='_ignore_'):
    """Disables all nodes containing '_ignore_' in their name."""
    for node in parentNode.childNodes():
        if node.visible():
            if tag in node.name():
                node.setVisible(not disable)

            if node.type() == 'grouplayer':
                disableNodes(node, disable, tag)

def enableNodes(nodes):
    for node in nodes:
        node.setVisible(True)

def exportDocument(document, fileName, timeOut=10000):
    """Attempts to export the document for timeOut milliseconds"""

    succeed = False

    currentTime = 0
    while currentTime < timeOut:
        succeed = document.exportImage(fileName, krita.InfoObject())
        if succeed:
            break
        time.sleep(0.5)
        currentTime += 500

    return succeed

def getDocInfo(document):
    """Creates a new document info."""
    bgColor = document.backgroundColor()
    return {
        'name':  document.name(),
        'frameRate': document.framesPerSecond(),
        'width': document.width(),
        'height': document.height(),
        'startTime': document.fullClipRangeStartTime(),
        'endTime': document.fullClipRangeEndTime(),
        'colorDepth': document.colorDepth(),
        'backgroundColor': [
            bgColor.redF(),
            bgColor.greenF(),
            bgColor.blueF(),
            bgColor.alphaF()
        ],
        'layers': [],
        'originApp': 'Krita',
        'originAppVersion': krita.Krita.instance().version()
    }

def createNodeInfo(name, nodeType = 'paintlayer'):
    """Creates a new default node info of a given type with a given name."""
    return {
        'name': name,
        'frames': [],
        'childLayers': [],
        'type': nodeType,
        'fileType': "",
        'blendingMode': 'normal',
        'animated': False,
        'position': [0, 0],
        'width': 0,
        'height': 0,
        'label': -1,
        'opacity': 1.0,
        'visible': True,
        'reference': False,
        'passThrough': False,
        'inheritAlpha': False
    }

def getNodeInfo(document, node, useDocumentSize = False):
    """Constructs a new node info based on a given node"""

    useDocumentSize = useDocumentSize or node.animated() or node.type() == 'grouplayer'

    x, y, w, h = getNodeCoordinates(document, node, useDocumentSize)
    pT = node.passThroughMode() if node.type() == 'grouplayer' else False

    return {
        'name': node.name().strip(),
        'frames': [],
        'childLayers': [],
        'type': node.type(),
        'fileType': "",
        'blendingMode': node.blendingMode(),
        'animated': node.animated(),
        'position': [x, y],
        'width': w,
        'height': h,
        'label': node.colorLabel(),
        'opacity': 1.0,  # Opacity is set by the frame
        'visible': node.visible(),
        'passThrough': pT,
        'reference': False,
        'inheritAlpha': node.inheritAlpha()
    }

def createKeyframeInfo(name, fileName, frameNumber):
    """Creates a new default keyframe info."""
    return {
        'name': name,
        'fileName': fileName,
        'frameNumber': frameNumber,
        'opacity': 1.0,
        'position': [0, 0],
        'width': 0,
        'height': 0,
        'duration': 1
    }

def getKeyframeInfo(document, node, frameNumber, useDocumentSize = False):
    """Constructs a new keyframe info based on a given node at a given frame"""
    setCurrentFrame(document, frameNumber)

    x, y, w, h = getNodeCoordinates(document, node, useDocumentSize)

    return {
        'name': f'{node.name()}_{intToStr(frameNumber)}',
        'fileName': '',
        'frameNumber': frameNumber,
        'opacity': node.opacity() / 255.0,
        'position': [x, y],
        'width': w,
        'height': h,
        'duration': 1
    }

def getNodeCoordinates( document, node, useDocumentSize = False):
    """The position, width and height of the exported node"""
    x, y = 0, 0
    w, h = 0 ,0
    if useDocumentSize:
        x, y = document.width() / 2, document.height() / 2
        w, h = document.width(), document.height()
    else:
        bounds = node.bounds()
        x, y = bounds.center().x(), bounds.center().y()
        w, h = bounds.width(), bounds.height()
    
    return x, y, w, h
