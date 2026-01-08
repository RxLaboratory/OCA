# Roadmap

This page describes what we're currently working on or what we'd like to have in OCA one day or the other.

Features are ordered from closer and more likely to be implemented to further or optional.

!!! warning
    Everything which is described here is still subject to change before it makes its way to OCA.

## Layer transform

We'd like to add **position**, **pivot** coordinates, **rotation** and **scale** to the Layer Object.

!!! discuss
    [Join the discussion about this feature here](https://codeberg.org/OCA/OCA/issues/5).

## Thumbnails

An 8-bit sRGB PNG file could be included in the OCA format as a thumbnail for the document.

!!! discuss
    [Join the discussion about this feature here](https://codeberg.org/OCA/OCA/issues/6).

## Layer and Frame Time values

It may be useful to allow for moving and cutting the [*Layer Object*](specs/layer.md) in time. We could add `startTime` and `endTime` values to the object, same as the [*Root Object*](specs/root.md).

!!! discuss
    [Join the discussion about this feature here](https://codeberg.org/OCA/OCA/issues/7).

## Frame sequences

Instead of storing the list of all the frames, we could add a new Frame Sequence Object to be used when all the frames have the same position, size and opacity, which would describe how the frames are named, or use and `.ifl` file as source.

!!! discuss
    [Join the discussion about this feature here](https://codeberg.org/OCA/OCA/issues/8).

## Color space

It would be easy and useful to add some info about the color space. To be used at least for `F16` and `F32` color depth with *EXR* files, but we may also support *Rec-2020* with PNG files.

## OCAZ, Zipped OCA, and/or OpenDocument

For now, OCA is just a folder; it could also be a zipped archive (using only the most common compression algorithms, Store and Deflate), with the new `.ocaz` extension. Encryption, Digital signatures, and segmented/multiple volumes archives would be prohibited, following the OpenDocument format.

We could also allow for a format completely following the OpenDocument specifications, and use XML files instead of JSON.

This can be an issue though, as parsing XML in *Adobe* apps is notoriously more difficult than JSON; JSON is also easier to read and understand by humans than XML, and this is an important matter for adoption amongst the animation community where there are a lot of amateur developers. It's also an easy way for humans to understand the content of the file, or even modify it manually.

We could separate the content, styles, metadata, and application settings into four separate files like OpenDocument formats though. For now, only content (and very few metadata) is stored by OCA, but we may add more metadata and application settings too for example.  
It does make sense to store the metadata associated with specific objects next to them though; separating the metadata would concern only the general metadata, like the existing `originApp` and `originAppVersion` of the [*Root Object*](specs/root.md).

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

## Keyframe animation

When layer transform's been added, it would be nice to have the ability to add keyframes to the position, pivot, rotation, scale and opacity values.

This raises more complicated questions about interpolation and how to store this info, but we're also working on an *OKA Open Keyframe Animation* format and API which should help that!

## Loops

It would be nice to be able to extrapolate frames and transform animations, with several modes: `no`, `maintain`, `continue`, `cycle`, `pingpong`, both before and after the animation, with the ability to choose the number of keyframes or frames as the basis of the extrapolation...

This question is related to the interpolation and keyframes format, and will be handled by the *OKA Open Keyframe Animation* format we're working on.

An `inExtrapolation` and `outExtrapoplation` values (*OKAExtrapolationObject*) would be added to the hypothetical Frame Sequence Object.
