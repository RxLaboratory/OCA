"""! @brief Methods to handle OCA metadata
 @file metadata.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

from datetime import datetime
import krita # pylint: disable=import-error
from ..oca_core import VERSION # pylint: disable=relative-beyond-top-level
from ..oca_core import utils # pylint: disable=relative-beyond-top-level

# The plugin specific metadata
PLUGIN_METADATA = dict(
    originApp="Krita",
    originAppVersion=Application.version(),
    exportedBy="OCA for Krita",
    exportedByID="org.rxlaboratory.oca.krita",
    exportedByOrg="RxLaboratory",
    exportedByURL="http://rxlaboratory.org/tools/oca/",
    ocaVersion=VERSION,
)

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
