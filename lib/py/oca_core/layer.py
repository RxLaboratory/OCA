"""The OCALayer class"""

import uuid
from .frame import OCAFrame
from .source import OCASource
from . import blending_modes
from . import layer_types

class OCALayer():
    """An OCA Layer"""

    def __init__(self, data:dict = {}):
        """Creates a layer.
        Provide the data parsed from a JSON OCA file to load an existing layer."""

        self.__animated = data.get('animated', True)
        self.__fileType = data.get('fileType', 'png')
        self.__height:int = data.get('height', 0)
        self.__id = data.get('id', str(uuid.uuid4()))
        self.__inheritAlpha = data.get('inheritAlpha', False)
        self.__label = data.get('label', -1)
        self.__meta = data.get('meta', dict())
        self.__name = data.get('name', '')
        self.__opacity = data.get('opacity', 1.0)
        self.__passThrough = data.get('passThrough', False)
        self.__position = data.get('position', [])
        self.__reference = data.get('reference', False)
        self.__source = OCASource( data.get('source', dict()) )
        self.__visible = data.get('visible', True)
        self.__width:int = data.get('width', 0)

        try: # Silently replace invalid values by defaults
            self.setLayerType(
                data.get('type', layer_types.PAINT)
            )
            self.setBlendingMode(
                data.get('blendingMode', blending_modes.NORMAL)
            )
        except ValueError:
            self.__type = layer_types.PAINT
            self.__blendingMode = blending_modes.NORMAL

        # Load frames
        self.__frames:list[OCAFrame] = []
        for frame in data.get('frames', ()):
            self.appendFrame( OCAFrame(frame) )

        # Load child layers
        self.__childLayers:list[OCALayer] = []
        for layer in data.get('childLayers', ()):
            self.appendLayer( OCALayer(layer) )

    def isAnimated(self) -> bool:
        return self.__animated

    def blendingMode(self) -> str:
        return self.__blendingMode

    def setBlendingMode(self, blendingMode:str):
        if blendingMode in blending_modes.ALL_MODES:
            self.__blendingMode  = blendingMode
        else:
            raise ValueError("Invalid blending mode")

    def fileType(self):
        return self.__fileType

    def setFileType(self, fileType:str):
        self.__fileType = fileType

    def size(self) -> tuple[int,int]:
        return (
            self.__width,
            self.__height
        )

    def setSize(self, width:int, height:int):
        self.__width = size[0]
        self.__height = size[1]

    def id(self) -> str:
        return self.__id;

    def inheritAlpha(self) -> bool:
        return self.__inheritAlpha

    def setInheritAlpha(self, inherit:bool):
        self.__inheritAlpha = inherit

    def label(self) -> int:
        return self.__label

    def setLabel(self, label:int):
        self.__label = label

    def metadata(self, key:str='', defaultValue = None):
        if key != "":
            return self.__meta.get(key, defaultValue)
        return self.__meta

    def setMetadata(self, key:str, value):
        self.__meta[key] = value

    def name(self) -> str:
        return self.__name

    def setName(self, name:str):
        self.__name = name

    def opacity(self) -> float:
        return self.__opacity

    def setOpacity(self, opacity:float):
        if opacity > 1.0:
            opacity = 1.0
        if opacity < 0.0:
            opacity = 0.0
        self.__opacity = opacity

    def passThrough(self) -> bool:
        return self.__passThrough

    def setPassThrough(self, passThrough:bool):
        self.__passThrough = passThrough

    def position(self) -> tuple[float,float]:
        return self.__position

    def setPosition(self, x:float, y:float):
        self.__position = (x, y)

    def isReference(self):
        return self.__reference

    def setReference(self, reference:bool):
        self.__reference = reference

    def source(self) -> OCASource:
        return self.__source

    def setSource(self, source:OCASource):
        self.__source = source

    def layerType(self) -> str:
        return self.__type

    def setLayerType(self, layerType:str):
        if layerType in layer_types.ALL_TYPES:
            self.__type = layerType
        else:
            raise ValueError("Invalid layer type")

    def isVisible(self) -> bool:
        return self.__visible

    def setVisible(self, visible:bool):
        self.__visible = visible

    def frames(self) -> list[OCAFrame]:
        return self.__frames

    def appendFrame(self, frame:OCAFrame):
        self.__frames.append(frame)

    def layers(self) -> list[OCALayer]:
        return self.__childLayers

    def appendLayer(self, layer:OCALayer):
        # Sanitize and append
        w, h = layer.size()
        if w == 0:
            w = self.__width
        if h == 0:
            h = self.__height
        layer.setSize(w, h)

        p = layer.position()
        if len(p) != 2:
            layer.setPosition(
                self.__width/2,
                self.__height/2
            )

        self.__childLayers.append(layer)

    # ==== PROTECTED ====

    def _sanitize(self, savePath:str ):

        # Recursion
        for childLayer in self.__childLayers:
            childLayer._sanitize(savePath) # pylint: disable=protected-access

        for frame in self.__frames:
            frame._sanitize(savePath) # pylint: disable=protected-access
