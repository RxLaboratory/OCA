![META](authors:Nicolas "Duduf" Dufresne;license:GNU-FDL;copyright:2022;updated:2022/01/31)

# OCA, The *Open Cel Animation* format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

![](img/icons/oca.png){class="align-center"}

## Principles

- *OCA* has to be open and simple: it must be easy to implement an exporter or importer in any application providing a scripting API.

- As it relies on existing and standard file formats (images and json/text files) stored in a simple folder, the *OCA* format can be imported in any application manually, even if the application does not directly support it.

- *OCA* stores the most common features used by drawing/animation software: layers, groups, blending modes, animation exposure (x-sheet), etc.

![YOUTUBE](cjAMmYF8OtE)

## Implementation

We're providing some implementations of *OCA* as add-ons for a few applications, and third-party developers have added support for it in their applications too. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

| Application | Add-on name | Exporter | Importer | Comments |
|---|---|---|---|---|
| After Effects | [DuIO](https://github.com/Rainbox-dev/DuAEF_DuIO) | - | ![icon](img/icons/green_tick.png){style="width: 16px;"} | |
| [Animation Paper](https://animationpaper.com/) | *Native* | ![icon](img/icons/green_tick.png){style="width: 16px;"} | ? | *Third-party* |
| [Blender](http://blender.org) | Bluik | ![icon](img/icons/orange_diamond.png){style="width: 16px;"} | ![icon](img/icons/green_tick.png){style="width: 16px;"} | Exporter for Grease Pencil |
| [Fusion](https://www.blackmagicdesign.com/products/fusion/) | [Reactor](https://www.steakunderwater.com/) (using *Vonk Ultra*) | - | ![icon](img/icons/green_tick.png){style="width: 16px;"} | *Third-party*. |
| [Krita](http://krita.org) | [OCA for Krita](https://github.com/Rainbox-dev/DuKRIF_OCA) | ![icon](img/icons/green_tick.png){style="width: 16px;"} | ![icon](img/icons/orange_diamond.png){style="width: 16px;"} | |
| [OpenToonz](https://opentoonz.github.io/e/) | *Native* | ![icon](img/icons/green_tick.png){style="width: 16px;"} | - | *Third-party*. Available in the latest [nightly build](https://github.com/opentoonz/opentoonz/releases) for now, will be in the next release. |
| Photoshop | OCA for Photoshop | ![icon](img/icons/orange_diamond.png){style="width: 16px;"} | - | |
| TVPaint | OCA for TVPaint | ![icon](img/icons/orange_diamond.png){style="width: 16px;"} | - | |

Legend:  
![icon](img/icons/green_tick.png){style="width: 16px;"} | Available  
![icon](img/icons/blue_circle.png){style="width: 16px;"} | In development  
![icon](img/icons/orange_diamond.png){style="width: 16px;"} | Planned  
- | Not supported

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

## Speficications

- [Examples](specs/examples.md)
- [Folder Structure](specs/folder-structure.md)

### JSON Objects

- [Root Object Specs](specs/root.md)
- [Layer Object Specs](specs/layer.md)
- [Frame Object Specs](specs/frame.md)

### Values

- [Durations](specs/durations.md)
- [Color Depth](specs/color-depth.md)
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
