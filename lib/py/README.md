# OCA Python Library

As this is still a first version in development, this module is not yet documented, but it will be done soon!

## Core

The core library contains the main, cross-platform OCA library, required by all other modules.

You can use it to load, validate and sanitize, manipulate, and save OCA data.

```py
import oca_core as oca

ocaDoc = oca.file.load("an_oca_file.oca")
print( ocaDoc["name"] ) # Document name

oca.file.save(ocaDoc, "another_oca_file.oca")

```

## Krita

`oca_krita` is the library used to export (and one day import) OCA data from [Krita](http://krita.org)

````py
import oca_krita as oca
import krita # The krita module, available when running the script in Krita

# Get the first Krita document
doc = krita.Krita.instance().documents()[0]
# Export to OCA
docPath = oca.kritaDocument.export(doc, "destination/folder")

# The OCA Core library is also available
ocaDoc = oca.file.load(docPath)
```