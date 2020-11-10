# OCA

Open Cel Animation format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

## Principles

- *OCA* has to be open and simple: it must be easy to implement an exporter or importer in any application providing a scripting API.

- As it relies on existing and standard file formats (images and json/text files) stored in a simple folder, the *OCA* format can be imported in any application manually, even if the application does not directly support it.

- *OCA* stores the most common features used by drawing/animation software: layers, groups, blending modes, animation exposure (x-sheet), etc.

## Implementation

We're providing a few implementations of *OCA* as add-ons for a few applications. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

Note that the *OCA* format is made to be simple to export/import in any application and it should not be difficult to implement it/write your own script for your application.

| Application | Add-on name | Exporter | Importer | Comments |
|---|---|---|---|---|
| [Krita](http://krita.org) | [OCA for Krita](https://github.com/Rainbox-dev/DuKRIF_OCA) | :large_blue_circle: | :large_orange_diamond: | |
| Adobe Photoshop | OCA for Photoshop | :large_orange_diamond: | :red_circle: | |
| TVPaint | OCA for TVPaint | :large_orange_diamond: | :red_circle: | |
| Adobe After Effects | [DuIO](https://github.com/Rainbox-dev/DuAEF_DuIO) | :red_circle: | :large_blue_circle: | |
| [Blender](http://blender.org) | OCA for Blender | :red_circle: | :large_orange_diamond: | |

Legend:  
:heavy_check_mark: | Available  
:large_blue_circle: | In development  
:large_orange_diamond: | Planned  
:red_circle: | Not supported  

## Specifications and features

- Layers
- Layer groups
- Layer labels
- Layer visibility
- Keyframes / Animation exposure
- Blending Modes
- Layer sizes and coordinates
- Opacity and opacity keyframes
- Document background color
- Document color depth
- Document resolution
- Duration
- Framerate

All these properties are stored in a simple *JSON* file, and the images are stored in standard image file formats: *PNG*, *EXR*, *SVG*...

Everything is assembled in a folder which name ends with `.oca`. The *JSON* file is at the root, while the images are stored in subfolders corresponding to layers and groups.

### Folder Structure

```
|v Document_name.oca
 |- Document_name.oca
 |v Layer_name_1
  |- Layer_name_1_00000.png
  |- Layer_name_1_00110.png
  |- Layer_name_1_00112.png
  |- Layer_name_1_00114.png
  |- Layer_name_1_00200.png
 |v Group_name_2
  |v Layer_name_3
   |- Layer_name_3_00000.png
   |- Layer_name_3_00003.png
  |> Layer_name_4
  |> Layer_name_5
 |> Group_name_6
 ```

Note that the `.oca` file at the root could also use the extension `.json`

### JSON Specs

Default values should be used when importing an OCA format if the data can't be read or is not available.

#### Root Object Specs

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

#### Layer Object Specs

- `name`: *string*, the name of the layer
- `frames`: *frameObject[]*, the frames of the layer. See the *Frame Object Specs* section below.
- `childLayers`: *layerObject[]*, the child layers if this layer is a group.
- `type`: *string*, the type of the layer. See the *Layer Types* section below. Default: `paintlayer`
- `fileType`: *string*, the type of the files used for the frames. The file extension, without the initial dot.
- `blendingMode`: *string*, the blending mode of the layer. See the *Blending modes* section below. Default: `normal`
- `animated`: *boolean*, whether this layer is a single frame or not. Default: `true`
- `position`: *int[]*, the coordinates of the center of the layer, in pixels [X,Y] in the document coordinates. Default: half the document width and half the document height
- `width`: *int*, the width, in pixels. Default: the document width
- `height`: *int*, the height, in pixels. Default: the document height
- `label`: *int*, a label for the layer. See the *Layer Label* section below. Default: `-1`
- `opacity`: *float*, the opacity of the layer in the range [0.0 - 1.0]. Default `1.0`
- `visible`: *boolean*, whether the layer is activated/visible. Default `true`
- `reference`: *boolean*, whether the layer is a guide or reference, and should not be rendered. Default `false`
- `passThrough`: *boolean*, whether the layer is in pass through mode. Only for grouplayer.

#### Frame object Specs

- `name`: *string*, the name of the frame
- `fileName`: *string*, the path and name of the file of the frame. It is the absolute path from the root of the *OCA* folder. Default: a file named `layer_name/frame_name.fileType`
- `frameNumber`: *int*, the frame in the document at which the frames starts to be visible
- `opacity`: *float*, the opacity of the keyframe in the range [0.0 - 1.0]. Default `1.0`
- `position`: *int[]*, the coordinates of the center of the keyframe, in pixels [X,Y] in the document coordinates. Default: half the document width and half the document height
- `width`: *int*, the width, in pixels. Default: the layer width
- `height`: *int*, the height, in pixels. Default: the layer height
- `duration`: *int*, the duration of the frame, in frames. Default: `1`

### Durations

As *OCA* is made for traditionnal animation, **all durations are stored in _frames_**, not in seconds, and it also stores the framerate.

The first frame of an animation is the frame numbered ***0 (zero)*** by default.

### Color Depth

Color depths for the document are stored as a string. *OCA* uses the same values as *Krita*. This table shows the possible values:

| OCA Identifier | Description |
|---|---|
| U8 | unsigned 8 bits integer, the most common type |
| U16 | unsigned 16 bits integer |
| F16 | half, 16 bits floating point |
| F32 | 32 bits floating point |

### Layer Types

*OCA* is able to store different types of layers. For now, three types are supported : `paintlayer`, `grouplayer`, and `vectorlayer`. We hope to be able to support other types in the future like adjustment layers (at least with the most common effects) or masks.

| OCA Identifier | Description |
|---|---|
| paintlayer | A bitmap containing an image |
| vectorlayer | Vectors forming an image, like an *SVG* file |
| grouplayer | A layer without frames/images but continaing other layers |

### Blending modes

[Blending modes](https://github.com/Rainbox-dev/OCA/blob/master/blending-modes.md) are named after the ones used in [*Krita*](http://krita.org).

Depending on the application, a blending mode with the same name may have different results. When a blending mode is set in *OCA*, its result should be the same as the blending mode with the same name in *Krita*. This choice was made because *Krita* is a free and open source software, so anyone can have a look at how these blending modes are implemented, to be sure about what they do, and because *Krita* uses one of the biggest list of blending modes.

To know the correspondance of the blending mode names and implementations between *Krita/OCA* and the most common other applciations, we're building [correspondance tables](https://github.com/Rainbox-dev/OCA/blob/master/blending-modes.md).

### Layer Labels

Most drawing and animation applications are able to label the layers. These labels are often just different colors to display the layers and used to differentiate them. *OCA* stores a simple number to identify these labels. If this number is less than 0, it means the layer is not labelled.
