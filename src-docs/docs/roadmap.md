# Roadmap

This page describes what we're currently working on or what we'd like to have in OCA one day or the other.

Features are ordered from closer and more likely to be implemented to further or optional.

!!! warning
    Everything which is described here is still subject to change before it makes its way to OCA.

## Thumbnails

An 8-bit sRGB PNG file could be included in the OCA format as a thumbnail for the document.

A new `thumbnail` attribute would be added to the [*Root Object*](specs/root.md).

It would be a new *Thumbnail Object* with:


| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`fileName`** | *string* | | The relative path to the thumbnail (which should be at the root of the folder and named after the OCA file). |
| **`width`** | *int* | `256`? `512`? `640`? | The width. |
| **`height`** | *int* | `256`? `512`? `360`? | The width. |


!!! question
    What should be the aspect ratio and default resolution of the thumbnail?  
    Proposed default sizes:

    - `256x256` or `512x512`, 1:1
    - `640x360`, 1.78:1

!!! question
    How useful would it be to add thumbnails to layers?

## Color space

It would be easy and useful to add some info about the color space. To be used at least for `F16` and `F32` color depth with *EXR* files, but we may also support *Rec-2020* with PNG files.

## OCAZ, Zipped OCA, and/or OpenDocument

For now, OCA is just a folder; it could also be a zipped archive (using only the most common compression algorithms, Store and Deflate), with the new `.ocaz` extension. Encryption, Digital signatures, and segmented/multiple volumes archives would be prohibited, following the OpenDocument format.

We could also allow for a format completely following the OpenDocument specifications, and use XML files instead of JSON.

This can be an issue though, as parsing XML in *Adobe* apps is notoriously more difficult than JSON; JSON is also easier to read and understand by humans than XML, and this is an important matter for adoption amongst the animation community where there are a lot of amateur developers. It's also an easy way for humans to understand the content of the file, or even modify it manually.

We could separate the content, styles, metadata, and application settings into four separate files like OpenDocument formats though. For now, only content (and very few metadata) is stored by OCA, but we may add more metadata and application settings too for example.  
It does make sense to store the metadata associated with specific objects next to them though; separating the metadata would concern only the general metadata, like the existing `originApp` and `originAppVersion` of the [*Root Object*](specs/root.md).

## Layer and Frame Time values

It may be useful to allow for moving and cutting the [*Layer Object*](specs/layer.md) in time. We could add `startTime` and `endTime` values to the object, same as the [*Root Object*](specs/root.md).

!!! question
    Does it make sense for the [*Frame Object*](specs/frame.md) to use `frameNumber` and `duration` instead of `startTime` and `endTime` like the [*Root Object*](specs/root.md)?

    `frameNumber` makes it explicit it's the number used in the filename too. `duration` makes more sense when moving the frame in time, and just changing the `frameNumber` or `startTime`.

    Maybe the layer should use `startTime` and `duration`? (see below)

!!! question
    Are times relative to the container or absolute?

    They should probably be relative to make it easier to move a whole layer in time. The `duration` of the frames is less ambiguous than `endTime` and makes it easier to offset objects in time.

## Frame sequences

Instead of storing the list of all the frames, we could add a new Frame Sequence Object to be used when all the frames have the same position, size and opacity, which would describe how the frames are named, or use and `.ifl` file as source.

It would make the file smaller and easier/quicker to read (both for humans and APIs), in the case where all frames have the same size, position and opacity.

A new attribute would be added to the [Layer Object](specs/layer.md):

- `frameSequence`: *FrameSequenceObject*, the frame sequence. Default: `null`.

It would replace the `frames`  attribute of the [Layer Object](specs/layer.md), kept for backward compatibility, which would be ignored if the `frameSequence` is set.

### New Frame Sequence Object

