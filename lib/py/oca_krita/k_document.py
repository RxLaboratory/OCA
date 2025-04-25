"""! @brief Document-related methods
 @file document.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

import os
import krita # pylint: disable=import-error
from PyQt5.QtCore import Qt # pylint: disable=import-error,no-name-in-module
from PyQt5.QtWidgets import QProgressDialog # pylint: disable=import-error,no-name-in-module

from oca_core import ( # pylint: disable=relative-beyond-top-level
    OCALayer,
    OCADocument
)
from . import k_utils
from . import k_tags
from . import k_node
from .k_metadata import updateMetadata

def export(kDocument, exportPath, options = None, metaData = None):
    """!
    @brief Exports the given document

    Parameters : 
        @param document => The document to export
        @param {string} exportPath => The destination
        @param options = None => The export options
    """

    if options is None:
        options = {}
    if metaData is None:
        metaData = {}
    # Add plugin metaData
    metaData = updateMetadata(metaData)

    # === PREPARE APP ===

    Application.setBatchmode(True) # pylint: disable=undefined-variable
    # Let's duplicate the document first
    kDocument = kDocument.clone()
    # For some reason, Krita fails to save the keyframes
    # If we don't start after the last one...
    # (probably a cache issue...)
    k_utils.setCurrentFrame(kDocument, 10000)
    kDocument.setBatchmode(True)

    # ==== GATHER INFO ====

    # Create OCA Document
    ocaDoc = kDocumentToOCA( kDocument, metaData, options )

    # Set exportPath (the folder containing everytthing)
    fileName = kDocument.fileName() or 'Untitled'
    fileName = os.path.basename(fileName)
    fileName = os.path.splitext(fileName)[0] + '.oca'
    exportPath = os.path.join(exportPath, fileName)

    ocaDoc.setFileName(
        os.path.join(exportPath, fileName)
    )

    # ==== SHOW PROGRESS ====

    progressdialog = QProgressDialog(
        "Exporting animation...",
        "Cancel",
        0,
        ocaDoc.duration()
        )
    progressdialog.setWindowModality(Qt.WindowModality.WindowModal)

    # ==== EXPORT ====

    if options.get('flattenImage', False):
        exportFlattened(
            ocaDoc,
            kDocument,
            options,
            progressdialog
        )
    else:
        exportDocLayers(
            ocaDoc,
            kDocument,
            options,
            progressdialog
        )

    # Save doc
    if not ocaDoc.save():
        print("OCA >> Some errors have occured when exporting {} ({})".format(ocaDoc.name(), ocaDoc.fileName()))

    # ==== CLEAN ====

    progressdialog.close()
    kDocument.setBatchmode(False)
    # close document
    kDocument.close()
    Application.setBatchmode(False) # pylint: disable=undefined-variable

    return ocaDoc

def exportFlattened(ocaDoc, kDoc, options, progressdialog):
    """ This method exports a flattened image of the document for each keyframe of the animation. """

    # INFO

    ocaLayer = OCALayer()

    ocaLayer.setName( ocaDoc.name() )

    ocaLayer.setFileType(
        options.get('fileFormat', 'png')
    )

    ocaLayer.setAnimated(True)

    w,h = ocaDoc.size()
    ocaLayer.setPosition(w/2, h/2)
    ocaLayer.setSize(w, h)

    # DO EXPORT

    startTime, endTime = ocaDoc.timeRange()
    frame = startTime
    prevFrameNumber = -1

    disabledNodes = disableNodes(kDoc.rootNode(), tag = k_tags.IGNORE)
    if not options.get('exportReference', True):
        disabledNodes += disableNodes(kDoc.rootNode(), tag = k_tags.REFERENCE)

    frames = []
    while frame <= endTime:
        progressdialog.setValue(frame)
        if progressdialog.wasCanceled():
            k_utils.enableNodes( disabledNodes )
            break
        if k_utils.hasKeyframeAtTime(kDoc.rootNode(), frame):
            ocaFrame = k_node.exportFlattenedFrame(ocaDoc, kDoc, frame, options)
            if prevFrameNumber >= 0:
                frames[-1].setDuration(frame - prevFrameNumber)
            frames.append(ocaFrame)
            prevFrameNumber = frame
        frame = frame + 1

    # set the last frame duration
    if len(frames) > 0:
        lastFrame = frames[-1]
        lastFrame.setDuration(
            kDoc.fullClipRangeEndTime() - lastFrame.frameNumber()
        )
        ocaLayer.setFrames(frames)

    ocaDoc.appendLayer(ocaLayer)

def exportDocLayers(ocaDoc, kDoc, options, progressdialog):
    """Exports all the layers of the document"""
    layers = exportLayers(ocaDoc, kDoc, kDoc.rootNode(), ocaDoc.layersPath(), options, progressdialog)
    ocaDoc.setLayers(layers)

def exportLayers(ocaDoc, kDoc, parentNode, exportPath, options, progressdialog):
    """ This method get all sub-nodes from the current k_node and export them in
        the defined format."""

    layers = []

    print("OCA >> Listing children of: " + parentNode.name())

    for i, childNode in enumerate(parentNode.childNodes()):

        if progressdialog.wasCanceled():
            break

        newDir = ''
        nodeName = childNode.name().strip()

        print("OCA >> Loading k_node: " + nodeName)

        # ignore filters
        if (not options.get('exportFilterLayers', False)
            and 'filter' in childNode.type()):
            continue
        # ignore invisible
        if (not options.get('exportInvisibleLayers', False)
            and not childNode.visible()):
            continue
        # ignore reference
        if (not options.get('exportReference')
            and k_tags.REFERENCE in nodeName):
            continue
        # ignore _ignore_
        if k_tags.IGNORE in nodeName:
            continue

        merge = k_tags.MERGE in nodeName

        if merge:
            print("OCA >> Merging k_node: " + nodeName)
            k_utils.disableNodes(childNode)
            childNode = k_utils.flattenNode(kDoc, childNode, i, parentNode)
            nodeName = nodeName.replace(k_tags.MERGE,"").strip()
            childNode.setName( nodeName )
            print("OCA >> Merged and renamed k_node: " + childNode.name())

        ocaLayer = k_node.kNodeToOCA(kDoc, childNode, options)

        # if this is a clone or a doc, nothing to export, skip to the next
        if ocaLayer.layerType() == 'ocalayer' or ocaLayer.layerType() == 'clonelayer':
            layers.append(ocaLayer)
            continue

        # if there are children and not merged, export them
        if childNode.childNodes() and not merge:
            newDir = os.path.join(exportPath, nodeName)
            k_utils.mkdir( newDir )
            childLayers = exportLayers(ocaDoc, kDoc, childNode, newDir, options, progressdialog)
            ocaLayer.setLayers(childLayers)
        # if not a group
        else:
            k_node.export(ocaDoc, kDoc, ocaLayer, childNode, exportPath, options, progressdialog)

        layers.append(ocaLayer)

    return layers

def disableNodes(parentNode, disable=True, tag='_ignore_'):
    """Disables all nodes containing the tag in their name."""
    disabled = []
    for childNode in parentNode.childNodes():
        if childNode.visible():
            if tag in childNode.name():
                childNode.setVisible(not disable)
                disabled.append(childNode)

            if childNode.type() == 'grouplayer':
                disabled += disableNodes(childNode, disable, tag)
    return disabled

def kDocumentToOCA( kDocument, metadata, options ):
    """Creates an OCADocument"""

    ocaDoc = OCADocument()

    docName = kDocument.name() if kDocument.name() != "" else options.get("defaultDocumentName", "Document")
    ocaDoc.setName( docName )

    ocaDoc.setFrameRate(
        kDocument.framesPerSecond()
        )

    ocaDoc.setSize(
        kDocument.width(),
        kDocument.height()
    )

    ocaDoc.setColorDepth(
        kDocument.colorDepth()
    )

    bgColor = kDocument.backgroundColor()
    ocaDoc.setBackgroundColor(
        (
            bgColor.redF(),
            bgColor.greenF(),
            bgColor.blueF(),
            bgColor.alphaF()
        )
    )

    if options.get('fullClip', True):
        ocaDoc.setTimeRange(
            kDocument.fullClipRangeStartTime(),
            kDocument.fullClipRangeEndTime()
        )
    else:
        ocaDoc.setTimeRange(
            kDocument.playBackStartTime(),
            kDocument.playBackEndTime()
        )

    ocaDoc.setMeta(metadata)

    return ocaDoc
