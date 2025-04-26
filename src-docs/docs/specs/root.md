# Root (Document) Object

## Values

Default values should be used when importing an OCA document if the data can't be read or is not available.  
If there is no default value, importing the OCA document should fail.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`backgroundColor`** | *float[]* | `[0.0, 0.0, 0.0, 0.0]` | The color of the background, in an [R,G,B,A] array, each value in the range `[0.0 - 1.0]`. The values may be higher than `1.0` if and only if the color depth is `F16` or `F32`. |
| **`colorDepth`** | *string* | `U8` | The colors used in the frames. See the [*Color Depth*](color-depth.md) section. |
| **`endTime`** | *int* | `240` | The last frame number in the animation. The frame with this number is *not* part of the animation; the exact duration in frames is `endTime - startTime` |
| **`height`** | *int* | `1080` | The height, in pixels.  |
| **`frameRate`** | *float* | `24.0` | The frame rate, in frames/second. |
| **`layers`** | *LayerObject[]* | `[]` | The layers used in the animation. See the [*Layer Object*](layer.md) section.<br>Layers are stored from bottom to top, the first layer in the list is the bottom one (the background). |
| **`name`** | *string* | `"Untitled"` | The name of the animation. |
| **`ocaVersion`** | *string* | `"0.0.0"` | The version of OCA used in this file.<br>Must be one of the versions listed in the [changelog](../changelog.md). |
| **`startTime`** | *int* | `0` | The first frame number in the animation. |
| **`width`** | *int* | `1920` | The width, in pixels. |

!!! note
    If the layers don't have the same size as the document (this root object), they may be cropped, but they're never scaled.

    In the same manner, if layer durations are longer than `endTime - startTime`, or if their first frame is lower than the start time, there may be frames not visible or outside of a timeline.

## Example

```json
{
    "name": "Document_name",
    "frameRate": 24,
    "width": 1920,
    "height": 1080,
    "startTime": 0,
    "endTime": 220,
    "colorDepth": "U8",
    "backgroundColor": [
        0.9882352941176471,
        0.9137254901960784,
        0.30980392156862746,
        1.0
    ],
    "layers": [ ... ],
    "ocaVersion": "1.1.0"
}
```

## Changelog

### 1.2.0

`originApp` and `originAppVersion` are deprecated in the Document object and should now be stored in the sidecar [metadata file](meta.md).
