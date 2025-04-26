# File Specificatons

## OCA Data

The OCA data is stored in a standard text file.

- The file extension *must* be **`.oca`**.
- The text encoding *must* be **`UTF-8`**.
- The data must be formatted as [***JSON***](https://en.wikipedia.org/wiki/JSON).  
    *We chose* JSON *(over* XML *or* YAML *) because it is both very easy to use with any programming language, and easy to read and edit by humans.*
    - The *JSON* string *should* be **pretty printed**, with a 4-space indentation.  
        *This makes it easier to read by humans.*
    - There *must* be a **single [*Root (Document) Object*](root.md)** which itself contains all data.
    - There ***must not* be any other data** than what is listed in this document.  
        *This is needed to prevent potential conflicts with future updates.*

## Document Metadata

Any metadata associated to the whole document *must* be stored in the metadata file.

The metadata is separated from the main OCA data file to make it easy for users to strip (or replace) all metadata from the file.

- It must have the same name as the OCA Data file, suffixed with **`_meta`**, and the file extension *must* be **`.json`**.
- The text encoding *must* be **`UTF-8`**.
- The data must be formatted as [***JSON***](https://en.wikipedia.org/wiki/JSON).  
    - The *JSON* string *should* be **pretty printed**, with a 4-space indentation.  
    - There *must* be a **single [*Metadata Object*](meta.md)** which itself contains all metadata.

## Image Data

Image data is stored in standard image files, according to the type sepcified in the OCA data file.

- For `paintlayers` and `U8` or `U16` color depths, images must be **PNG** files.
    - Their colorspace *must* be **sRGB**.
    - Their **color depth *must* correspond to the color depth set in the OCA data**  
        (`U8` for 8-bit integer, `U16` for 16-bit integer).
    - There can be only a **single color depth used for the whole document**.
    - The **alpha channel *must not* be premultiplied**.
- For `paintlayers` and `F16` or `F32` color depths, images must be **openEXR** files.
    - Their colorspace *should* be **linear RGB**.  
        There's no way yet to specify the color space with OCA; you may add its name in the file name.
    - Their **color depth *must* correspond to the color depth set in the OCA data**  
        (`F16` for "half" 16-bit float, `F32` for 32-bit float).
    - There can be only a **single color depth used for the whole document**.
    - They *should not* use the *Luma/Chroma* option.
    - They ***must* contain *at least* four channels called `R, G, B, A`**, and they *may* contain other AOVs.
    - The **alpha channel *must* be premultiplied with black**.
- For `vectorlayers`, images must be **SVG** files.

!!! wip
    We plan to add the ability to use other color spaces, and store the info in the OCA data.
