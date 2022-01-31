![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Layer Object

Default values should be used when importing an OCA format if the data can't be read or is not available.

- `name`: *string*, the name of the layer
- `frames`: *frameObject[]*, the frames of the layer. See the *Frame Object Specs* section below.
- `childLayers`: *layerObject[]*, the child layers if this layer is a group.
- `type`: *string*, the type of the layer. See the *Layer Types* section below. Default: `paintlayer`
- `fileType`: *string*, the type of the files used for the frames. The file extension, without the initial dot.
- `blendingMode`: *string*, the blending mode of the layer. See the *Blending modes* section below. Default: `normal`
- `inheritAlpha`: *boolean*, when true, the alpha of the layer is multiplied with the alpha of all the layers under in the same group (called *Preserve Transparency* in *Adobe After Effects*, *Inherit Alpha* in *Krita*). Default: `false`
- `animated`: *boolean*, whether this layer is a single frame or not. Default: `true`
- `position`: *int[]*, the coordinates of the center of the layer, in pixels [X,Y] in the document coordinates. Default: half the document width and half the document height
- `width`: *int*, the width, in pixels. Default: the document width
- `height`: *int*, the height, in pixels. Default: the document height
- `label`: *int*, a label for the layer. See the *Layer Label* section below. Default: `-1`
- `opacity`: *float*, the opacity of the layer in the range [0.0 - 1.0]. Default `1.0`
- `visible`: *boolean*, whether the layer is activated/visible. Default `true`
- `reference`: *boolean*, whether the layer is a guide or reference, and should not be rendered. Default `false`
- `passThrough`: *boolean*, whether the layer is in pass through mode. Only for grouplayer.

## Examples

### Generic paintlayer

This is an empty `paintlayer` (without any frame).

```json
{
    "name": "Layer_name_1",
    "frames": [ ],
    "childLayers": [ ],
    "type": "paintlayer",
    "fileType": "png",
    "blendingMode": "normal",
    "inheritAlpha": false,
    "animated": false,
    "position": [
        959,
        539
    ],
    "width": 1920,
    "height": 1080,
    "label": 0,
    "opacity": 1.0,
    "visible": true,
    "passThrough": false,
    "reference": false
}
```

### Generic grouplayer

This is an empty `grouplayer` (without any child layer).

```json
{
    "name": "Group_name_1",
    "frames": [ ],
    "childLayers": [ ],
    "type": "grouplayer",
    "fileType": "png",
    "blendingMode": "normal",
    "inheritAlpha": false,
    "animated": false,
    "position": [
        959,
        539
    ],
    "width": 1920,
    "height": 1080,
    "label": 0,
    "opacity": 1.0,
    "visible": true,
    "passThrough": true,
    "reference": false
}
```