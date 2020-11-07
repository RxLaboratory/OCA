# OCA

The *Open Cel Animation* format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

## Principles

- *OCA* has to be open and simple: it must be easy to implement an exporter or importer in any application providing a scripting API.

- As it relies on existing and standard file formats (images and json/text files) stored in a simple folder, the *OCA* format can be imported in any application manually, even if the application does not directly support it.

- *OCA* stores the most common features used by drawing/animation software: layers, groups, blending modes, animation exposure (x-sheet), etc.

## Implementation

We're providing some implementations of *OCA* as add-ons for a few applications. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

| Application | Add-on name | Exporter | Importer | Comments |
|---|---|---|---|---|
| [Krita](http://krita.org) | [OCA for Krita](https://github.com/Rainbox-dev/DuKRIF_OCA) | ![icon](img/icons/blue_circle.png) | ![icon](img/icons/orange_diamond.png) | |
| Adobe Photoshop | OCA for Photoshop | ![icon](img/icons/orange_diamond.png) | ![icon](img/icons/red_circle.png) | |
| TVPaint | OCA for TVPaint | ![icon](img/icons/orange_diamond.png) | ![icon](img/icons/red_circle.png) | |
| Adobe After Effects | [DuIO](https://github.com/Rainbox-dev/DuAEF_DuIO) | ![icon](img/icons/red_circle.png) | ![icon](img/icons/blue_circle.png) | |
| [Blender](http://blender.org) | OCA for Blender | ![icon](img/icons/red_circle.png) | ![icon](img/icons/orange_diamond.png) | |

Legend:  
![icon](img/icons/green_tick.png) | Available  
![icon](img/icons/blue_circle.png) | In development  
![icon](img/icons/orange_diamond.png) | Planned  
![icon](img/icons/red_circle.png) | Not supported

!!! tip
    The *OCA* format is made to be simple to export/import in any application and it should not be difficult to implement it/write your own script for your application.

## Features

*OCA* supports the most common features of all drawing/animation software:

- Layers
- Layer Groups (and pass through mode if any)
- Layer Labels
- Layer Visibility
- Keyframes and their duration (animation exposure)
- Opacity Keyframes
- Blending Modes
- Layer Sizes and Coordinates
- Document background color
- Document color depth
- Duration
- Framerate

For a technical description of the format and some examples, please [refer to the Github Repository](https://github.com/Rainbox-dev/OCA).

## License

### Software

**Copyright (C)  2020 Nicolas Dufresne and Contributors.**  
This program is free software; you can redistribute them and/or modify them under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the *GNU General Public License* along with *DuBuilder*. If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/).

### This Documentation

**Copyright (C)  2020 Nicolas Dufresne and Contributors.**  
Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation;  
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "[Documentation License](licenses/gfdl.md)".

![GNU](img/gnu.png) ![GFDL](img/gfdl-logo.png)