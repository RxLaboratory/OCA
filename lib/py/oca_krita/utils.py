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
        currentTime = currentTime + 500

    return succeed

def getDocInfo(document):
    """Creates a new document info."""
    docInfo = {}
    docInfo['name'] = document.name()
    docInfo['frameRate'] = document.framesPerSecond()
    docInfo['width'] = document.width()
    docInfo['height'] = document.height()
    docInfo['startTime'] = document.fullClipRangeStartTime()
    docInfo['endTime'] = document.fullClipRangeEndTime()
    docInfo['colorDepth'] = document.colorDepth()
    bgColor = document.backgroundColor()
    docInfo['backgroundColor'] = [ bgColor.redF(), bgColor.greenF(), bgColor.blueF(), bgColor.alphaF() ]
    docInfo['layers'] = []
    docInfo['originApp'] = 'Krita'
    docInfo['originAppVersion'] = krita.Krita.instance().version()
    return docInfo

def createNodeInfo(name, nodeType = 'paintlayer'):
    """Creates a new default node info of a given type with a given name."""
    nodeInfo = {}
    nodeInfo['name'] = name
    nodeInfo['frames'] = []
    nodeInfo['childLayers'] = []
    nodeInfo['type'] = nodeType
    nodeInfo['fileType'] = ""
    nodeInfo['blendingMode'] = 'normal'
    nodeInfo['animated'] = False
    nodeInfo['position'] = [ 0, 0 ]
    nodeInfo['width'] = 0
    nodeInfo['height'] = 0
    nodeInfo['label'] = -1
    nodeInfo['opacity'] = 1.0
    nodeInfo['visible'] = True
    nodeInfo['reference'] = False
    nodeInfo['passThrough'] = False
    nodeInfo['inheritAlpha'] = False
    return nodeInfo

def getNodeInfo(document, node, useDocumentSize = False):
    """Constructs a new node info based on a given node"""
    nodeInfo = {}
    nodeInfo['name'] = node.name().strip()
    nodeInfo['frames'] = []
    nodeInfo['childLayers'] = []
    nodeInfo['type'] = node.type()
    nodeInfo['fileType'] = ""
    nodeInfo['blendingMode'] = node.blendingMode()
    nodeInfo['animated'] = node.animated()
    if useDocumentSize or node.animated():
        nodeInfo['position'] = [ document.width() / 2, document.height() / 2 ]
        nodeInfo['width'] = document.width()
        nodeInfo['height'] = document.height()
    else:
        nodeInfo['position'] = [ node.bounds().center().x(), node.bounds().center().y() ]
        nodeInfo['width'] = node.bounds().width()
        nodeInfo['height'] = node.bounds().height()
    nodeInfo['label'] = node.colorLabel()
    nodeInfo['opacity'] = 1.0 # Opacity is set by the frame
    nodeInfo['visible'] = node.visible()
    nodeInfo['passThrough'] = False
    nodeInfo['reference'] = False
    nodeInfo['inheritAlpha'] = node.inheritAlpha()
    if node.type() == 'grouplayer':
        nodeInfo['passThrough'] = node.passThroughMode()
        nodeInfo['width'] = document.width()
        nodeInfo['height'] = document.height()
        nodeInfo['position'] = [ document.width() / 2, document.height() / 2 ]

    return nodeInfo

def createKeyframeInfo(name, fileName, frameNumber):
    """Creates a new default keyframe info."""
    frameInfo = {}
    frameInfo['name'] = name
    frameInfo['fileName'] = fileName
    frameInfo['frameNumber'] = frameNumber
    frameInfo['opacity'] = 1.0
    frameInfo['position'] = [0,0]
    frameInfo['width'] = 0
    frameInfo['height'] = 0
    frameInfo['duration'] = 1

    return frameInfo

def getKeyframeInfo(document, node, frameNumber, useDocumentSize = False):
    """Constructs a new keyframe info based on a given node at a given frame"""
    setCurrentFrame(document, frameNumber)

    frameInfo = {}
    frameInfo['name'] = '{0}_{1}'.format( node.name(), intToStr(frameNumber))
    frameInfo['fileName'] = ''
    frameInfo['frameNumber'] = frameNumber
    frameInfo['opacity'] = node.opacity() / 255.0
    if useDocumentSize:
        frameInfo['position'] = [ document.width() / 2, document.height() / 2 ]
        frameInfo['width'] = document.width()
        frameInfo['height'] = document.height()
    else:
        frameInfo['position'] = [ node.bounds().center().x(), node.bounds().center().y() ]
        frameInfo['width'] = node.bounds().width()
        frameInfo['height'] = node.bounds().height()
    frameInfo['duration'] = 1

    return frameInfo