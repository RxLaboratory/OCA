"""An OCA Frame"""

import os
import uuid
from .object import OCAObject

class OCAFrame(OCAObject):
    """An OCA Frame"""

    BLANK_NAME = '_blank'

    def __init__(self, data=None ):
        """Creates a frame.
        Provide the data parsed from a JSON OCA file to load an existing frame."""
        super().__init__()

        if data is None:
            data = {}

        self._fileName = data.get('fileName', "")
        self._name = data.get('name', OCAFrame.BLANK_NAME)

        self._duration = data.get('duration', 1)
        self._frameNumber = data.get('frameNumber', 0)
        self._height = data.get('height', 0)
        self._id = data.get('id', str(uuid.uuid4()))
        self._meta = data.get('meta', {})
        self._name = data.get('name', OCAFrame.BLANK_NAME)
        self._opacity = data.get('opacity', 1.0)
        self._position = data.get('position', [])
        self._width = data.get('width', 0)

    def fileName(self) -> str:
        """The (relative) path to the file."""
        return self._fileName

    def setFileName(self, fileName:str):
        """Sets a new file for the frame."""
        self._fileName = fileName

    def duration(self) -> int:
        """The duration of the frame, in frames."""
        return self._duration

    def setDuration(self, duration:int):
        """Sets the duration, in frames."""
        self._duration = duration

    def frameNumber(self) -> int:
        """The frame number (the start time of the frame)."""
        return self._frameNumber

    def setFrameNumber(self, frameNumber:int):
        """Sets the frame number."""
        self._frameNumber = frameNumber

    def size(self) -> tuple[int, int]:
        """The size of the frame, in pixels."""
        return (
            self._width,
            self._height
        )

    def setSize(self, width:int, height:int):
        """Sets the size of the frame, in pixels."""
        self._width = width
        self._height = height
    
    def id(self) -> str:
        """The unique identifier of the frame."""
        return self._id

    def name(self) -> str:
        """The name of the frame."""
        if self.fileName() == "":
            return OCAFrame.BLANK_NAME
        return self._name

    def setName(self, name:str):
        """Sets the name of the frame"""
        self._name = name

    def isBlank(self) -> bool:
        """Is this a blank frame?"""
        return self.name() == OCAFrame.BLANK_NAME

    def opacity(self) -> float:
        """The opacity of the frame."""
        return self._opacity

    def setOpacity(self, opacity):
        """Sets the opacity of the frame."""
        if opacity < 0:
            opacity = 0
        if opacity > 1.0:
            opacity = 1.0
        self._opacity = opacity

    def position(self) -> tuple[float,float]:
        """The position of the frame, relative to the layer."""
        return self._position

    def setPosition(self, x:float, y:float):
        """Sets the position of the frame, relative to the layer."""
        self._position = (x, y)

    # ==== PRIVATE ====

    def __eq__(self, other):
        return self.id() == other.id()
