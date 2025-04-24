"""! @brief OCA file I/O
 @file file.py
 @section authors Author(s)
  - Created by Nicolas Dufresne on 4/1/2024 .
"""

import json
import os
import warnings
from .config import VERSION

def load(filepath:str):
    """Deprecated"""
    warnings.warn("OCA as a simple dict is deprecated. Use the new OCADocument class", DeprecationWarning)

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
    """Deprecated"""
    warnings.warn("OCA as a simple dict is deprecated. Use the new OCADocument class", DeprecationWarning)

    sanitize(ocaDoc, filepath)

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
    """Deprecated"""
    warnings.warn("OCA as a simple dict is deprecated. Use the new OCADocument class", DeprecationWarning)
    return os.path.splitext(ocaFilePath)[0] + "_meta.json"

def sanitize(ocaDoc, savePath='') :
    """Deprecated"""
    if savePath != '':
        docPath = os.path.dirname(savePath)
    else:
        docPath = ''
    for childLayer in ocaDoc['layers']:
        sanitizeLayer(childLayer, docPath)

def sanitizeLayer(ocaLayer, savePath=''):
    """Deprecated"""
    # Recursion
    if ocaLayer['type']  == 'grouplayer':
        for childLayer in ocaLayer['childLayers']:
            sanitize(childLayer, savePath)
        return
    for ocaFrame in ocaLayer['frames']:
        sanitizeFrame(ocaFrame, savePath)

def sanitizeFrame(ocaFrame, savePath=''):
    """Deprecated"""
    if ocaFrame['name'] != '_blank':
        # Set paths relative
        if savePath != '':
            ocaFrame['fileName'] = os.path.relpath(
                ocaFrame['fileName'],
                savePath
                )
        # Path must use a / delimiter, no matter the platform
        ocaFrame['fileName'] = ocaFrame['fileName'].replace("\\","/")
    else:
        ocaFrame['fileName'] = ""
