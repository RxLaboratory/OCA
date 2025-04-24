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

    def id(self) -> str:
        """The ID of the instanced source"""
        return self._id

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
