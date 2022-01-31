![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# Examples

## Generic

A generic OCA file looks like this:

```json
{
    "name": "Document_name",
    "frameRate": 24,
    "width": 1920,
    "height": 1080,
    "startTime": 0,
    "endTime": 220,
    "colorDepth": "U8",
    "backgroundColor": [
        0.9882352941176471,
        0.9137254901960784,s
        0.30980392156862746,
        1.0
    ],
    "ocaVersion": "1.1.0",
    "originApp": "Krita",
    "originAppVersion": "5.0.0",
    "layers": [
        {
            "name": "Layer_name_1",
            "frames": [
                {
                    "name": "Layer_name_1_00000",
                    "fileName": "Document_name.oca/Layer_name_1/Layer_name_1_00000.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        959,
                        539
                    ],
                    "width": 1920,
                    "height": 1080,
                    "duration": 110
                },
                {
                    "name": "Layer_name_1_00110",
                    "fileName": "Document_name.oca/Layer_name_1/Layer_name_1_00110.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        959,
                        539
                    ],
                    "width": 1920,
                    "height": 1080,
                    "duration": 2
                },
                {
                    "name": "Layer_name_1_00112",
                    "fileName": "Document_name.oca/Layer_name_1/Layer_name_1_00112.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        959,
                        539
                    ],
                    "width": 1920,
                    "height": 1080,
                    "duration": 2
                },
                {
                    "name": "Layer_name_1_00114",
                    "fileName": "Document_name.oca/Layer_name_1/Layer_name_1_00114.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        959,
                        539
                    ],
                    "width": 1920,
                    "height": 1080,
                    "duration": 6
                },
                {
                    "name": "Layer_name_1_00200",
                    "fileName": "Document_name.oca/Layer_name_1/Layer_name_1_00200.png",
                    "frameNumber": 0,
                    "opacity": 1.0,
                    "position": [
                        959,
                        539
                    ],
                    "width": 1920,
                    "height": 1080,
                    "duration": 20
                }
            ],
            "childLayers": [],
            "type": "paintlayer",
            "fileType": "png",
            "blendingMode": "normal",
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
        },
        {
            "name": "Group_name_2",
            "frames": [],
            "childLayers": [
                {
                    "name": "Layer_name_3",
                    "frames": [
                        {
                            "name": "Layer_name_3_00000",
                            "fileName": "Document_name.oca/Group_name_2/Layer_name_3/Layer_name_3_00000.png",
                            "frameNumber": 0,
                            "opacity": 1.0,
                            "position": [
                                960,
                                540
                            ],
                            "width": 1920,
                            "height": 1080,
                            "duration": 3
                        },
                        {
                            "name": "Layer_name_3_00003",
                            "fileName": "Document_name.oca/Group_name_2/Layer_name_3/Layer_name_3_00003.png",
                            "frameNumber": 0,
                            "opacity": 1.0,
                            "position": [
                                960,
                                540
                            ],
                            "width": 1920,
                            "height": 1080,
                            "duration": 7
                        }
                        {
                            "name": "_blank_",
                            "fileName": "",
                            "frameNumber": 0,
                            "opacity": 1.0,
                            "position": [
                                0,
                                0
                            ],
                            "width": 0,
                            "height": 0,
                            "duration": 210
                        }
                    ],
                    "childLayers": [],
                    "type": "paintlayer",
                    "fileType": "png",
                    "blendingMode": "normal",
                    "animated": true,
                    "position": [
                        960.0,
                        540.0
                    ],
                    "width": 1920,
                    "height": 1080,
                    "label": 0,
                    "opacity": 1.0,
                    "visible": true,
                    "passThrough": false,
                    "reference": false
                }
            ],
            "type": "grouplayer",
            "fileType": "png",
            "blendingMode": "normal",
            "animated": false,
            "position": [
                957,
                544
            ],
            "width": 1743,
            "height": 1051,
            "label": 0,
            "opacity": 1.0,
            "visible": true,
            "passThrough": false,
            "reference": false
        }
    ]
}
```

And its corresponding folder structure should look like this:

```
|v Document_name.oca
 |- Document_name.oca
 |v Layer_name_1
  |- Layer_name_1_00000.png
  |- Layer_name_1_00110.png
  |- Layer_name_1_00112.png
  |- Layer_name_1_00114.png
  |- Layer_name_1_00200.png
 |v Group_name_2
  |v Layer_name_3
   |- Layer_name_3_00000.png
   |- Layer_name_3_00003.png
  |> Layer_name_4
  |> Layer_name_5
 |> Group_name_6
```