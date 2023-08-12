from . import frame

def sanitize(ocaLayer, savePath=''):

    # Recursion
    if ocaLayer['type']  == 'grouplayer':
        for childLayer in ocaLayer['childLayers']:
            sanitize(childLayer, savePath)
        return
    
    for ocaFrame in ocaLayer['frames']:
        frame.sanitize(ocaFrame, savePath)
