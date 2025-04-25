"""The OCALayer class"""

import os
import uuid
from .object import OCAObject
from .frame import OCAFrame
from .source import OCASource
from .labels import LABELS
from . import blending_modes
from . import layer_types

class OCALayer(OCAObject):
    """An OCA Layer"""

    def __init__(self, data=None):
        """Creates a layer.
        Provide the data parsed from a JSON OCA file to load an existing layer."""
        super().__init__()

        if data is None:
            data = {}

        self._parentId = ""
        self._animated = data.get('animated', True)
        self._fileType = data.get('fileType', 'png').lower()
        self._height = data.get('height', 0)
        self._id = data.get('id', str(uuid.uuid4()))
        self._inheritAlpha = data.get('inheritAlpha', False)
        self._label = data.get('label', -1)
        self._meta = data.get('meta', {})
        self._name = data.get('name', '')
        self._opacity = data.get('opacity', 1.0)
        self._passThrough = data.get('passThrough', False)
        self._position = data.get('position', [])
        self._reference = data.get('reference', False)
        self._source = OCASource( data.get('source', {}) )
        self._visible = data.get('visible', True)
        self._width = data.get('width', 0)
        self._document = None

        # Parse enums JSON data
        try:
            self.setLayerType(
                data.get('type', layer_types.PAINT)
            )
            self.setBlendingMode(
                data.get('blendingMode', blending_modes.NORMAL)
            )
        except ValueError as e:
            # Replace invalid values by defaults and log error
            self._type = layer_types.PAINT
            self._blendingMode = blending_modes.NORMAL

            self._status = OCAObject.PARSE_ERROR
            self._errors.append(e.args[0])

        # Set the source object

        # Load frames
        self._frames = []
        for frame in data.get('frames', ()):
            self.appendFrame( OCAFrame(frame) )

        # Load child layers
        self._childLayers = []
        for layer in data.get('childLayers', ()):
            self.appendLayer( OCALayer(layer) )

        # Cache the source doc for ocalayer
        self._sourceDocument = None

    def document(self):
        """The document containing this layer."""
        return self._document

    def documentPath(self) -> str:
        """The path of the current document."""
        if not self._document:
            return ""
        return self._document.path()

    def documentFileName(self) -> str:
        """The path to the file of the current document."""
        if not self._document:
            return ""
        return self._document.fileName()

    def isAnimated(self) -> bool:
        """Does this layer contain an animation?"""
        return self._animated

    def setAnimated(self, animated:bool):
        """Sets this as an animation or fixed frame."""
        self._animated = animated

    def blendingMode(self) -> str:
        """The layer blending mode"""
        return self._blendingMode

    def setBlendingMode(self, blendingMode:str):
        """Sets the layer blending mode"""
        if blendingMode in blending_modes.ALL_MODES:
            self._blendingMode  = blendingMode
        else:
            raise ValueError("Invalid blending mode: \"{}\"".format(blendingMode))

    def fileType(self):
        """The file type of the frames.
        i.e. the extension (lower case)"""
        return self._fileType

    def setFileType(self, fileType:str):
        """Sets the file type of the frames, i.e. the extension."""
        self._fileType = fileType.lower()

    def size(self) -> tuple[int,int]:
        """The layer size, in pixels."""
        return (
            self._width,
            self._height
        )

    def setSize(self, width:int, height:int):
        """Sets the layer size, in pixels."""
        self._width = width
        self._height = height

    def id(self) -> str:
        """The layer unique identifier"""
        return self._id

    def inheritAlpha(self) -> bool:
        """Does the layer inherit alpha?"""
        return self._inheritAlpha

    def setInheritAlpha(self, inherit:bool):
        """Sets alpha inherintance."""
        self._inheritAlpha = inherit

    def label(self) -> int:
        """The layer label"""
        return self._label

    def labelColor(self) -> tuple[float,float,float,float]:
        """A proposed color for the label, [r,g,b,a]"""
        if self._label > 0 and self._label < len(LABELS):
            return LABELS[self._label]
        return (0,0,0,1.0) # black by default

    def setLabel(self, label:int):
        """Sets the layer label"""
        self._label = label

    def name(self) -> str:
        """The layer name."""
        return self._name

    def setName(self, name:str):
        """Sets the layer name."""
        self._name = name

    def opacity(self) -> float:
        """The layer opacity."""
        return self._opacity

    def setOpacity(self, opacity:float):
        """Sets the layer opacity"""
        if opacity > 1.0:
            opacity = 1.0
        if opacity < 0.0:
            opacity = 0.0
        self._opacity = opacity

    def passThrough(self) -> bool:
        """The layer pass through mode, if it's a group or an ocalayer."""
        if self._type in layer_types.GROUP_TYPES:
            return self._passThrough
        else:
            return False

    def setPassThrough(self, passThrough:bool):
        """Sets the layer pass through mode. The layer must be a group or an ocalayer."""
        self._passThrough = passThrough

    def position(self) -> tuple[float,float]:
        """The (relative to its parent) position of the layer."""
        return self._position

    def setPosition(self, x:float, y:float):
        """Sets the relative position of the layer."""
        self._position = (x, y)

    def isReference(self):
        """Is this a reference which should not be rendered?"""
        return self._reference

    def setReference(self, reference:bool):
        """Sets the layer as a reference."""
        self._reference = reference

    def source(self):
        """The source of the layer if it's an instance type.
        None if this layer is not an instance"""
        if self._type in layer_types.INSTANCE_TYPES:
            return self._source
        return None

    def setSource(self, source:OCASource):
        """Sets the source for instance types."""
        self._source = source

    def sourceDocument(self):
        """The source document, if this is an ocalayer."""
        if self._type != layer_types.OCA:
            return None
        if not self._document:
            raise RuntimeError("Cannot get the source of a layer which is not part of a document.")

        # Load doc if not already cached
        if not self._sourceDocument:
            # Load source doc
            source = self.source()
            if not source:
                self._sourceDocument = None
                return None
            path = source.fileName( self.documentPath() )
            if not os.path.isfile(path):
                self._sourceDocument = None
                return None
            from .document import OCADocument # pylint: disable=import-outside-toplevel
            self._sourceDocument = OCADocument(path)

        return self._sourceDocument

    def sourceLayer(self):
        """The source layer, if this is an instance layer type."""
        if self._type not in layer_types.INSTANCE_TYPES:
            return None
        if not self._document:
            raise RuntimeError("Cannot get the source of a layer which is not part of a document.")

        source = self.source()
        if not source:
            return None
        if source.id() == "":
            return None

        if self._type == layer_types.CLONE:
            return self._document.getLayer(source.id())

        if self._type == layer_types.OCA:
            sourceDoc = self.sourceDocument()
            if not sourceDoc:
                return None
            return sourceDoc.getLayer(source.id())

        return None

    def layerType(self) -> str:
        """The type of the layer."""
        return self._type

    def setLayerType(self, layerType:str):
        """Sets the type of layer"""
        if layerType in layer_types.ALL_TYPES:
            self._type = layerType
        else:
            raise ValueError("Invalid layer type: \"{}\"".format(layerType))

    def isVisible(self) -> bool:
        """Is this layer visible?"""
        return self._visible

    def setVisible(self, visible:bool):
        """Sets the layer visibility."""
        self._visible = visible

    def frames(self) -> list[OCAFrame]:
        """The frames of the layer."""
        return self._frames

    def appendFrame(self, frame:OCAFrame):
        """Adds a frame at the end."""
        frame._setDocument(self._document) # pylint: disable=protected-access
        self._frames.append(frame)

    def setFrames(self, frames:list[OCAFrame]):
        """Sets the frames for this layer."""
        self._frames = []
        for frame in frames:
            self.appendFrame(frame)

    def layers(self) -> list:
        """The child layers if this is a group layer type."""

        if self._type == layer_types.GROUP:
            return self._childLayers

        # If we're an instance of a specific layer
        sourceLayer = self.sourceLayer()
        if sourceLayer:
            return sourceLayer.layers()

        # If we're an instance of a document
        sourceDoc = self.sourceDocument()
        if not sourceDoc:
            return []
        return sourceDoc.layers()

    def getLayer(self, layerId:str):
        """Gets a layer by its ID, or None if not found"""
        for layer in self.layers():
            if layer.id() == layerId:
                return layer
            # Recurse
            found = layer.getLayer(layerId)
            if found:
                return found
        return None

    def getFrame(self, frameId:str):
        """Gets a frame by its ID, or None if not found"""
        for layer in self.layers():
            for frame in layer.frames():
                if frame.id() == frameId:
                    return frame
            # Recurse
            found = layer.getFrame(frameId)
            if found:
                return found
        return None

    def appendLayer(self, layer):
        """Adds a child layer on top of the stack"""
        if layer in self._childLayers:
            raise ValueError("This layer {} is already a child of this layer.".format(layer.name()))
        self._takeLayerOwnership(layer)
        self._childLayers.append(layer)

    def setLayers(self, layers:list):
        """Sets the list of layers"""
        self._childLayers = []
        for layer in layers:
            self.appendLayer(layer)

    def insertLayer(self, i:int, layer):
        """Inserts a layer in the list at the given index"""
        if layer in self._childLayers:
            raise ValueError("This layer {} is already a child of this layer.".format(layer.name()))
        self._takeLayerOwnership(layer)
        self._childLayers.insert(i, layer)

    def removeLayer(self, layer):
        """Removes a layer from the list"""
        self._releaseLayerOwnership(layer)
        self._childLayers.remove(layer)

    def parentLayerId(self):
        """The parent layer id if it has one"""
        return self._parentId

    def toDict(self) -> dict:
        """Exports the layer as a simple python Dict,
        Which can then be written in a JSON file."""
        super()._sanitize()

        # Add data which is common to all layer types
        data:dict = {
            "blendingMode": self.blendingMode(),
            "id": self.id(),
            "inheritAlpha": self.inheritAlpha(),
            "label": self.label(),
            "meta": self.metadata(),
            "name": self.name(),
            "opacity": self.opacity(),
            "passThrough": self.passThrough(),
            "position": self.position(),
            "reference": self.isReference(),
            "type": self.layerType(),
            "visible": self.isVisible()
        }

        # Add standard layer data
        if self._type not in layer_types.INSTANCE_TYPES:
            w, h = self.size()
            data["animated"] = self.isAnimated()
            data["fileType"] = self.fileType()
            data["height"] = h
            data["width"] = w

            # Add frames
            data["frames"] = []
            for frame in self.frames():
                data['frames'].append(frame.toDict())

            # Add child layers
            if self._type == layer_types.GROUP:
                data["childLayers"] = []
                for layer in self.layers():
                    data["childLayers"].append(layer.toDict())
    
        # Add source info
        elif self.source():
            data["source"] = self.source().toDict()

        return data

    # ==== PROTECTED ====

    def _takeLayerOwnership(self, layer):
        layer._parentId =  self._id # pylint: disable=protected-access
        layer._setDocument(self._document) # pylint: disable=protected-access

    def _releaseLayerOwnership(self, layer):
        layer._parentId = "" # pylint: disable=protected-access
        layer._setDocument(None) # pylint: disable=protected-access
        layer._sourceDocument = None # pylint: disable=protected-access

    def _setDocument(self, doc):
        self._document = doc
        # Recurse
        for childLayer in self.layers():
            childLayer._setDocument(doc) # pylint: disable=protected-access
        # Frames
        for frame in self.frames():
            frame._setDocument(doc) # pylint: disable=protected-access

    # ==== PRIVATE ====

    def __eq__(self, other):
        return self.id() == other.id()
