import os

def sanitize(ocaFrame, savePath=''):

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
