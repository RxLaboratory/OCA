"""An OCA Frame"""

import os

class OCAFrame():
    """An OCA Frame"""
    # TODO

    BLANK_NAME = '_blank'

    def __init__(self, data:dict={} ):
        """Creates a frame.
        Provide the data parsed from a JSON OCA file to load an existing frame."""

        self.__fileName = data.get('fileName', "")
        self.__name = data.get('name', OCAFrame.BLANK_NAME)

    def _sanitize(self, savePath=''):

        if self.__name != OCAFrame.BLANK_NAME:

            # Set paths relative
            if savePath != '':
                self.__fileName = os.path.relpath(
                    self.__fileName,
                    savePath
                    )
            
            # Path must use a / delimiter, no matter the platform
            self.__fileName = self.__fileName.replace("\\","/")

        else:
            self.__fileName = ""

