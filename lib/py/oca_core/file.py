import json
from . import document

from PyQt5.QtWidgets import QMessageBox

def load(filepath):
    oca = {}
    with open(filepath, 'r') as ocaFile:
        oca = json.loads(ocaFile.read())
    return oca

def save(ocaDoc, filepath):

    document.sanitize(ocaDoc, filepath)

    with open(filepath,  "w", encoding='utf-8') as ocaFile:
        ocaFile.write( json.dumps(ocaDoc, indent=4) )
