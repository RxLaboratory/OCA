# OCA

*OCA*, Open Cel Animation format, is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

You can [read the documentation here](http://oca.rxlab.guide) for more information and specifications of the format.

We're providing some implementations of OCA as add-ons for a few applications and other applications already support it natively. If the application you need is not listed, you can politely ask for it in a feature request and we'll consider it.

- **After Effects / [DuIO](https://rxlaboratorio.org/rx-tool/duio/)**
  - Export: -
  - Import: **◉**
  - Maintained by: [RxLaboratorio / Duduf](https://rxlaboratorio.org)
- **[Animation Paper](https://animationpaper.com/)** / *Native support*
  - Export: **◉**
  - Import: *?*
  - Maintained by: Niels Krogh Mortensen
- **Blender/ [Bluik](https://rxlaboratorio.org/rx-tool/bluik/)**
  - Export: **○** (Exporter for Grease Pencil planned)
  - Import: **◉**
  - Maintained by: [RxLaboratorio / Duduf](https://rxlaboratorio.org)
- **[Callipeg](https://callipeg.com) / *Native support***
  - Export: **◉**
  - Import: -
  - Maintained by: Enoben
- **Fusion / [Reactor (using Vonk Ultra)](https://www.steakunderwater.com/)**
  - Export: -
  - Import: **◉**
  - Maintained by: [We Suck Less](https://www.steakunderwater.com/wesuckless/)
- **Krita / [OCA for Krita](https://rxlaboratorio.org/rx-tool/oca-for-krita/)**
  - Export: **◉**
  - Import: **○**
  - Maintained by: [RxLaboratorio / Duduf](https://rxlaboratorio.org)
- **[OpenToonz](https://opentoonz.github.io/e/) / *Native support***
  - Export: **◉** with [some limitations](ttps://github.com/opentoonz/opentoonz/pull/4483)
  - Import: -
  - Maintained by: [Dwango](https://en.dwango.co.jp/)
- **Photoshop / OCA for Photoshop**
  - Export: **○**
  - Import: -
  - Maintained by: [RxLaboratorio / Duduf](https://rxlaboratorio.org)
- **TVPaint / OCA for TVPaint**
  - Export: **○**
  - Import: -
  - Maintained by: [RxLaboratorio / Duduf](https://rxlaboratorio.org)
- **XDTS / [OCA to XDTS converter](https://wolfinabowl.itch.io/oca-to-xdts-converter)**
  - Export: **◉**
  - Import: **◉**
  - XDTS is a format supported by OpenToonz, Tahoma, Clip Studio Paint EX and Toei Animation Digital Exposure Sheet.
  - Maintained by: [Wolf In A Bow](https://wolfinabowl.itch.io/)

Legend:  
**◉** | Available  
**◔** | In development  
**○** | Planned  
\- | Not supported

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


