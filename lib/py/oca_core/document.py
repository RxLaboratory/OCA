import os
from . import layer

def sanitize(ocaDoc, savePath='') :

    if savePath != '':
        docPath = os.path.dirname(savePath)
    else:
        docPath = ''

    for childLayer in ocaDoc['layers']:
        layer.sanitize(childLayer, docPath)
        pass