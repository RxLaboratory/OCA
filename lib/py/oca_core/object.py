"""The base class for main OCA objects,
with some metadata and a status"""

class OCAObject():

    PARSE_ERROR = 'PARSE_ERROR'
    LOADED = 'LOADED'
    SAVED = 'SAVED'
    WRONG_VERSION = 'WRONG_VERSION'
    WRITE_ERROR = 'WRITE_ERROR'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'

    def __init__(self):
        self._status = OCAObject.LOADED
        self._errors = []
        self._meta = {}

    def status(self):
        """The data status"""
        return self._status

    def setStatus(self, status:str):
        """Changes the status"""
        self._status = status

    def hasError(self) -> bool:
        """Checks if there are errors in the data"""
        return self._status in (
            OCAObject.PARSE_ERROR,
            OCAObject.WRONG_VERSION,
            OCAObject.WRITE_ERROR,
            OCAObject.UNKNOWN_ERROR
        )

    def hasWriteError(self) -> bool:
        """Checks if errors occured when exporting"""
        return self._status in (
            OCAObject.WRITE_ERROR,
            OCAObject.UNKNOWN_ERROR
        )

    def hasReadError(self) -> bool:
        """Checks if errors occured when loading"""
        return self._status in (
            OCAObject.PARSE_ERROR,
            OCAObject.WRONG_VERSION,
            OCAObject.UNKNOWN_ERROR
        )

    def errors(self) -> list[str]:
        """The errors"""
        return self._errors

    def lastError(self) -> str:
        """The last error"""
        if len(self._errors) == 0:
            return ""

        return self._errors[-1]

    def addError(self, error:str, newStatus:str='UNKNOWN_ERROR'):
        """Appends an error message"""
        self._errors.append(error)
        self.setStatus(newStatus)

    def metadata(self, key:str='', defaultValue = None):
        """Gets some metadata.
        If the key is empty, the whole metadata dict is returned."""
        if key != "":
            return self._meta.get(key, defaultValue)
        meta = self._meta
        if len(self._errors) > 0:
            meta['errors'] = self._errors
        if self.hasError():
            meta['error_status'] = self._status
        return meta

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

        # Make sure the metadata is a valid dictionnary
        if not isinstance(self._meta, dict):
            self._status = OCAObject.UNKNOWN_ERROR
            self._errors.append("The metadata is not a valid dictionnary.")
            self._meta = {}

        return not self.hasError()
