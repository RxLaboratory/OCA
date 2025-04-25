"""The base class for main OCA objects,
with some metadata and a status"""

class OCAObject():

    PARSE_ERROR = 'PARSE_ERROR'
    LOADED = 'LOADED'
    SAVED = 'SAVED'
    WRONG_VERSION = 'WRONG_VERSION'

    def __init__(self):
        self._status = OCAObject.LOADED
        self._errors = []
        self._meta = {}

    def status(self):
        """The data status"""
        return self._status

    def hasError(self):
        """Checks if there are errors in the data"""
        return self._status in (
            OCAObject.PARSE_ERROR,
            OCAObject.WRONG_VERSION
        )

    def errors(self) -> list[str]:
        """The errors"""
        return self._errors

    def lastError(self) -> str:
        """The last error"""
        if len(self._errors) == 0:
            return ""

        return self._errors[-1]

    def metadata(self, key:str='', defaultValue = None):
        """Gets some metadata.
        If the key is empty, the whole metadata dict is returned."""
        if key != "":
            return self._meta.get(key, defaultValue)
        return self._meta

    def setMetadata(self, key:str, value):
        """Sets some metadata"""
        self._meta[key] = value

    def setMeta(self, data):
        """Sets the whole metadata dict."""
        self._meta = data

    def _sanitize(self) -> bool:
        """Sanitizes the data.
        May change the status and add errors.
        Returns true if everything works correctly."""

        # Reinit status
        self._status = OCAObject.LOADED
        self._errors = []

        # Make sure the metadata is a valid dictionnary
        if not isinstance(self._meta, dict):
            self._status = OCAObject.PARSE_ERROR
            self._errors.append("The metadata is not a valid dictionnary.")
            self._meta = {}

        return not self.hasError()
