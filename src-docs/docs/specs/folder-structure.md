# Folder Structure

The OCA format is a folder, containing an [OCA *JSON* data file](file.md) with all data about the document (except images), and image files, which can be one of these formats: *PNG*, *openEXR*, *SVG*.

## Data file

The OCA data file *must* be at the root of the OCA folder, and *should* have the same name.

There *must* be a single OCA data file in the folder, and it *must* be at the root.

## Metadata file

There *may* or *may not* be a metadata file at the root of the OCA folder, which is named after the OCA data file, suffixed with  `_meta` and with the `.json` extension.

The metadata is separated from the main OCA data file to make it easy for users to strip (or replace) all metadata from the file.

## Other files

Other files and folders *may* be stored as follow, but as the JSON data contains all (relative) paths to all files, that's not mandatory.

```
▾ Document_name.oca
    · Document_name.oca
    · Document_name_meta.json
    ▾ Layer_name_1
        · Layer_name_1_00000.png
        · Layer_name_1_00110.png
        · Layer_name_1_00112.png
        · Layer_name_1_00114.png
        · Layer_name_1_00200.png
    ▾ Group_name_2
        ▾ Layer_name_3
            · Layer_name_3_00000.png
            · Layer_name_3_00003.png
        ▸ Layer_name_4
        ▸ Layer_name_5
    ▸ Group_name_6
```

!!! note
    The `.oca` file at the root may also use the extension `.json`.

!!! tip
    All layers may be stored in a single subfolder with an arbitrary name (e.g. "content", "data", "layers", "Document"...) instead of directly at the root.
