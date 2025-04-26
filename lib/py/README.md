# OCA Python Library

As this is still a first version in development, this module is not yet documented, but it will be done soon!

## Core

The core module contains the main, cross-platform OCA library, required by all other modules.

You can use it to load, validate and sanitize, manipulate, and save OCA data.

```py
import oca_core as oca

# Load a document
ocaDoc = oca.OCADocument("/path/to/an_oca_file.oca")
print( ocaDoc->name() ) # Document name

# Create a new document
otherOcaDoc = oca.OCADocument()
otherOcaDoc.setFileName("/path/to/somewhere_to_save_the_doc.oca")

# Create a layer
aLayer = oca.OCALayer()
aLayer.setName("Some layer name")

# Create a frame
aFrame = oca.OCAFrame()
aFrame.setDuration(240)
aFrame.setFrameNumber(0)
aFrame.setFileName("/path/to/pixmap.png")

# Store them in the doc
aLayer.appendFrame(aFrame)
otherOcaDoc.appendLayer(aLayer)

# Save the doc
otherOcaDoc.save()

```

## Krita

`oca_krita` is the module used to export (and maybe one day import) OCA data from [Krita](http://krita.org).

The library depends on `oca_core` which must be available in `sys.path`.

An official implementation of an [OCA Plugin for Krita using this module is available here](https://codeberg.org/OCA/OCA-Krita).

````py
import oca_krita as oca
import krita # The krita module, available when running the script in Krita

# Get the first Krita document
doc = krita.Krita.instance().documents()[0]
# Export to OCA
oca.kDocument.export(doc, "destination/folder")

# The OCA Core library is also available if you need
ocaDoc = oca.OCADocument("destination/folder/exported_doc.oca")
```