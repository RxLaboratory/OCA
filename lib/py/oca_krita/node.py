import os
import krita # pylint: disable=import-error
from PyQt5.QtCore import QRect # pylint: disable=no-name-in-module # pylint: disable=import-error
from . import utils

def exportFlattenedFrame(docInfo, document, frameNumber, exportPath, options):

    utils.setCurrentFrame(document, frameNumber)

    imageName = '{0}_{1}'.format( docInfo['name'], utils.intToStr(frameNumber))
    imagePath = os.path.join(exportPath, imageName) + "." + options.get('fileFormat', 'png')

    succeed = utils.exportDocument(document, imagePath)
    
    if not succeed:
        frameInfo = utils.createKeyframeInfo("Export failed", "", frameNumber)
    else:       
        frameInfo = utils.createKeyframeInfo(imageName, imagePath, frameNumber)
        frameInfo['position'] = [ docInfo['width'] / 2, docInfo['height'] / 2 ]
        frameInfo['width'] = docInfo['width']
        frameInfo['height'] = docInfo['height']
        
    return frameInfo

def exportFrame(document, node, frameNumber, exportPath, options):
    utils.setCurrentFrame(document, frameNumber)

    if node.bounds().width() == 0:
        frameInfo = utils.createKeyframeInfo("_blank", "", frameNumber)
        return frameInfo
    
    nodeName = node.name().strip()
    fileFormat = options.get('fileFormat', 'png')
    if '[jpeg]' in nodeName:
        fileFormat = 'jpeg'
    elif '[png]' in nodeName:
        fileFormat = 'png'
    elif '[exr]' in nodeName:
        fileFormat = 'exr'

    imageName = '{0}_{1}'.format( node.name().strip(), utils.intToStr(frameNumber))
    imagePath = os.path.join(exportPath, imageName) + '.' + fileFormat

    if options.get('cropToImageBounds'):
        bounds = QRect()
    else:
        bounds = QRect(0, 0, options.get('width', 1920), options.get('height', 1080))

    opacity = node.opacity()
    node.setOpacity(255)

    node.save(imagePath, options.get('resolution', 1), options.get('resolution', 1), krita.InfoObject(), bounds)

    node.setOpacity(opacity)
    
    # TODO check if the file was correctly exported. The Node.save() method always reports False :/

    frameInfo = utils.getKeyframeInfo(document, node, frameNumber, not options.get('cropToImageBounds', False))
    frameInfo['fileName'] = imagePath

    return frameInfo

def export(docInfo, document, nodeInfo, node, exportPath, options, progressdialog):
    nodeName = node.name().strip()

    print("OCA >> Exporting node: " + nodeName + " (" + node.type() + ")")

    progressdialog.setLabelText(i18n("Exporting") + " " + nodeName) # pylint: disable=undefined-variable

    frame = docInfo['startTime']

    if node.animated() or node.type() == 'grouplayer':
        nodeDir = os.path.join(exportPath, nodeName)
        prevFrameNumber = -1
        utils.mkdir( nodeDir )
        while frame <= docInfo['endTime']:
            progressdialog.setValue(frame)
            if (progressdialog.wasCanceled()):
                break

            if utils.hasKeyframeAtTime(node, frame):
                frameInfo = exportFrame(document, node, frame, nodeDir, options)
                if prevFrameNumber >= 0:
                    nodeInfo['frames'][-1]['duration'] = frame - prevFrameNumber
                nodeInfo['frames'].append(frameInfo)
                prevFrameNumber = frame
            frame = frame + 1

        # set the last frame duration
        if len(nodeInfo['frames']) > 0:
            f = nodeInfo['frames'][-1]
            f['duration'] = document.fullClipRangeEndTime() - f['frameNumber']

    else:
        frameInfo = exportFrame(document, node, frame, exportPath, options)
        frameInfo['duration'] = document.playBackEndTime() - document.playBackStartTime()
        nodeInfo['frames'].append(frameInfo)
