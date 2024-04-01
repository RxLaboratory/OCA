"""! @brief Document-related methods
 @file document.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

import os
import krita # pylint: disable=import-error
from PyQt5.QtCore import Qt # pylint: disable=import-error,no-name-in-module
from PyQt5.QtWidgets import QProgressDialog # pylint: disable=import-error,no-name-in-module

from . import utils
from . import tags
from . import node
from .blending_modes import BLENDING_MODES
from .. import oca_core as oca # pylint: disable=relative-beyond-top-level

def export(document, exportPath, options = None):
    """!
    @brief Exports the given document

    Parameters : 
        @param document => The document to export
        @param {string} exportPath => The destination
        @param options = None => The export options
    """

    if options is None:
        options = dict()

    Application.setBatchmode(True) # pylint: disable=undefined-variable

    # Let's duplicate the document first
    document = document.clone()
    # For some reason, Krita fails to save the keyframes
    # If we don't start after the last one...
    # (probably a cache issue...)
    utils.setCurrentFrame(document, 10000)
    document.setBatchmode(True)

    # Set exportPath
    documentFileName = document.fileName() if document.fileName() else 'Untitled'  # noqa: E501
    fileName = os.path.splitext(os.path.basename(documentFileName))[0] + '.oca'
    exportPath = os.path.join(exportPath, fileName)
    utils.mkdir( exportPath )

    # Collect doc info
    docInfo = utils.getDocInfo(document)
    docInfo['ocaVersion'] = oca.VERSION
    if docInfo['name'] == "":
        docInfo['name'] = "Document"
    documentDirName = docInfo['name']
    documentPath = os.path.join(exportPath, documentDirName)
    utils.mkdir( documentPath )

    if not options.get('fullClip', True):
        docInfo['startTime'] = document.playBackStartTime()
        docInfo['endTime'] = document.playBackEndTime()

    progressdialog = QProgressDialog("Exporting animation...", "Cancel", 0, docInfo['endTime'] - docInfo['startTime'])
    progressdialog.setWindowModality(Qt.WindowModality.WindowModal)

    if options.get('flattenImage', False):
        nodeInfo = exportFlattened(
            docInfo,
            document,
            documentPath,
            options,
            progressdialog
        )
        docInfo['layers'].append(nodeInfo)
    else:
        nodes = exportLayers(
            docInfo,
            document,
            document.rootNode(),
            documentPath,
            options,
            progressdialog
        )
        docInfo['layers'] = nodes

    # Write doc info
    oca.file.save(
        docInfo,
        os.path.join(exportPath, fileName)
    )

    progressdialog.close()

    document.setBatchmode(False)

    # close document
    document.close()

    Application.setBatchmode(False) # pylint: disable=undefined-variable

    return documentPath + docInfo['name'] + '.oca'

def exportFlattened(docInfo, document, exportPath, options, progressdialog):
    """ This method exports a flattened image of the document for each keyframe of the animation. """

    nodeInfo = utils.createNodeInfo( docInfo['name'])
    nodeInfo['fileType'] = options.get('fileFormat', 'png')
    nodeInfo['animated'] = True
    nodeInfo['position'] = [ docInfo['width'] / 2, docInfo['height'] / 2 ]
    nodeInfo['width'] = docInfo['width']
    nodeInfo['height'] = docInfo['height']

    frame = docInfo['startTime']
    prevFrameNumber = -1

    disabledNodes = disableNodes(document.rootNode(), tag = tags.IGNORE)
    if not options.get('exportReference', True):
        disabledNodes += disableNodes(document.rootNode(), tag = tags.REFERENCE)

    while frame <= docInfo['endTime']:
        progressdialog.setValue(frame)
        if (progressdialog.wasCanceled()):
            utils.enableNodes( disabledNodes )
            break
        if utils.hasKeyframeAtTime(document.rootNode(), frame):
            frameInfo = node.exportFlattenedFrame(document, frame, exportPath)
            if prevFrameNumber >= 0:
                nodeInfo['frames'][-1]['duration'] = frame - prevFrameNumber
            nodeInfo['frames'].append(frameInfo)
            prevFrameNumber = frame
        frame = frame + 1

    # set the last frame duration
    if len(nodeInfo['frames']) > 0:
        f = nodeInfo['frames'][-1]
        f['duration'] = document.fullClipRangeEndTime() - f['frameNumber']

    return nodeInfo

def exportLayers(docInfo, document, parentNode, exportPath, options, progressdialog):
    """ This method get all sub-nodes from the current node and export them in
        the defined format."""

    nodes = []

    print("OCA >> Listing children of: " + parentNode.name())

    for i, childNode in enumerate(parentNode.childNodes()):

        if progressdialog.wasCanceled():
            break

        newDir = ''
        nodeName = childNode.name().strip()

        print("OCA >> Loading node: " + nodeName)

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
                and tags.REFERENCE in nodeName):
            continue
        # ignore _ignore_
        if tags.IGNORE in nodeName:
            continue

        merge = tags.MERGE in nodeName

        if merge:
            print("OCA >> Merging node: " + nodeName)
            utils.disableNodes(childNode)
            childNode = utils.flattenNode(document, childNode, i, parentNode)
            nodeName = nodeName.replace(tags.MERGE,"").strip()
            childNode.setName( nodeName )
            print("OCA >> Merged and renamed node: " + childNode.name())

        nodeInfo = utils.getNodeInfo(document, childNode)
        nodeInfo['fileType'] = options.get('fileFormat', 'png')
        nodeInfo['reference'] = tags.REFERENCE in nodeName
        # Update size if not cropped:
        if not options.get('cropToImageBounds', False):
            nodeInfo['width'] = document.width()
            nodeInfo['height'] = document.height()
            nodeInfo['position'] = [ document.width() / 2, document.height() / 2 ]

        # translate blending mode to OCA
        nodeInfo['blendingMode'] = BLENDING_MODES.get(
            nodeInfo['blendingMode'],
            oca.blending_modes.NORMAL
            )

        # if there are children and not merged, export them
        if childNode.childNodes() and not merge:
            newDir = os.path.join(exportPath, nodeName)
            utils.mkdir( newDir )
            childNodes = exportLayers(docInfo, document, childNode, newDir, options, progressdialog)
            nodeInfo['childLayers'] = childNodes
        # if not a group
        else:
            node.export(docInfo, document, nodeInfo, childNode, exportPath, options, progressdialog)

        nodes.append(nodeInfo)

    return nodes

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