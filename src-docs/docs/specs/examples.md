![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Examples

## Bird

![](../img/OCA_Example_Bird.apng)  
Rendered in the *APNG* format.

This is a complete example featuring blending modes, groups, and the *passthrough* option for groups.

It was made in *Krita 5.1.1*.

There are two different versions, as the reference implementation of an [OCA exporter in Krita](http://oca-krita.rxlab.guide/index.html){target="_blank"} ([src](https://codeberg.org/RxLaboratory/OCA-Krita){target="_blank"}) has the option to either export all layers at the same size at the document (cropped if bigger, with empty space if smaller), or retain their original size (which may be bigger or smaller than the document).

▶ You can [download this example here](http://oca.rxlab.guide/downloads/), including the source *Krita* document and two OCA versions.

For both versions, the folder structure is the same:

- **Document**  
    Folder containing all the layers and frames  
    - **Bird Flying**  
    Folder containing the frames of a layer  
        - *Bird Flying_00000.png* ... *Bird Flying_00022.png*  
        The frames
    - **Cui !**  
    Folder containing the frames of a layer  
        - *Cui !_00008.png* ... *Cui !_00026.png*  
        The frames
    - **Sun**  
    Folder of a group layer
        - *Flare_00000.png*  
            A layer without animation (single frame)
        - *Sun_00000.png*  
            A layer without animation (single frame)
    - **Trees**  
    Folder of a group layer
        - *Tree 1_00000.png*  
            A layer without animation (single frame)
        - *Tree 2_00000.png*  
            A layer without animation (single frame)
        - *Tree 3_00000.png*  
            A layer without animation (single frame)
    - *Sky_00000.png*  
        A layer without animation (single frame)
- *OCA_Example_Bird.oca*  
    OCA JSON data
- *OCA_Example_Bird_meta.json*  
    JSON metadata

Here's a copy of the two versions of the OCA JSON data. We've stripped some frames from the data to make it smaller in this page.

### Full Layers

```json
{
    "name": "Document",
    "frameRate": 12,
    "width": 1280,
    "height": 720,
    "startTime": 0,
    "endTime": 33,
    "colorDepth": "U8",
    "backgroundColor": [
        0.0,
        0.0,
        0.0,
        0.0
    ],
    "layers": [
        {
            "name": "Sky",
            "frames": [
                {
                    "name": "Sky_00000",
                    "fileName": "Document/Sky_00000.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        582,
                        388
                    ],
                    "width": 2543,
                    "height": 909,
                    "duration": 33
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                582,
                388
            ],
            "width": 2543,
            "height": 909,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Trees",
            "frames": [],
            "childLayers": [
                {
                    "name": "Tree 3",
                    "frames": [
                        {
                            "name": "Tree 3_00000",
                            "fileName": "Document\\Trees/Tree 3_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.45098039215686275,
                            "position": [
                                720,
                                677
                            ],
                            "width": 471,
                            "height": 617,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        720,
                        677
                    ],
                    "width": 471,
                    "height": 617,
                    "label": 0,
                    "opacity": 0.45098039215686275,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Tree  2",
                    "frames": [
                        {
                            "name": "Tree  2_00000",
                            "fileName": "Document\\Trees/Tree  2_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.7607843137254902,
                            "position": [
                                275,
                                599
                            ],
                            "width": 471,
                            "height": 617,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        275,
                        599
                    ],
                    "width": 471,
                    "height": 617,
                    "label": 0,
                    "opacity": 0.7607843137254902,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Tree 1",
                    "frames": [
                        {
                            "name": "Tree 1_00000",
                            "fileName": "Document\\Trees/Tree 1_00000.png",
                            "frameNumber": 0,
                            "opacity": 1.0,
                            "position": [
                                928,
                                510
                            ],
                            "width": 471,
                            "height": 617,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        928,
                        510
                    ],
                    "width": 471,
                    "height": 617,
                    "label": 0,
                    "opacity": 1.0,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                }
            ],
            "type": "grouplayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Bird Flying",
            "frames": [
                {
                    "name": "Bird Flying_00000",
                    "fileName": "Document/Bird Flying/Bird Flying_00000.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        99,
                        488
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00001",
                    "fileName": "Document/Bird Flying/Bird Flying_00001.png",
                    "frameNumber": 1,
                    "opacity": 1.0,
                    "position": [
                        144,
                        453
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "_blank",
                    "fileName": "",
                    "frameNumber": 23,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 10
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": true,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Cui !",
            "frames": [
                {
                    "name": "_blank",
                    "fileName": "",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 8
                },
                {
                    "name": "Cui !_00008",
                    "fileName": "Document/Cui !/Cui !_00008.png",
                    "frameNumber": 8,
                    "opacity": 1.0,
                    "position": [
                        479,
                        302
                    ],
                    "width": 30,
                    "height": 39,
                    "duration": 1
                },
                {
                    "name": "Cui !_00009",
                    "fileName": "Document/Cui !/Cui !_00009.png",
                    "frameNumber": 9,
                    "opacity": 1.0,
                    "position": [
                        498,
                        297
                    ],
                    "width": 68,
                    "height": 48,
                    "duration": 1
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "dodge",
            "animated": true,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Sun",
            "frames": [],
            "childLayers": [
                {
                    "name": "Sun",
                    "frames": [
                        {
                            "name": "Sun_00000",
                            "fileName": "Document\\Sun/Sun_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.611764705882353,
                            "position": [
                                152,
                                111
                            ],
                            "width": 257,
                            "height": 247,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        152,
                        111
                    ],
                    "width": 257,
                    "height": 247,
                    "label": 0,
                    "opacity": 0.611764705882353,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Flare",
                    "frames": [
                        {
                            "name": "Flare_00000",
                            "fileName": "Document\\Sun/Flare_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.7098039215686275,
                            "position": [
                                639,
                                359
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "add",
                    "animated": false,
                    "position": [
                        639,
                        359
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 0.7098039215686275,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                }
            ],
            "type": "grouplayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": true,
            "reference": false,
            "inheritAlpha": false
        }
    ],
    "ocaVersion": "1.2.0"
}
```

### Cropped Layers

```json
{
    "name": "Document",
    "frameRate": 12,
    "width": 1280,
    "height": 720,
    "startTime": 0,
    "endTime": 33,
    "colorDepth": "U8",
    "backgroundColor": [
        0.0,
        0.0,
        0.0,
        0.0
    ],
    "layers": [
        {
            "name": "Sky",
            "frames": [
                {
                    "name": "Sky_00000",
                    "fileName": "Document/Sky_00000.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 33
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Trees",
            "frames": [],
            "childLayers": [
                {
                    "name": "Tree 3",
                    "frames": [
                        {
                            "name": "Tree 3_00000",
                            "fileName": "Document\\Trees/Tree 3_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.45098039215686275,
                            "position": [
                                640.0,
                                360.0
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 0.45098039215686275,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Tree  2",
                    "frames": [
                        {
                            "name": "Tree  2_00000",
                            "fileName": "Document\\Trees/Tree  2_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.7607843137254902,
                            "position": [
                                640.0,
                                360.0
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 0.7607843137254902,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Tree 1",
                    "frames": [
                        {
                            "name": "Tree 1_00000",
                            "fileName": "Document\\Trees/Tree 1_00000.png",
                            "frameNumber": 0,
                            "opacity": 1.0,
                            "position": [
                                640.0,
                                360.0
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 1.0,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                }
            ],
            "type": "grouplayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Bird Flying",
            "frames": [
                {
                    "name": "Bird Flying_00000",
                    "fileName": "Document/Bird Flying/Bird Flying_00000.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00001",
                    "fileName": "Document/Bird Flying/Bird Flying_00001.png",
                    "frameNumber": 1,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 1
                },
                {
                    "name": "_blank",
                    "fileName": "",
                    "frameNumber": 23,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 10
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": true,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Cui !",
            "frames": [
                {
                    "name": "_blank",
                    "fileName": "",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 8
                },
                {
                    "name": "Cui !_00008",
                    "fileName": "Document/Cui !/Cui !_00008.png",
                    "frameNumber": 8,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 1
                },
                {
                    "name": "Cui !_00009",
                    "fileName": "Document/Cui !/Cui !_00009.png",
                    "frameNumber": 9,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 1
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "dodge",
            "animated": true,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false,
            "inheritAlpha": false
        },
        {
            "name": "Sun",
            "frames": [],
            "childLayers": [
                {
                    "name": "Sun",
                    "frames": [
                        {
                            "name": "Sun_00000",
                            "fileName": "Document\\Sun/Sun_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.611764705882353,
                            "position": [
                                640.0,
                                360.0
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": false,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 0.611764705882353,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                },
                {
                    "name": "Flare",
                    "frames": [
                        {
                            "name": "Flare_00000",
                            "fileName": "Document\\Sun/Flare_00000.png",
                            "frameNumber": 0,
                            "opacity": 0.7098039215686275,
                            "position": [
                                640.0,
                                360.0
                            ],
                            "width": 1280,
                            "height": 720,
                            "duration": 33
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "add",
                    "animated": false,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "label": 0,
                    "opacity": 0.7098039215686275,
                    "visible": true,
                    "passThrough": false,
                    "reference": false,
                    "inheritAlpha": false
                }
            ],
            "type": "grouplayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                640.0,
                360.0
            ],
            "width": 1280,
            "height": 720,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": true,
            "reference": false,
            "inheritAlpha": false
        }
    ],
    "ocaVersion": "1.2.0"
}
```