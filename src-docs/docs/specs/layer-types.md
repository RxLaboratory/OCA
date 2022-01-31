![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Layer Types

*OCA* is able to store different types of layers. For now, three types are supported : `paintlayer`, `grouplayer`, and `vectorlayer`. We hope to be able to support other types in the future like adjustment layers (at least with the most common effects) or masks.

| OCA Identifier | Description |
|---|---|
| paintlayer | A bitmap containing an image |
| vectorlayer | Vectors forming an image, like an *SVG* file |
| grouplayer | A layer without frames/images but continaing other layers |