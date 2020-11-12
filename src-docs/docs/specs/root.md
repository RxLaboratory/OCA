# Root Object

Default values should be used when importing an OCA format if the data can't be read or is not available.

- `ocaVersion`: *string*, the version of OCA used in this file. Must be one of the versions listed in the [changelog](../changelog.md)
- `name`: *string*, the name of the animation
- `frameRate`: *float*, the frame rate, in frames/second. Default: `24`
- `width`: *int*, the width, in pixels. Default: `1920`
- `height`: *int*, the height, in pixels. Default: `1080`
- `startTime`: *int*, the first frame number in the animation. Default: `0`
- `endTime`: *int*, the last frame number in the animation. Default: `240`
- `colorDepth`: *string*, the colors used in the frames. See the *Color Depth* section below. Default: `U8`
- `backgroundColor`: *float[]*, the color of the background, in an [R,G,B,A] array, each value in the range [0.0 - 1.0]. Default: `[0.0, 0.0, 0.0, 0.0]`
- `layers`: *layerObject[]*, the layers used in the animation. See the *Layer Object Specs* section below
- `originApp`: *string*, the application name from which the document was exported.
- `originAppVersion`: *string*, the version of the origin application.