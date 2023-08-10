# Roadmap

This page describes what we're currently working on or what we'd like to have in OCA one day or the other.

Features are ordered from closer and more likely to be implemented to further or optional.

!!! warning
    Everything which is described here is still subject to change before it makes its way to OCA.

## Layer type: ocalayer

We're going to add a new `ocalayer` [layer type](specs/layer-types.md). This is a way to nest a complete OCA document into another one, as a layer. It would be similar to a `grouplayer`.

A new attribute would be added to the [Layer Object](specs/layer.md):

- `ocaSource`: *ocaSourceObject*, the object describing how the other OCA document is included.

### OCA Source Object

The new OCA Source Object would have these attributes:

- `sourceFile`: *string*, the relative file path to the OCA JSON file.
- `timeOffset`: *int*, the frame number at which the other OCA document is inserted.

### Notes

Some attributes in the Root Object of the nested OCA document are to be ignored and replaced by the values of the current document:

- `frameRate`, `colorDepth`, `backgroundColor` are completely ignored.
- `width` and `height` should be the same as of the `ocalayer` representing the nested document. If they're different, they're to be ignored and replaced by those of the `ocalayer`.
- `startTime` and `endTime` are added the `timeOffset` value of the OCA Source Object.

## Frame sequences

Instead of storing the list of all the frames, we could add a new Frame Sequence Object to be used when all the frames have the same position, size and opacity, which would describe how the frames are named, or use and `.ifl` file as source.

## Layer transform

We'd like to add position, pivot coordinates, rotation and scale to the Layer Object.

## Keyframe animation

When layer transform's been added, it would be nice to have the ability to add keyframes to the position, pivot, rotation, scale and opacity values.

This raises more complicated questions about interpolation and how to store this info, but we're also working on an *OKA Open Keyframe Animation* format and API which should help that!

## Loops

It would be nice to be able to extrapolate frames and transform animations, with several modes: `no`, `maintain`, `continue`, `cycle`, `pingpong`, both before and after the animation, with the ability to choose the number of keyframes or frames as the basis of the extrapolation...

This question is related to the interpolation and keyframes format.
