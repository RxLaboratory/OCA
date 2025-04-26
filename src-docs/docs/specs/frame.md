# Frame Object

Default values should be used when importing an OCA format if the data can't be read or is not available.  
If there is no default value, importing the OCA document should fail.

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`duration`** | *int* | `1` | The duration of the frame, in frames. |
| **`fileName`** | *string* | `""` | The path and name of the file of the frame. It is the relative path from the root of the *OCA* folder.<br>It can be an empty string if and only if it's a blank/empty frame (i.e. the name is `"_blank"` ). |
| **`frameNumber`** | *int* | | The frame in the document at which the frames starts to be visible. |
| **`height`** | *int* | `layer.height` | The height, in pixels. |
| **`id`** | *string* | `""` | A unique identifier. It should at least be unique in the current document, but the best is to use actual UUIDs whenever possible. |
| **`meta`** | *object* | `{}` | Any custom metadata associated to the frame. It *must* be an object, not a value or a list. |
| **`name`** | *string* | `"_blank"` | The name of the frame. It can be `"_blank"` for an empty frame. |
| **`opacity`** | *int* | `1.0` | The opacity of the frame in the range `[0.0 - 1.0]`. It *must* be multiplied by the containing layer opacity during the rendering process. |
| **`position`** | *int[]* | `[layer.width / 2, layer.height/2]` | The coordinates of the center of the frame, in pixels [X,Y] in the containing ([*Layer Object*](layer.md)) coordinates; the origin `[0,0]` is the top left corner of the containing layer. |
| **`width`** | *int* | `layer.width` | The width, in pixels. |

!!! WIP
    We're planning to add a new Frame Sequence Object to simplify storing frames when they all have the same size, position and opacity, and allow the use of `.ifl` files.

    ▹ [Roadmap](../roadmap.md)

## Examples

### Generic frame

```json
{
    "name": "Layer_name_3_00000",
    "id": "123456789",
    "fileName": "Group_name_2/Layer_name_3/Layer_name_3_00000.png",
    "frameNumber": 0,
    "opacity": 1.0,
    "position": [
        960,
        540
    ],
    "width": 1920,
    "height": 1080,
    "duration": 3,
    "meta": {}
}
```

### Empty frame

You can insert empty, blank frames using `"_blank"` as its name, and an empty filename.

```json
{
    "name": "_blank",
    "id": "123456789",
    "fileName": "",
    "frameNumber": 20,
    "opacity": 1.0,
    "position": [
        0,
        0
    ],
    "width": 0,
    "height": 0,
    "duration": 10,
    "meta": {}
}
```

## Changelog

### 1.3.0

- Added `id`
