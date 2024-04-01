"""! @brief OCA file I/O
 @file file.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

import json
import os
from . import document
from .config import VERSION

def load(filepath:str):
    """!
    @brief Loads the OCA file.

    Parameters : 
        @param filepath => The path to the .oca file
    
    @returns {dict} The Data, including any metadata under the "meta" key.
    """

    oca = {}
    with open(filepath, 'r', encoding='utf8') as ocaFile:
        oca = json.loads(ocaFile.read())

    # Check if there's some metadata file and load it
    ocaMetaPath = getMetaPath(filepath)
    if os.path.isfile(ocaMetaPath):
        with open(ocaMetaPath, 'r', encoding='utf8') as metaFile:
            oca['meta'] = json.loads(metaFile.read())

    return oca

def save(ocaDoc:dict, filepath:str):
    """!
    @brief Saves the OCA document to an OCA file,
    And a sidecar metadata file if the 'meta' key exists in the document.

    Parameters : 
        @param ocaDoc : dict => The document to save
        @param filepath : str => The filename where to save
    """

    document.sanitize(ocaDoc, filepath)

    # Separate the metadata and set the ocaVersion
    meta = ocaDoc.get('meta', {})
    ocaDoc.pop('meta', None)
    ocaDoc['ocaVersion'] = VERSION

    with open(filepath,  "w", encoding='utf-8') as ocaFile:
        ocaFile.write( json.dumps(ocaDoc, indent=4) )

    if meta:
        metaPath = getMetaPath(filepath)
        with open(metaPath,  "w", encoding='utf-8') as metaFile:
            metaFile.write( json.dumps(meta, indent=4) )

def getMetaPath(ocaFilePath:str):
    """!
    @brief Gets the path to the metadata file associated to this OCA file.
    Note that the file represented by the returned path may not exist.

    Parameters : 
        @param ocaFilePath : str => The path to the OCA file

    @returns {string} The path to the metadata file.
    """
    return os.path.splitext(ocaFilePath)[0] + "_meta.json"
