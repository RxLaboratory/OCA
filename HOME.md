# OCA

*OCA*, Open Cel Animation format, is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

You can [read the documentation here](http://oca.rxlab.guide) for more information and specifications of the format.

We're providing some implementations of OCA as add-ons for a few applications and other applications already support it natively. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

<!-- implementation_list:begin -->
| App | Add-on | Exports | Imports | Comments | Maintainer |
|---|---|---|---|---|---|
| [After Effects](https://www.adobe.com/products/aftereffects.html) | [DuIO](https://github.com/RxLaboratory/DuIO) | - | **◉** |  | [RxLaboratorio / Duduf](https://rxlaboratorio.org) |
| [Animation Paper](https://animationpaper.com/) | *Native* | **◉** | *?* |  | Niels Krogh Mortensen |
| [Blender](https://blender.org/) | [Bluik](https://rxlaboratory.org/tools/bluik/) | **○** | **◉** | Exporter for Grease Pencil planned. | [RxLaboratorio / Duduf](https://rxlaboratorio.org) |
| [Callipeg](https://callipeg.com) | *Native* | **◉** | - |  | Enoben |
| [Fusion](https://www.blackmagicdesign.com/products/fusion/) | [Reactor (using Vonk Ultra)](https://www.steakunderwater.com/) | - | **◉** |  | [We Suck Less](https://www.steakunderwater.com/wesuckless/) |
| [Krita](http://krita.org/) | [OCA for Krita](https://rxlaboratory.org/tools/oca-for-krita/) | **◉** | **○** |  | [RxLaboratorio / Duduf](https://rxlaboratorio.org) |
| [OpenToonz](https://opentoonz.github.io/e/) | *Native* | **◉** | - | Some limitations, see https://github.com/opentoonz/opentoonz/pull/4483 | [Dwango](https://en.dwango.co.jp/) |
| [Photoshop](https://www.adobe.com/products/photoshop.html) | OCA | **○** | - |  | [RxLaboratory / Duduf](https://rxlaboratory.org) |
| [TVPaint](https://www.tvpaint.com/) | OCA | **○** | - |  | [RxLaboratorio / Duduf](https://rxlaboratorio.org) |
| XDTS | [OCA to XDTS converter](https://wolfinabowl.itch.io/oca-to-xdts-converter) | **◉** | **◉** | XDTS is a format supported by OpenToonz, Tahoma, Clip Studio Paint EX and Toei Animation Digital Exposure Sheet. | [Wolf In A Bow](https://wolfinabowl.itch.io/) |

Legend:  
**◉** | Available  
**◔** | In development  
**○** | Planned  
\- | Not supported

<!-- implementation_list:end -->

## Principles

- OCA has to be open and simple: it must be easy to implement an exporter or importer in any application providing a scripting API.

- As it relies on existing and standard file formats (images and json/text files) stored in a simple folder, the OCA format can be imported in any application manually, even if the application does not directly support it.

- OCA stores the most common features used by drawing/animation software: layers, groups, blending modes, animation exposure (x-sheet), etc.

## Features

OCA supports the most common features of all drawing/animation software:

- Layers
- Layer Groups (and pass through mode if any)
- Layer Labels
- Layer Visibility
- Blending Modes
- Layer Alpha options (inherit alpha)
- Keyframes and their duration (animation exposure)
- Opacity Keyframes
- Layer Sizes and Coordinates
- Document background color
- Document color depth
- Duration
- Framerate

All these properties are stored in a simple *JSON* file, and the images are stored in standard image file formats: *PNG, EXR, SVG*…

Everything is assembled in a folder which name ends with `.oca`. The *JSON* file is at the root, while the images are stored in subfolders corresponding to layers and groups.

## Open Format / Free license

The format is completely open, that means everyone can export to or export from OCA very easily, and there's no license or whatever to use the format.

The code provided in the source code repository is released under the GNU-GPLv3 license (for now), which means you must comply to this license or any compatible free and open source license to use it. If you can't, you'll have to write your code for handling OCA completely from scratch.


