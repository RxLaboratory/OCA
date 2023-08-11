# Opacity, Colors and Color Depth

## Color Depth

Color depths for the document are stored as a string. *OCA* uses the same values as *Krita*. This table shows the possible values:

| OCA Identifier | Description |
|---|---|
| U8 | unsigned 8-bit integer, the most common type |
| U16 | unsigned 16-bit integer |
| F16 | half, 16-bit floating point |
| F32 | 32-bit floating point |

## Colors

All colors are stored as an [R,G,B,A] float array. Channel values are in the range `[0.0 - 1.0]` except Red, Green and Blue channels for `F16` and `F32` depths only where they can be higher than `1.0`.

## Opacity

Opacities (and Alpha channels) are stored as a float value, in the range `[0.0 - 1.0]`.