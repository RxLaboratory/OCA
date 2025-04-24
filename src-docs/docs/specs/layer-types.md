![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Layer Types

*OCA* is able to store different types of layers. For now, three types are supported : `paintlayer`, `grouplayer`, and `vectorlayer`. We hope to be able to support other types in the future like adjustment layers (at least with the most common effects) or masks.

| OCA Identifier | Description |
|---|---|
| clonelayer | An instance of another layer |
| grouplayer | A layer without frames/images but continaing other layers |
| ocalayer | A reference to another OCA document, allows for nested documents |
| paintlayer | A bitmap containing an image |
| vectorlayer | Vectors forming an image, like an *SVG* file |

## Groups

These types may contain other layers:

- `ocalayer`
- `grouplayer`

With these types, the following attributes may be used. Read the [Layer Object reference](layer.md) for more details.

- `childLayers`
- `passThrough`

## Instances

These types are instances of other layers:

- `ocalayer`
- `clonelayer`

With these types, the `source` attribute must be set. Read the [Source Object reference](layer.md#source-object) for more details.