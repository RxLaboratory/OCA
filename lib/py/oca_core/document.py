"""The OCADocument class"""

import os
import json
from .layer import OCALayer
from .config import VERSION

class OCADocument():
    """An OCA document"""

    # Document Status
    LOADED_STATUS = 'LOADED'
    SAVED_STATUS = 'SAVED'
    WRONG_VERSION_STATUS = 'WRONG_VERSION'

    def __init__(self, filepath:str = ''):
        """Creates the document.
        Provide filepath to load an existing document."""

        self.__fileName = ""
        self.__ocaVersion = VERSION

        oca = {}
        if os.path.isfile( filepath ):
            self.__fileName = filepath
            with open(filepath, 'r', encoding='utf8') as ocaFile:
                oca = json.loads(ocaFile.read())
                self.__ocaVersion = oca.get('ocaVersion', "0.0.0")

        # TODO Check ocaVersion against VERSION
        # to make sure everything can be loaded correctly!
        # If not, we should set a status property
        self.__status = OCADocument.LOADED_STATUS
        self.__error = ""

        # Parse the JSON data
        self.__backgroundColor = oca.get('backgroundColor', (0.0, 0.0, 0.0, 0.0))
        self.__colorDepth = oca.get('colorDepth', 'U8')
        self.__endTime = oca.get('endTime', 240)
        self.__frameRate = oca.get('frameRate', 24)
        self.__height = oca.get('height', 1080)
        self.__name = oca.get('name', "Untitled")
        self.__startTime = oca.get('startTime', 0)
        self.__width = oca.get('width', 1920)

        # Load layers
        self.__layers:list[OCALayer] = []
        for layer in oca.get('layers', ()):
            self.appendLayer( OCALayer(layer) )

        # Load metadata
        self.__meta = dict()
        metaPath = self.metadataFileName()
        if os.path.isfile(metaPath):
            with open(metaPath, 'r', encoding='utf8') as metaFile:
                self.__meta = json.loads(metaFile.read())

        self.__sanitize()

    def backgroundColor(self) -> tuple[float]:
        return self.__backgroundColor

    def setBackgroundColor(self, color:list|tuple ):
        self.__backgroundColor = color

    def colorDepth(self, depth:str ) -> str:
        return self.__colorDepth

    def setColorDepth(self, depth:str):
        self.__colorDepth = depth

    def timeRange(self) -> tuple[int]:
        return (self.__startTime, self.__endTime)

    def setTimeRange(self, timerange:tuple|list):
        self.__startTime = timerange[0]
        self.__endTime = timernge[1]

    def frameRate(self) -> float:
        return self.__frameRate

    def setFrameRate(self, frameRate:float):
        self.__frameRate = frameRate

    def name(self) -> str:
        return self.__name

    def setName(self, name:str):
        self.__name = name

    def size(self) -> tuple[int]:
        return (self.__width, self.__height)

    def setSize(self, width:int, height:int):
        self.__width = width
        self.__height = height

    def ocaVersion(self) -> str:
        return self.__ocaVersion

    def layers(self) -> list:
        return self.__layers

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

        self.__layers.append(layer)

    def metadata(self, key:str='', defaultValue = None):
        if key != "":
            return self.__meta.get(key, defaultValue)
        return self.__meta

    def setMetadata(self, key:str, value):
        self.__meta[key] = value

    def metadataFileName(self):
        """!
        @brief Gets the path to the metadata file associated to this OCA file.
        Note that the file represented by the returned path may not exist.

        Parameters : 
            @param ocaFilePath : str => The path to the OCA file

        @returns {string} The path to the metadata file.
        """
        return os.path.splitext( self.__fileName )[0] + "_meta.json"

    def status(self) -> str:
        return self.__status

    def hasError(self) -> bool:
        return self.__status in (OCADocument.WRONG_VERSION_STATUS,)

    def error(self) -> str:
        return self.__error

    # ==== PRIVATE ====

    def __sanitize(self):
        """Sanitizes all the data"""

        docPath = ''
        if self.__fileName != '':
            docPath = os.path.dirname(self.__fileName)
        
        for childLayer in self.__layers:
            childLayer._sanitize(docPath) # pylint: disable=protected-access
