"""The OCADocument class"""

import os
import json
from . import color_depths
from .object import OCAObject
from .layer import OCALayer
from .frame import OCAFrame
from .config import VERSION

class OCADocument(OCAObject):
    """An OCA document"""

    def __init__(self, filepath:str = ''):
        """Creates the document.
        Provide filepath to load an existing document."""
        super().__init__()

        self._fileName = ""
        self._ocaVersion = VERSION

        oca = {}
        if os.path.isfile( filepath ):
            self._fileName = filepath
            with open(filepath, 'r', encoding='utf8') as ocaFile:
                oca = json.loads(ocaFile.read())
                self._ocaVersion = oca.get('ocaVersion', "0.0.0")

        # TODO Check ocaVersion against VERSION
        # to make sure everything can be loaded correctly!
        # If not, we should set the status to WRONG_VERSION

        # Parse the basic JSON data
        self._backgroundColor = oca.get('backgroundColor', (0.0, 0.0, 0.0, 0.0))
        self._endTime = oca.get('endTime', 240)
        self._frameRate = oca.get('frameRate', 24)
        self._height = oca.get('height', 1080)
        self._name = oca.get('name', "Untitled")
        self._startTime = oca.get('startTime', 0)
        self._width = oca.get('width', 1920)

        # Parse enums JSON data
        try:
            self.setColorDepth(
                oca.get('colorDepth', color_depths.UINT8)
            )
        except ValueError as e:
            # Replace invalid values by defaults and log error
            self._colorDepth = color_depths.UINT8

            self._status = OCAObject.PARSE_ERROR
            self._errors.append(e.args[0])

        # Load layers
        self._layers:list[OCALayer] = []
        for layer in oca.get('layers', ()):
            self.appendLayer( OCALayer(layer) )

        # Load metadata
        metaPath = self.metadataFileName()
        if os.path.isfile(metaPath):
            with open(metaPath, 'r', encoding='utf8') as metaFile:
                self._meta = json.loads(metaFile.read())

        self._sanitize()

    def fileName(self) -> str:
        """The document file."""
        return os.path.normpath(
            self._fileName
        )

    def backgroundColor(self) -> tuple[float]:
        """The document background color, visible through layer transparency"""
        return self._backgroundColor

    def setBackgroundColor(self, color:tuple ):
        """Sets the document background color"""
        self._backgroundColor = color

    def colorDepth(self ) -> str:
        """The color depth of the layers (bit depth)"""
        return self._colorDepth

    def setColorDepth(self, depth:str):
        """Sets the color depth of the layers (bit depth)"""
        if not depth in color_depths.ALL_DEPTHS:
            raise ValueError("Invalid color depth: \"{}\"".format(depth))
        self._colorDepth = depth

    def timeRange(self) -> tuple[int,int]:
        """The start and end time of the document, in frames."""
        return (self._startTime, self._endTime)

    def setTimeRange(self, timerange:tuple|list):
        """Sets the start and end time of the document, in frames."""
        self._startTime = timerange[0]
        self._endTime = timerange[1]

    def frameRate(self) -> float:
        """The framerate of the document, in frames per second"""
        return self._frameRate

    def setFrameRate(self, frameRate:float):
        """Sets the framerate of the document, in frames per second"""
        self._frameRate = frameRate

    def name(self) -> str:
        """The name of the document"""
        return self._name

    def setName(self, name:str):
        """Sets the name of the document"""
        self._name = name

    def size(self) -> tuple[int,int]:
        """The document size, in pixels"""
        return (self._width, self._height)

    def setSize(self, width:int, height:int):
        """Sets the size of the document, in pixels"""
        self._width = width
        self._height = height

    def ocaVersion(self) -> str:
        """The version used to save this OCA Document"""
        return self._ocaVersion

    def layers(self) -> list:
        """The list of layers in this document"""
        return self._layers

    def moveLayerUp(self, layer:OCALayer):
        """Moves a layer up in the list"""
        try:
            i = self._layers.index(layer)
        except ValueError:
            return
        # Already at the top
        if i == len(self._layers)-1:
            return
        self._layers.insert(i+1, self._layers.pop(i))

    def moveLayerDown(self, layer:OCALayer):
        """Moves a layer down in the list"""
        try:
            i = self._layers.index(layer)
        except ValueError:
            return
        # Already at the bottom
        if i <= 0:
            return
        self._layers.insert(i-1, self._layers.pop(i))

    def getLayer(self, layerId:str):
        """Gets a layer by its ID, or None if not found"""
        for layer in self._layers:
            found = layer.getLayer(layerId)
            if found:
                return found
        return None

    def getFrame(self, frameId:str):
        """Gets a frame by its ID, or None if not found"""
        for layer in self._layers:
            found = layer.getFrame(frameId)
            if found:
                return found
        return None

    def appendLayer(self, layer:OCALayer):
        """Adds a layer to the document"""
        if layer in self._layers:
            raise ValueError("This layer {} is already in the document.".format(layer.name()))
        self._takeLayerOwnership(layer)
        self._layers.append(layer)

    def insertLayer(self, i:int, layer:OCALayer):
        """Inserts a layer in the list at the given index"""
        if layer in self._layers:
            raise ValueError("This layer {} is already in the document.".format(layer.name()))
        self._takeLayerOwnership(layer)
        self._layers.insert(i, layer)

    def removeLayer(self, layer:OCALayer):
        """Removes a layer from the list"""
        self._releaseLayerOwnership(layer)
        self._layers.remove(layer)

    def metadataFileName(self):
        """!
        @brief Gets the path to the metadata file associated to this OCA file.
        Note that the file represented by the returned path may not exist.

        Parameters : 
            @param ocaFilePath : str => The path to the OCA file

        @returns {string} The path to the metadata file.
        """
        return os.path.splitext( self._fileName )[0] + "_meta.json"

    # ==== PROTECTED ====

    def _takeLayerOwnership(self, layer:OCALayer):
        layer._parentId = "" # pylint: disable=protected-access
        layer._document = self # pylint: disable=protected-access

    def _releaseLayerOwnership(self, layer:OCALayer):
        layer._parentId = "" # pylint: disable=protected-access
        layer._document = None # pylint: disable=protected-access

    def _sanitize(self) -> bool:
        """Sanitizes all the data"""

        super()._sanitize()

        docPath = ''
        if self._fileName != '':
            docPath = os.path.dirname(self._fileName)

        for childLayer in self._layers:
            ok = self._sanitizeLayer(childLayer, docPath)
            if not ok:
                self._status = OCAObject.PARSE_ERROR
                self._errors.append("Parse error in layer {}".format(childLayer.name()))

        return not self.hasError()

    def _sanitizeLayer(self, layer:OCALayer, docPath:str) -> bool:
        """Sanitizes the data in a layer"""

        # Recursion
        for childLayer in layer.layers():
            ok = self._sanitizeLayer(childLayer, docPath)
            if not ok:
                layer._status = OCAObject.PARSE_ERROR # pylint: disable=protected-access
                layer._errors.append("Parse error in layer {}".format(childLayer.name()))  # pylint: disable=protected-access

        # Sanitize frames
        for frame in layer.frames():
            ok = self._sanitizeFrame(frame, docPath)
            if not ok:
                layer._status = OCAObject.PARSE_ERROR # pylint: disable=protected-access
                layer._errors.append("Parse error in frame {}".format(frame.name()))  # pylint: disable=protected-access

        # Sanitize position and size
        w, h = layer.size()
        # Default size is the document size
        w = w | self.size()[0]
        h = h | self.size()[1]
        layer.setSize(w, h)

        p = layer.position()
        if len(p) != 2:
            # Default position is centered on parent
            parentLayer = self.getLayer(layer.parentLayerId())
            if not parentLayer:
                parentLayer = self
            pw, ph = parentLayer.size()
            layer.setPosition( pw/2, ph/2 )

        return not layer.hasError()

    def _sanitizeFrame(self, frame:OCAFrame, docPath) -> bool:
        """Sanitizes the data in a frame"""

        # Make sure all paths are relative to the document folder.
        if not frame.isBlank():
            fName = frame.fileName()
            if docPath != '':
                fName = os.path.relpath( fName, docPath )
            # Path must use a / delimiter, no matter the platform
            fName = fName.replace("\\","/")

            frame.setFileName(fName)
        # Blank frames should not have any path
        else:
            frame.setFileName("")

        return not frame.hasError()
