# Layer Object

Default values should be used when importing an OCA format if the data can't be read or is not available.  
If there is no default value, importing the OCA document should fail.


| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`name`** | *string* | | The name of the layer. It *must* be unique in the document. |
| **`frames`** | *FrameObject[]* | `[]` | The frames of the layer if it is a `paintlayer` or a `vectorlayer`, ignored otherwise. See the [*Frame Object*](frame.md) section. |
| **`childLayers`** | *LayerObject[]* | `[]` | The child layers if this layer is a `grouplayer`. |
| **`type`** | *string* | `"paintlayer"` | The type of the layer. See the [*Layer Types*](layer-types.md) section. |
| **`fileType`** | *string* | `"png"` | The type of the files used for the frames. The file extension, without the initial dot. |
| **`blendingMode`** | *string* | `"normal"` | The blending mode of the layer. See the [*Blending modes*](blending-modes.md) section. |
| **`inheritAlpha`** | *boolean* | `false` | When true, the alpha of the layer is multiplied with the alpha of all the layers under it (before it in an OCA list) in the same group (called *Preserve Transparency* in *Adobe After Effects*, *Inherit Alpha* in *Krita*).  |
| **`animated`** | *boolean* | `true` | Whether this layer is a single frame or not. |
| **`position`** | *int[]* | `[root.width / 2, root.height/2]`<br>or<br>`[layer.width / 2, layer.height/2]` | The coordinates of the center of the layer, in pixels [X,Y] in the document ([*Root Object*](root.md)) or the containing group ([*Layer Object*](layer.md)) coordinates; the origin `[0,0]` is the top left corner of the container. |
| **`width`** | *int* | `root.width` | The width, in pixels. |
| **`height`** | *int* | `root.height` | The height, in pixels. |
| **`label`** | *int* | `-1` | A label for the layer. See the [*Layer Label*](layer-labels.md) section. |
| **`opacity`** | *float* | `1.0` | The opacity of the layer in the range [0.0 - 1.0]. |
| **`visible`** | *boolean* | `true` | Whether the layer is activated/visible. |
| **`reference`** | *boolean* | `false` | Whether the layer is a guide or reference, and should not be rendered. |
| **`passThrough`** | *boolean* | `false` | Only for `grouplayer`. When this is `false`, the group content *must* be merged (using alpha, opacity values, blending modes, etc.) before the rendering process goes to the next node/layer, and cropped if the contained layers are bigger than the group size. When this is `true`, the group is to be completely by the rendering process, and only used as a way to group the layers in the UI of the application. |

!!! note
    If the frames don't have the same size as the layer, they may be cropped, but they're never scaled.

!!! WIP
    We're planning to add a new `ocalayer` layer type to allow for nested OCA documents.

    ▹ [Roadmap](../roadmap.md)

!!! WIP
    We're planning to add full layer transform to OCA, with pivot, scale and rotation.

    ▹ [Roadmap](../roadmap.md)

!!! WIP
    When layer transform’s been added, it would be nice to have the ability to add keyframes to the position, pivot, rotation, scale and opacity values.

    ▹ [Roadmap](../roadmap.md)

!!! WIP
    It would be nice to be able to extrapolate frames and transform animations, with several modes: `no`, `constant`, `continue`, `cycle`, `offset`, `pingpong`.

    ▹ [Roadmap](../roadmap.md)

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