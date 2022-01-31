![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Frame Object

Default values should be used when importing an OCA format if the data can't be read or is not available.

- `name`: *string*, the name of the frame.  
    It can be `"_blank"` for an empty frame.
- `fileName`: *string*, the path and name of the file of the frame. It is the absolute path from the root of the *OCA* folder. Default: a file named `layer_name/frame_name.fileType`.  
    It can be an empty string if there's no actual frame (i.e. a blank/empty frame).
- `frameNumber`: *int*, the frame in the document at which the frames starts to be visible
- `opacity`: *float*, the opacity of the keyframe in the range [0.0 - 1.0]. Default `1.0`
- `position`: *int[]*, the coordinates of the center of the keyframe, in pixels [X,Y] in the document coordinates. Default: half the document width and half the document height
- `width`: *int*, the width, in pixels. Default: the layer width
- `height`: *int*, the height, in pixels. Default: the layer height
- `duration`: *int*, the duration of the frame, in frames. Default: `1`

## Examples

### Generic frame

```json
{
    "name": "Layer_name_3_00000",
    "fileName": "Document_name.oca/Group_name_2/Layer_name_3/Layer_name_3_00000.png",
    "frameNumber": 0,
    "opacity": 1.0,
    "position": [
        960,
        540
    ],
    "width": 1920,
    "height": 1080,
    "duration": 3
}
```

### Empty frame

You can insert empty, blank frames using `"_blank"` as its name, and an empty filename.

```json
{
    "name": "_blank",
    "fileName": "",
    "frameNumber": 20,
    "opacity": 1.0,
    "position": [
        0,
        0
    ],
    "width": 0,
    "height": 0,
    "duration": 10
}
```