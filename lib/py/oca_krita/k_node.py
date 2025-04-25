"""! @brief Node-related OCA methods
 @file node.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

import os
import krita # pylint: disable=import-error
from PyQt5.QtCore import QRect, QUuid # pylint: disable=no-name-in-module,import-error
from oca_core import BLENDING_MODES as OCA_BLENDING_MODES # pylint: disable=relative-beyond-top-level
from oca_core import ( # pylint: disable=relative-beyond-top-level
    OCAFrame,
    OCALayer,
    OCAObject,
    OCASource,
    LAYER_TYPES,
    FILE_TYPES,
)
from . import k_utils
from . import k_tags
from .k_blending_modes import KRITA_BLENDING_MODES

def exportFlattenedFrame(ocaDoc, kDoc, frameNumber, options):
    """Exports the frame as a flattend image."""
    k_utils.setCurrentFrame(kDoc, frameNumber)

    imageName = '{0}_{1}'.format(
        ocaDoc.name(),
        k_utils.intToStr(frameNumber)
        )
    imagePath = os.path.join(
        ocaDoc.layersPath(),
        imageName
        )
    imagePath += "." + options.get('fileFormat', 'png')

    succeed = k_utils.exportDocument(kDoc, imagePath)
    # A single PNG Pixel is 89 Bytes
    if os.path.getsize(imagePath) < 100:
        succeed = False

    ocaFrame = OCAFrame()

    if not succeed:
        print("OCA >> Error when writing file: {}".format(imagePath))
        error = "Error when writing file: {}".format(imagePath)
        ocaFrame.addError(
            error,
            OCAObject.WRITE_ERROR
            )

    ocaFrame.setName(imageName)
    ocaFrame.setFileName(imagePath)
    ocaFrame.setFrameNumber(frameNumber)
    w, h = ocaDoc.size()
    ocaFrame.setPosition( w/2, h/2 )
    ocaFrame.setSize(w, h)

    return ocaFrame

def exportFrame(kDoc, kNode, frameNumber, exportPath, options):
    """Exports a frame"""
    k_utils.setCurrentFrame(kDoc, frameNumber)


    if kNode.bounds().width() < 2:
        ocaFrame = OCAFrame()
        ocaFrame.setName( OCAFrame.BLANK_NAME )
        ocaFrame.setFrameNumber(frameNumber)
        return ocaFrame

    nodeName = kNode.name().strip()
    fileFormat = options.get('fileFormat', 'png')
    if '[jpeg]' in nodeName:
        fileFormat = 'jpeg'
    elif '[png]' in nodeName:
        fileFormat = 'png'
    elif '[exr]' in nodeName:
        fileFormat = 'exr'

    imageName = '{0}_{1}'.format(
        kNode.name().strip(),
        k_utils.intToStr(frameNumber)
        )
    imagePath = os.path.join(exportPath, imageName) + '.' + fileFormat

    if options.get('cropToImageBounds', False):
        bounds = QRect()
    else:
        bounds = QRect(0, 0, kDoc.width(), kDoc.height())

    opacity = kNode.opacity()
    kNode.setOpacity(255)
    kNode.save(imagePath, options.get('resolution', 1), options.get('resolution', 1), krita.InfoObject(), bounds)
    kNode.setOpacity(opacity)

    ocaFrame = kFrameToOCA(kDoc, kNode, frameNumber, options)
    ocaFrame.setFileName(imagePath)
    # Sometimes, a blank frame may be saved, remove it
    if ocaFrame.isBlank():
        os.remove(imagePath)
        ocaFrame.setFileName("")
        return ocaFrame

    # Make sure the image has been correctly exported
    succeed = True
    if not os.path.isfile(imagePath):
        succeed = False
    # A single PNG Pixel is 89 Bytes
    elif os.path.getsize(imagePath) < 100:
        succeed = False

    if not succeed:
        print("OCA >> Error when writing file: {}".format(imagePath))
        error = "Error when writing file: {}".format(imagePath)
        ocaFrame.addError(
            error,
            OCAObject.WRITE_ERROR
            )

    return ocaFrame

def export(ocaDoc, kDoc, ocaLayer, kNode, exportPath, options, progressdialog):
    """Exports the Krita node."""
    nodeName = kNode.name().strip()
    print("OCA >> Exporting node: " + nodeName + " (" + kNode.type() + ")")
    progressdialog.setLabelText(i18n("Exporting") + " " + nodeName) # pylint: disable=undefined-variable

    startTime, endTime = ocaDoc.timeRange()
    frame = startTime

    if kNode.animated() or kNode.type() == 'grouplayer':
        nodeDir = os.path.join(exportPath, nodeName)
        prevFrameNumber = -1
        frames = []
        k_utils.mkdir( nodeDir )
        while frame <= endTime:
            progressdialog.setValue(frame)
            if progressdialog.wasCanceled():
                break

            if k_utils.hasKeyframeAtTime(kNode, frame):
                ocaFrame = exportFrame(kDoc, kNode, frame, nodeDir, options)
                if prevFrameNumber >= 0:
                    frames[-1].setDuration( frame - prevFrameNumber )
                frames.append(ocaFrame)
                prevFrameNumber = frame
            frame = frame + 1

        # set the last frame duration
        if len(frames) > 0:
            f = frames[-1]
            f.setDuration( kDoc.fullClipRangeEndTime() - f.frameNumber() )

        ocaLayer.setFrames(frames)

    else:
        ocaFrame = exportFrame(kDoc, kNode, frame, exportPath, options)
        ocaFrame.setDuration( kDoc.playBackEndTime() - kDoc.playBackStartTime() )
        ocaLayer.appendFrame(ocaFrame)

def getCoordinates(kDoc, kNode, useDocumentSize = False):
    """The position, width and height of the exported node"""
    x, y = 0, 0
    w, h = 0 ,0
    if useDocumentSize:
        x, y = kDoc.width() / 2, kDoc.height() / 2
        w, h = kDoc.width(), kDoc.height()
    else:
        bounds = kNode.bounds()
        x, y = bounds.center().x(), bounds.center().y()
        w, h = bounds.width(), bounds.height()

    return x, y, w, h

def kNodeToOCA( kDocument, kNode, options ):
    """Creates an OCALayer."""

    useDocumentSize = (
        not options.get('cropToImageBounds', False)
        or kNode.animated()
        or kNode.type() == 'grouplayer'
    )
    x, y, w, h = getCoordinates(kDocument, kNode, useDocumentSize)
    pT = kNode.passThroughMode() if kNode.type() == 'grouplayer' else False

    ocaLayer = OCALayer()

    ocaLayer.setName(
        kNode.name().strip()
    )
    ocaLayer.setId(
        kNode.uniqueId().toString(QUuid.WithoutBraces)
    )

    # If this is a clone or a doc, set the source object
    t = kNode.type()
    if t == 'clonelayer':
        ocaLayer.setLayerType( LAYER_TYPES.CLONE )
        kSourceNode = kNode.sourceNode()
        source = OCASource()
        source.setId(
            kSourceNode.uniqueId().toString(QUuid.WithoutBraces)
            )
        ocaLayer.setSource(source)
    elif t == 'filelayer' and not options.get('mergeNestedDocuments', False):
        # If this is a layered file,
        # It can be nested as an OCA Document
        sourcePath = kNode.path()
        print("OCA >> Analyzing File Layer: {}".format(sourcePath))
        ext = FILE_TYPES.getFileType(sourcePath)
        if ext in FILE_TYPES.LAYERED_TYPES:
            print("OCA >> This file may contain layers, it will be exported as an OCA Document.")
            ocaLayer.setLayerType( LAYER_TYPES.OCA )
            source = OCASource()
            source.setFileName(sourcePath)
            ocaLayer.setSource(source)
        else:
            print("OCA >> The file will be exported as a paintlayer.")
            ocaLayer.setLayerType( LAYER_TYPES.PAINT )
            ocaLayer.setFileType(
                options.get('fileFormat', 'png')
            )
    else:
        ocaLayer.setLayerType( t )
        ocaLayer.setFileType(
            options.get('fileFormat', 'png')
        )

    ocaLayer.setBlendingMode(
        KRITA_BLENDING_MODES.get(
            kNode.blendingMode(),
            OCA_BLENDING_MODES.NORMAL
            )
        )
    ocaLayer.setAnimated(kNode.animated())
    ocaLayer.setPosition(x, y)
    ocaLayer.setSize( w, h)
    ocaLayer.setLabel(kNode.colorLabel())
    ocaLayer.setVisible(kNode.visible())
    ocaLayer.setPassThrough(pT)
    ocaLayer.setInheritAlpha(kNode.inheritAlpha())

    # Set as reference if the tag is set
    ocaLayer.setReference(
        k_tags.REFERENCE in kNode.name()
    )

    return ocaLayer

def kFrameToOCA( kDocument, kNode, frameNumber, options):
    """Creates an OCAFrame"""
    k_utils.setCurrentFrame(kDocument, frameNumber)

    useDocumentSize = not options.get('cropToImageBounds', False)
    x, y, w, h = getCoordinates(kDocument, kNode, useDocumentSize)

    ocaFrame = OCAFrame()

    if w == 0 or h == 0:
        ocaFrame.setName( OCAFrame.BLANK_NAME )
        ocaFrame.setFrameNumber(frameNumber)
        return ocaFrame

    ocaFrame.setName(
        "{}_{}".format(kNode.name(), k_utils.intToStr(frameNumber))
    )
    ocaFrame.setOpacity( kNode.opacity() / 255.0 )
    ocaFrame.setPosition( x, y )
    ocaFrame.setSize(w, h)
    ocaFrame.setFrameNumber(frameNumber)

    return ocaFrame
