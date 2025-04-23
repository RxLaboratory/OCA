# Layer Object

Default values should be used when importing an OCA format if the data can't be read or is not available.  
If there is no default value, importing the OCA document should fail.


| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`animated`** | *boolean* | `true` | Whether this layer is a single frame or not. |
| **`blendingMode`** | *string* | `"normal"` | The blending mode of the layer. See the [*Blending modes*](blending-modes.md) section. |
| **`childLayers`** | *LayerObject[]* | `[]` | The child layers if this layer is a `grouplayer`. |
| **`fileType`** | *string* | `"png"` | The type of the files used for the frames. The file extension, without the initial dot. |
| **`frames`** | *FrameObject[]* | `[]` | The frames of the layer if it is a `paintlayer` or a `vectorlayer`, ignored otherwise. See the [*Frame Object*](frame.md) section. |
| **`height`** | *int* | `root.height` | The height, in pixels. |
| **`id`** | *string* | `""` | A unique identifier. It should at least be unique in the current document, but the best is to use actual UUIDs whenever possible. |
| **`inheritAlpha`** | *boolean* | `false` | When true, the alpha of the layer is multiplied with the alpha of all the layers under it (before it in an OCA list) in the same group (called *Preserve Transparency* in *Adobe After Effects*, *Inherit Alpha* in *Krita*).  |
| **`label`** | *int* | `-1` | A label for the layer. See the [*Layer Label*](layer-labels.md) section. |
| **`meta`** | *object* | `{}` | Any custom metadata associated to the layer. It *must* be an object, not a value or a list. |
| **`name`** | *string* | | The name of the layer. It *must* be unique in the document. |
| **`opacity`** | *float* | `1.0` | The opacity of the layer in the range [0.0 - 1.0]. |
| **`passThrough`** | *boolean* | `false` | Only for `grouplayer`. When this is `false`, the group content *must* be merged (using alpha, opacity values, blending modes, etc.) before the rendering process goes to the next node/layer, and cropped if the contained layers are bigger than the group size. When this is `true`, the group is to be completely by the rendering process, and only used as a way to group the layers in the UI of the application. |
| **`position`** | *int[]* | `[root.width / 2, root.height/2]`<br>or<br>`[layer.width / 2, layer.height/2]` | The coordinates of the center of the layer, in pixels [X,Y] in the document ([*Root Object*](root.md)) or the containing group ([*Layer Object*](layer.md)) coordinates; the origin `[0,0]` is the top left corner of the container. |
| **`reference`** | *boolean* | `false` | Whether the layer is a guide or reference, and should not be rendered. |
| **`source`** | *SourceObject* | `{}` | If the type is `ocalayer` or `clonelayer`, this object contains the source info. |
| **`type`** | *string* | `"paintlayer"` | The type of the layer. See the [*Layer Types*](layer-types.md) section. |
| **`visible`** | *boolean* | `true` | Whether the layer is activated/visible. |
| **`width`** | *int* | `root.width` | The width, in pixels. |

!!! note
    If the frames don't have the same size as the layer, they may be cropped, but they're never scaled.

!!! WIP
    We're planning to add full layer transform to OCA, with pivot, scale and rotation.

    ▹ [Roadmap](../roadmap.md)

!!! WIP
    When layer transform’s been added, it would be nice to have the ability to add keyframes to the position, pivot, rotation, scale and opacity values.

    ▹ [Roadmap](../roadmap.md)

!!! WIP
    It would be nice to be able to extrapolate frames and transform animations, with several modes: `no`, `constant`, `continue`, `cycle`, `offset`, `pingpong`.

    ▹ [Roadmap](../roadmap.md)

## Source Object

This object describes the source of `ocalayer` (another OCA document) and `clonelayer` (another Layer Object).

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`absFileName`** | *string* | `""` | The *absolute* path and name of the OCA file if the layer is an `ocalayer`. It is the absolute path at time of the export.<br>It is an empty string if the layer is a `clonelayer`. |
| **`id`** | *string* | `""` | The ID of the referenced layer. It is mandatory for `clonelayer` but may be an empty string for `ocalayer`, it which case the whole document should be used. |
| **`relFileName`** | *string* | `""` | The *relative* path and name of the OCA file if the layer is an `ocalayer`. It is the relative path from the root of the *OCA* folder.<br>It is an empty string if the layer is a `clonelayer`. |

!!! note
    For `ocalayer`, both a relative and an absolute path are saved; when loading the document, the absolute path should be preferred, and the relative path should be used if the file is not found. If the source is not found at both paths, a placeholder should be used and the user should be warned, or an interactive prompt should let the user pick the file or cancel the process.

!!! note
    With `ocalayer`, some attributes in the Root Object of the nested OCA document are to be ignored and replaced by the values of the current document:

    - `frameRate`, `colorDepth`, `backgroundColor` are completely ignored.
    - `width` and `height` should be the same as of the `ocalayer` representing the nested document. If they're different, they're to be ignored and replaced by those of the `ocalayer`.
    - `startTime` and `endTime` are added the `timeOffset` value of the OCA Source Object.

!!! note
    With `clonelayer`, some attributes of the cloned layers should be empty, as they're replaced by the values of the source layer: `frames`, `animated`, `childLayers`, `fileType`, `width`, `height`

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
    "reference": false,
    "meta": {}
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
    "reference": false,
    "meta": {}
}
```