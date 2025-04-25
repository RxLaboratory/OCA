"""A reference to another OCA Layer or Document"""

import os

class OCASource():
    """A reference to another OCA Layer or Document"""

    def __init__(self, data=None ):

        if data is None:
            data = {}

        self._id = data.get('id', "")
        self._absFileName = data.get('absFileName', "")
        self._relFileName = data.get('relFileName', "")
        self._timeOffset = data.get('timeOffset', 0)

    def id(self) -> str:
        """The ID of the instanced source"""
        return self._id

    def setId(self, uid:str):
        """Sets the source uid"""
        self._id = uid

    def fileName(self, documentFolderPath:str ) -> str:
        """Retrieves the absolute path to the file, making sure it exists.
        Returns an empty string if the document can't be found.
        Priority is given to the internal relative path."""

        path = ""

        # Try from relative path
        if self._relFileName != "":
            path = os.path.join(documentFolderPath, self._relFileName)
            path = os.path.normpath(path)
            if os.path.isfile(path):
                return path

        # Try from absolute path
        if self._absFileName != "":
            path = os.path.normpath(self._absFileName)
            if os.path.isfile(path):
                return path

        return path

    def asbFileName(self) -> str:
        """The absolute path to the instanced OCA document, at time of saving."""
        return self._absFileName

    def relFileName(self) -> str:
        """The path relative to the current doc of the instanced OCA document."""
        return self._relFileName

    def timeOffset(self) -> int:
        """The time offset in frames."""
        return self._timeOffset

    def toDict(self, docPath:str) -> dict:
        """Exports the source as a simple python Dict,
        Which can then be written in a JSON file."""

        absFileName = self.fileName(docPath)
        relFileName = self.relFileName()
        if (not os.path.isfile(relFileName)
            and os.path.isfile(absFileName)):
            relFileName = os.path.relpath(absFileName, docPath)

        if not os.path.isfile(absFileName):
            absFileName = ''
        else:
            self._absFileName = absFileName

        if not os.path.isfile(relFileName):
            relFileName = ''
        else:
            self._relFileName = relFileName

        return {
            "absFileName": absFileName,
            "relFileName": relFileName,
            "id": self.id(),
            "timeOffset": self.timeOffset()
        }
