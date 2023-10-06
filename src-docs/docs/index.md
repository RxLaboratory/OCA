# ![](img/icons/oca.png){style="width:2em;"} OCA, The *Open Cel Animation* format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

## Principles

- *OCA* has to be open and simple: it must be easy to implement an exporter or importer in any application providing a scripting API.

- As it relies on existing and standard file formats (images and json/text files) stored in a simple folder, the *OCA* format can be imported in any application manually, even if the application does not directly support it.

- Full freely available documentation.

- Extensible, but private undocumented extensions should be excluded, any extension should be added to the spec and documentation of the file format.

- *OCA* stores the most common features used by drawing/animation software: layers, groups, blending modes, animation exposure (x-sheet), etc.

- Applications are not expected to support all features of the file format, but when manipulating the file they should not lose any information they cannot handle

![YOUTUBE](cjAMmYF8OtE)

## Implementation

We're providing some implementations of *OCA* as add-ons for a few applications, and third-party developers have added support for it in their applications too. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

<!-- implementation_list:begin -->
| App | Add-on | Exports | Imports | Comments | Maintainer |
|---|---|---|---|---|---|
| [After Effects](https://www.adobe.com/products/aftereffects.html){target="_blank"} | [DuIO](https://github.com/Rainbox-dev/DuAEF_DuIO){target="_blank"} | - | **◉** |  | [RxLaboratory / Duduf](https://rxlaboratory.org){target="_blank"} |
| [Animation Paper](https://animationpaper.com/){target="_blank"} | [](){target="_blank"} | **◉** | *?* |  | [Niels Krogh Mortensen](){target="_blank"} |
| [Blender](https://blender.org/){target="_blank"} | [Bluik](https://rxlaboratory.org/tools/bluik/){target="_blank"} | **○** | **◉** | Exporter for Grease Pencil planned. | [RxLaboratory / Duduf](https://rxlaboratory.org){target="_blank"} |
| [Callipeg](https://callipeg.com){target="_blank"} | [](){target="_blank"} | **◉** | - |  | [Enoben](){target="_blank"} |
| [Fusion](https://www.blackmagicdesign.com/products/fusion/){target="_blank"} | [Reactor (using Vonk Ultra)](https://www.steakunderwater.com/){target="_blank"} | - | **◉** |  | [We Suck Less](https://www.steakunderwater.com/wesuckless/){target="_blank"} |
| [Krita](http://krita.org/){target="_blank"} | [OCA for Krita](https://rxlaboratory.org/tools/oca-for-krita/){target="_blank"} | **◉** | **○** |  | [RxLaboratory / Duduf](https://rxlaboratory.org){target="_blank"} |
| [OpenToonz](https://opentoonz.github.io/e/){target="_blank"} | [](){target="_blank"} | **◉** | - | Some limitations, see https://github.com/opentoonz/opentoonz/pull/4483 | [Dwango](https://en.dwango.co.jp/){target="_blank"} |
| [Photoshop](https://www.adobe.com/products/photoshop.html){target="_blank"} | [OCA](){target="_blank"} | **○** | - |  | [RxLaboratory / Duduf](https://rxlaboratory.org){target="_blank"} |
| [TVPaint](https://www.tvpaint.com/){target="_blank"} | [OCA](){target="_blank"} | **○** | - |  | [RxLaboratory / Duduf](https://rxlaboratory.org){target="_blank"} |
| [XDTS](){target="_blank"} | [OCA to XDTS converter](https://wolfinabowl.itch.io/oca-to-xdts-converter){target="_blank"} | **◉** | **◉** | XDTS is a format supported by OpenToonz, Tahoma, Clip Studio Paint EX and Toei Animation Digital Exposure Sheet. | [Wolf In A Bow](https://wolfinabowl.itch.io/){target="_blank"} |

Legend:  
**◉** | Available  
**◔** | In development  
**○** | Planned  
- | Not supported

<!-- implementation_list:end -->


!!! tip
    The *OCA* format is made to be simple to export/import in any application and it should not be difficult to implement it/write your own script for your application.

### Icon

You may use these icons when talking about or implementing OCA.

**SVG**: ![SVG icon](img/icons/oca-icon.svg){style="max-width:128px"}

**PNG**: ![PNG icon](img/icons/oca.png){style="max-width:128px"}

*(Right-click on the images to save them)*

## Features

*OCA* supports the most common features of all drawing/animation software:

- Layers
- Layer Groups (and pass through mode if any)
- Layer Labels
- Layer Visibility
- Layer Blending Modes
- Layer Alpha options (inherit alpha)
- Keyframes and their duration (animation exposure)
- Opacity Keyframes
- Layer Sizes and Coordinates
- Document background color
- Document color depth
- Duration
- Framerate

All these properties are stored in a simple *JSON* file, and the images are stored in standard image file formats: *PNG*, *EXR*, *SVG*...

Everything is assembled in a folder which name ends with `.oca`. The *JSON* file is at the root, while the images are stored in subfolders corresponding to layers and groups.

More features may be added later, have a look at the [**Roadmap**](roadmap.md)!

## Specifications

- [Examples](specs/examples.md)
- [Folder Structure](specs/folder-structure.md)
- [File Specifications](specs/folder-structure.md)

### JSON Objects

- [Metadata Object Specs](specs/meta.md)
- [Root Object Specs](specs/root.md)
- [Layer Object Specs](specs/layer.md)
- [Frame Object Specs](specs/frame.md)

### Values

- [Durations](specs/durations.md)
- [Coordinates and transform](specs/coordinates.md)
- [Opacity, Colors and Color Depth](specs/color-depth.md)
- [Layer Types](specs/layer-types.md)
- [Blending Modes](specs/blending-modes.md)
- [Layer Labels](specs/blending-modes.md)

## License

### Software

**Copyright (C)  2020-2022 Nicolas Dufresne and Contributors.**  
This program is free software; you can redistribute them and/or modify them under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the *GNU General Public License* along with *DuBuilder*. If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

### This Documentation

**Copyright (C)  2020-2022 Nicolas Dufresne and Contributors.**  
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation;  
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "[Documentation License](licenses/gfdl.md)".

![GNU](img/gnu.png) ![GFDL](img/gfdl-logo.png)
