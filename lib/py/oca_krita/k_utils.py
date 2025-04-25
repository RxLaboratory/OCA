"""Krita utils"""

import time
import os
import threading
import krita # pylint: disable=import-error

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

    # It seems we need to do something befre refreshProjection for it to work
    tmpNode = document.createNode('--- OCA TEMP ---', 'paintlayer')
    document.refreshProjection()
    tmpNode.remove()
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
    """Flattens a layer"""
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
    """Enable the nodes"""
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
