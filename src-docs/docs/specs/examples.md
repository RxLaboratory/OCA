![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Examples

## Bird

![](../img/OCA_Example_Bird.apng)  
Rendered in the *APNG* format.

This is a complete example featuring blending modes, groups, and the *passthrough* option for groups.

It was made in *Krita 5.1.1*.

There are two different versions, as the reference implementation of an OCA exporter in Krita has the option to either export all layers at the same size at the document (cropped if bigger, with empty space if smaller), or retain their original size (which may be bigger or smaller than the document).

▶ You can [download this example here](http://oca.rxlab.guide/downloads/OCA_Example_Bird.zip), including the source *Krita* document and two OCA versions.

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

Here's a copy of the two versions of the OCA JSON data.

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
                    "name": "Bird Flying_00002",
                    "fileName": "Document/Bird Flying/Bird Flying_00002.png",
                    "frameNumber": 2,
                    "opacity": 1.0,
                    "position": [
                        177,
                        429
                    ],
                    "width": 145,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00003",
                    "fileName": "Document/Bird Flying/Bird Flying_00003.png",
                    "frameNumber": 3,
                    "opacity": 1.0,
                    "position": [
                        198,
                        413
                    ],
                    "width": 151,
                    "height": 38,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00004",
                    "fileName": "Document/Bird Flying/Bird Flying_00004.png",
                    "frameNumber": 4,
                    "opacity": 1.0,
                    "position": [
                        207,
                        403
                    ],
                    "width": 149,
                    "height": 43,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00005",
                    "fileName": "Document/Bird Flying/Bird Flying_00005.png",
                    "frameNumber": 5,
                    "opacity": 1.0,
                    "position": [
                        216,
                        393
                    ],
                    "width": 148,
                    "height": 20,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00006",
                    "fileName": "Document/Bird Flying/Bird Flying_00006.png",
                    "frameNumber": 6,
                    "opacity": 1.0,
                    "position": [
                        247,
                        370
                    ],
                    "width": 135,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00007",
                    "fileName": "Document/Bird Flying/Bird Flying_00007.png",
                    "frameNumber": 7,
                    "opacity": 1.0,
                    "position": [
                        287,
                        333
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00008",
                    "fileName": "Document/Bird Flying/Bird Flying_00008.png",
                    "frameNumber": 8,
                    "opacity": 1.0,
                    "position": [
                        328,
                        305
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00009",
                    "fileName": "Document/Bird Flying/Bird Flying_00009.png",
                    "frameNumber": 9,
                    "opacity": 1.0,
                    "position": [
                        356,
                        279
                    ],
                    "width": 145,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00010",
                    "fileName": "Document/Bird Flying/Bird Flying_00010.png",
                    "frameNumber": 10,
                    "opacity": 1.0,
                    "position": [
                        371,
                        263
                    ],
                    "width": 151,
                    "height": 38,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00011",
                    "fileName": "Document/Bird Flying/Bird Flying_00011.png",
                    "frameNumber": 11,
                    "opacity": 1.0,
                    "position": [
                        383,
                        252
                    ],
                    "width": 149,
                    "height": 43,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00012",
                    "fileName": "Document/Bird Flying/Bird Flying_00012.png",
                    "frameNumber": 12,
                    "opacity": 1.0,
                    "position": [
                        394,
                        246
                    ],
                    "width": 148,
                    "height": 20,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00013",
                    "fileName": "Document/Bird Flying/Bird Flying_00013.png",
                    "frameNumber": 13,
                    "opacity": 1.0,
                    "position": [
                        435,
                        220
                    ],
                    "width": 135,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00014",
                    "fileName": "Document/Bird Flying/Bird Flying_00014.png",
                    "frameNumber": 14,
                    "opacity": 1.0,
                    "position": [
                        480,
                        180
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00015",
                    "fileName": "Document/Bird Flying/Bird Flying_00015.png",
                    "frameNumber": 15,
                    "opacity": 1.0,
                    "position": [
                        517,
                        148
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00016",
                    "fileName": "Document/Bird Flying/Bird Flying_00016.png",
                    "frameNumber": 16,
                    "opacity": 1.0,
                    "position": [
                        534,
                        127
                    ],
                    "width": 148,
                    "height": 18,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00017",
                    "fileName": "Document/Bird Flying/Bird Flying_00017.png",
                    "frameNumber": 17,
                    "opacity": 1.0,
                    "position": [
                        560,
                        103
                    ],
                    "width": 145,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00018",
                    "fileName": "Document/Bird Flying/Bird Flying_00018.png",
                    "frameNumber": 18,
                    "opacity": 1.0,
                    "position": [
                        579,
                        86
                    ],
                    "width": 151,
                    "height": 38,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00019",
                    "fileName": "Document/Bird Flying/Bird Flying_00019.png",
                    "frameNumber": 19,
                    "opacity": 1.0,
                    "position": [
                        595,
                        69
                    ],
                    "width": 149,
                    "height": 43,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00020",
                    "fileName": "Document/Bird Flying/Bird Flying_00020.png",
                    "frameNumber": 20,
                    "opacity": 1.0,
                    "position": [
                        629,
                        54
                    ],
                    "width": 148,
                    "height": 20,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00021",
                    "fileName": "Document/Bird Flying/Bird Flying_00021.png",
                    "frameNumber": 21,
                    "opacity": 1.0,
                    "position": [
                        664,
                        30
                    ],
                    "width": 135,
                    "height": 35,
                    "duration": 1
                },
                {
                    "name": "Bird Flying_00022",
                    "fileName": "Document/Bird Flying/Bird Flying_00022.png",
                    "frameNumber": 22,
                    "opacity": 1.0,
                    "position": [
                        684,
                        -1
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
                },
                {
                    "name": "Cui !_00010",
                    "fileName": "Document/Cui !/Cui !_00010.png",
                    "frameNumber": 10,
                    "opacity": 1.0,
                    "position": [
                        507,
                        297
                    ],
                    "width": 86,
                    "height": 48,
                    "duration": 2
                },
                {
                    "name": "Cui !_00012",
                    "fileName": "Document/Cui !/Cui !_00012.png",
                    "frameNumber": 12,
                    "opacity": 1.0,
                    "position": [
                        528,
                        300
                    ],
                    "width": 116,
                    "height": 56,
                    "duration": 3
                },
                {
                    "name": "Cui !_00015",
                    "fileName": "Document/Cui !/Cui !_00015.png",
                    "frameNumber": 15,
                    "opacity": 1.0,
                    "position": [
                        560,
                        319
                    ],
                    "width": 146,
                    "height": 60,
                    "duration": 2
                },
                {
                    "name": "Cui !_00017",
                    "fileName": "Document/Cui !/Cui !_00017.png",
                    "frameNumber": 17,
                    "opacity": 1.0,
                    "position": [
                        570,
                        342
                    ],
                    "width": 146,
                    "height": 60,
                    "duration": 2
                },
                {
                    "name": "Cui !_00019",
                    "fileName": "Document/Cui !/Cui !_00019.png",
                    "frameNumber": 19,
                    "opacity": 1.0,
                    "position": [
                        594,
                        366
                    ],
                    "width": 174,
                    "height": 85,
                    "duration": 2
                },
                {
                    "name": "Cui !_00021",
                    "fileName": "Document/Cui !/Cui !_00021.png",
                    "frameNumber": 21,
                    "opacity": 1.0,
                    "position": [
                        597,
                        436
                    ],
                    "width": 173,
                    "height": 84,
                    "duration": 2
                },
                {
                    "name": "Cui !_00023",
                    "fileName": "Document/Cui !/Cui !_00023.png",
                    "frameNumber": 23,
                    "opacity": 1.0,
                    "position": [
                        597,
                        487
                    ],
                    "width": 173,
                    "height": 84,
                    "duration": 1
                },
                {
                    "name": "Cui !_00024",
                    "fileName": "Document/Cui !/Cui !_00024.png",
                    "frameNumber": 24,
                    "opacity": 1.0,
                    "position": [
                        598,
                        510
                    ],
                    "width": 173,
                    "height": 84,
                    "duration": 1
                },
                {
                    "name": "Cui !_00025",
                    "fileName": "Document/Cui !/Cui !_00025.png",
                    "frameNumber": 25,
                    "opacity": 1.0,
                    "position": [
                        600,
                        525
                    ],
                    "width": 173,
                    "height": 84,
                    "duration": 1
                },
                {
                    "name": "Cui !_00026",
                    "fileName": "Document/Cui !/Cui !_00026.png",
                    "frameNumber": 26,
                    "opacity": 1.0,
                    "position": [
                        599,
                        533
                    ],
                    "width": 173,
                    "height": 84,
                    "duration": 1
                },
                {
                    "name": "_blank",
                    "fileName": "",
                    "frameNumber": 27,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 6
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
    "originApp": "Krita",
    "originAppVersion": "5.1.1",
    "ocaVersion": "1.1.0"
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
                    "name": "Bird Flying_00002",
                    "fileName": "Document/Bird Flying/Bird Flying_00002.png",
                    "frameNumber": 2,
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
                    "name": "Bird Flying_00003",
                    "fileName": "Document/Bird Flying/Bird Flying_00003.png",
                    "frameNumber": 3,
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
                    "name": "Bird Flying_00004",
                    "fileName": "Document/Bird Flying/Bird Flying_00004.png",
                    "frameNumber": 4,
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
                    "name": "Bird Flying_00005",
                    "fileName": "Document/Bird Flying/Bird Flying_00005.png",
                    "frameNumber": 5,
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
                    "name": "Bird Flying_00006",
                    "fileName": "Document/Bird Flying/Bird Flying_00006.png",
                    "frameNumber": 6,
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
                    "name": "Bird Flying_00007",
                    "fileName": "Document/Bird Flying/Bird Flying_00007.png",
                    "frameNumber": 7,
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
                    "name": "Bird Flying_00008",
                    "fileName": "Document/Bird Flying/Bird Flying_00008.png",
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
                    "name": "Bird Flying_00009",
                    "fileName": "Document/Bird Flying/Bird Flying_00009.png",
                    "frameNumber": 9,
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
                    "name": "Bird Flying_00010",
                    "fileName": "Document/Bird Flying/Bird Flying_00010.png",
                    "frameNumber": 10,
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
                    "name": "Bird Flying_00011",
                    "fileName": "Document/Bird Flying/Bird Flying_00011.png",
                    "frameNumber": 11,
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
                    "name": "Bird Flying_00012",
                    "fileName": "Document/Bird Flying/Bird Flying_00012.png",
                    "frameNumber": 12,
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
                    "name": "Bird Flying_00013",
                    "fileName": "Document/Bird Flying/Bird Flying_00013.png",
                    "frameNumber": 13,
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
                    "name": "Bird Flying_00014",
                    "fileName": "Document/Bird Flying/Bird Flying_00014.png",
                    "frameNumber": 14,
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
                    "name": "Bird Flying_00015",
                    "fileName": "Document/Bird Flying/Bird Flying_00015.png",
                    "frameNumber": 15,
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
                    "name": "Bird Flying_00016",
                    "fileName": "Document/Bird Flying/Bird Flying_00016.png",
                    "frameNumber": 16,
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
                    "name": "Bird Flying_00017",
                    "fileName": "Document/Bird Flying/Bird Flying_00017.png",
                    "frameNumber": 17,
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
                    "name": "Bird Flying_00018",
                    "fileName": "Document/Bird Flying/Bird Flying_00018.png",
                    "frameNumber": 18,
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
                    "name": "Bird Flying_00019",
                    "fileName": "Document/Bird Flying/Bird Flying_00019.png",
                    "frameNumber": 19,
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
                    "name": "Bird Flying_00020",
                    "fileName": "Document/Bird Flying/Bird Flying_00020.png",
                    "frameNumber": 20,
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
                    "name": "Bird Flying_00021",
                    "fileName": "Document/Bird Flying/Bird Flying_00021.png",
                    "frameNumber": 21,
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
                    "name": "Bird Flying_00022",
                    "fileName": "Document/Bird Flying/Bird Flying_00022.png",
                    "frameNumber": 22,
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
                },
                {
                    "name": "Cui !_00010",
                    "fileName": "Document/Cui !/Cui !_00010.png",
                    "frameNumber": 10,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 2
                },
                {
                    "name": "Cui !_00012",
                    "fileName": "Document/Cui !/Cui !_00012.png",
                    "frameNumber": 12,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 3
                },
                {
                    "name": "Cui !_00015",
                    "fileName": "Document/Cui !/Cui !_00015.png",
                    "frameNumber": 15,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 2
                },
                {
                    "name": "Cui !_00017",
                    "fileName": "Document/Cui !/Cui !_00017.png",
                    "frameNumber": 17,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 2
                },
                {
                    "name": "Cui !_00019",
                    "fileName": "Document/Cui !/Cui !_00019.png",
                    "frameNumber": 19,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 2
                },
                {
                    "name": "Cui !_00021",
                    "fileName": "Document/Cui !/Cui !_00021.png",
                    "frameNumber": 21,
                    "opacity": 1.0,
                    "position": [
                        640.0,
                        360.0
                    ],
                    "width": 1280,
                    "height": 720,
                    "duration": 2
                },
                {
                    "name": "Cui !_00023",
                    "fileName": "Document/Cui !/Cui !_00023.png",
                    "frameNumber": 23,
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
                    "name": "Cui !_00024",
                    "fileName": "Document/Cui !/Cui !_00024.png",
                    "frameNumber": 24,
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
                    "name": "Cui !_00025",
                    "fileName": "Document/Cui !/Cui !_00025.png",
                    "frameNumber": 25,
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
                    "name": "Cui !_00026",
                    "fileName": "Document/Cui !/Cui !_00026.png",
                    "frameNumber": 26,
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
                    "frameNumber": 27,
                    "opacity": 1.0,
                    "position": [
                        0,
                        0
                    ],
                    "width": 0,
                    "height": 0,
                    "duration": 6
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
    "originApp": "Krita",
    "originAppVersion": "5.1.1",
    "ocaVersion": "1.1.0"
}
```