The Frame Sequence Object would look like this:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`name`** | *string* | | The name of the frame sequence, which is the base name for all frames. |
| **`frameNameSchema`** | *string* | `"[name]_[#####].[ext]"` | How the frames are named, using these tokens:<br><ul><li>`[name]`: the sequence name.</li><li>`[#####]`: the frame number. The number of `#` gives the number of digits.</li><li>`[ext]`: the file extension, given by the `fileType` attribute of the containing [*Layer Object*](specs/layer.md).</li></ul> |
| **`frames`** | *string* or *FrameObject[]* | | One of:<br><ul><li>The path to the folder where the frames are stored, relative to the root of the *OCA* folder.</li><li>The path to an `.ifl` (Image File List)<sup>\*</sup> file, relative to the root of the *OCA* folder.</li><li>A list of [Frame Object](specs/frame.md).</li></ul> |
| **`position`** | *int[]* | `[layer.width / 2, layer.height/2]` | The coordinates of the center of the frame, in pixels [X,Y] in the containing ([*Layer Object*](specs/layer.md)) coordinates; the origin `[0,0]` is the top left corner of the containing layer. |
| **`opacity`** | *int* | `1.0` | The opacity of the frame sequence in the range `[0.0 - 1.0]`. It *must* be multiplied by the containing layer opacity during the rendering process. |
| **`width`** | *int* | `layer.width` | The width, in pixels. |
| **`height`** | *int* | `layer.height` | The height, in pixels. |
| **`duration`** | *int* | `10` | The duration of the frame sequence, in frames. |

<sup>\*</sup> An [IFL (Image File List)](https://help.autodesk.com/view/3DSMAX/2023/ENU/?guid=GUID-CA63616D-9E87-42FC-8E84-D67E1990EE71) file is a text file used by *Autodesk 3DS Max* that constructs an animation by listing single-frame bitmap files to be used for each rendered frame.

The `.ifl` file lists the bitmap files to be used with each frame. You can append an optional numeric argument to each file name to specify the number of frames of rendered animation on which it is used. For example: 

```
; Anything after a semicolon is a comment, and is ignored.
sand.png 20
pebble.png 40
stone.png 20
_blank 10
boulder.png 20
```

The bitmap files must be in the same folder as the `.ifl` file.

In addition to the specifications set by *Autodesk*, `.ifl` files used by OCA can include frames named `_blank`.

The advantage of the IFL file is that you can ignore the `frameNameSchema` to sequence any bitmap file, and set a specific duration for each frame.

If the duration of the frame is not defined (if you don't use an `.ifl` file, or if the duration is not set in the `.ifl` file), each frame lasts until the next frame (or the duration of the sequence if it's the last frame).

## Masks

Masks (and selections) could be stored as grayscale bitmaps, and associated to other layers. They could even be animated too.

That would be a new layer type, `masklayer`, and the [Layer Object](specs/layer.md) would get two new attributes: `mask` and `selection`, both represented by a masklayer.

## Adjustment/Effects Layers

Adjustment layers (layers with effects changing all layers under them in the stack) could be a new layer type, `adjustmentlayer`.

The [Layer Object](specs/layer.md) would have a new attribute: `effects`, an array of *EffectObject*.

The new Effect Object would store the effect data, which would look like this:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`name`** | *string* | `"untitled"` | The name of the effect. |
| **`type`** | *string* | | The effect. |
| **`settings`** | *object* | | The settings of the effect, which depend on the effect itself. |

We'd officially support only the most common effects, to ensure compatibility and simplicity across applications, but custom implementations could add their own effects.

This is a possible list of effects which could be officially supported:  
levels, curve, hsv, contrast, exposure, invert, balance, posterize, gaussianblur, directionalblur, radialblur, gradientmap, 2dlut, 3dlut

Effect settings could be animated (see below)

## Layer transform

We'd like to add position, pivot coordinates, rotation and scale to the Layer Object.

## Keyframe animation

When layer transform's been added, it would be nice to have the ability to add keyframes to the position, pivot, rotation, scale and opacity values.

This raises more complicated questions about interpolation and how to store this info, but we're also working on an *OKA Open Keyframe Animation* format and API which should help that!

## Loops

It would be nice to be able to extrapolate frames and transform animations, with several modes: `no`, `maintain`, `continue`, `cycle`, `pingpong`, both before and after the animation, with the ability to choose the number of keyframes or frames as the basis of the extrapolation...

This question is related to the interpolation and keyframes format, and will be handled by the *OKA Open Keyframe Animation* format we're working on.

An `inExtrapolation` and `outExtrapoplation` values (*OKAExtrapolationObject*) would be added to the hypothetical Frame Sequence Object.
