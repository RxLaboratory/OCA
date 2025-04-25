"""A list of common image types, by extension.
May be useful for OCA Plugins"""

import os

def getFileType(path:str):
    """Gets the file extension, lower case, without leading dot"""
    ext = os.path.splitext(path)[-1].lower()
    if len(ext) > 1:
        ext = ext[1:]
    return ext

KRITA = 'kra'
KRITA_ARCHIVE = 'krz'
OPEN_RASTER = 'ora'
OPEN_EXR = 'exr'
GIF = 'gif'
JPEG = 'jpg'
JPEG_2 = 'jpeg'
PNG = 'png'
PHOTOSHOP = 'psd'
PHOTOSHOP_BIG = 'psb'
TARGA = 'tga'
TIFF = 'tif'
WEBP = 'webp'
BMP = 'bmp'
SVG = 'svg'

VECTOR_TYPES = (
    SVG
)

LAYERED_TYPES = (
    KRITA,
    KRITA_ARCHIVE,
    OPEN_RASTER,
    OPEN_EXR,
    PHOTOSHOP,
    PHOTOSHOP_BIG,
    TIFF,
)

RASTER_TYPES = (
    GIF,
    JPEG,
    JPEG_2,
    PNG,
    TARGA,
    WEBP,
    BMP,
)

ALL_TYPES = (
    KRITA,
    KRITA_ARCHIVE,
    OPEN_RASTER,
    OPEN_EXR,
    GIF,
    JPEG,
    JPEG_2,
    PNG,
    PHOTOSHOP,
    PHOTOSHOP_BIG,
    TARGA,
    TIFF,
    WEBP,
    BMP,
)
