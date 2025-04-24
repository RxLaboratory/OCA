"""! @brief Methods to handle OCA metadata
 @file metadata.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

from ..oca_core import utils # pylint: disable=relative-beyond-top-level

# The plugin defaut options
PLUGIN_DEFAULT_OPTIONS = {
    "defaultDocumentName": "Document",
}

def updateMetadata(metadata:dict):
    """!
    @brief Updates the metadata with this plugin specific metadata

    Parameters : 
        @param metadata : dict => The current metadata

    @return {dict}
    """
    m = utils.mergeDicts(metadata, PLUGIN_METADATA)
    m['created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return m
