# Frame Object

Default values should be used when importing an OCA format if the data can't be read or is not available.

- `name`: *string*, the name of the frame
- `fileName`: *string*, the path and name of the file of the frame. It is the absolute path from the root of the *OCA* folder. Default: a file named `layer_name/frame_name.fileType`
- `frameNumber`: *int*, the frame in the document at which the frames starts to be visible
- `opacity`: *float*, the opacity of the keyframe in the range [0.0 - 1.0]. Default `1.0`
- `position`: *int[]*, the coordinates of the center of the keyframe, in pixels [X,Y] in the document coordinates. Default: half the document width and half the document height
- `width`: *int*, the width, in pixels. Default: the layer width
- `height`: *int*, the height, in pixels. Default: the layer height
- `duration`: *int*, the duration of the frame, in frames. Default: `1`