# OCA

Open Cel Animation format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

You can [read the documentation here](http://oca.rxlab.guide) for more information and specifications of the format.

## Open

The format is completely open, that means everyone can export to or export from OCA very easily, and there's no license or whatever to use the format.

The code provided in the `lib` folder is licensed under the GNU-GPLv3 license (for now), which means you must comply to this license or any compatible free and open source license to use it. If you can't, you'll have to write your code for handling OCA completely from scratch.

## Implementations

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




To submit a new app or add-on to be listed here and on all OCA-related sites, edit the [`implementations.json`](implementations.json) file and submit a pull request.

Each add-on or app is described like this:

```json
{
    {
        "host_name": "Name of the app importing or exporting",
        "host_url": "https://super.app.com",
        "addon_name": "OCA for Super APP. Can be left empty if it's a native support without addon",
        "addon_url": "https://oca.for.superapp.com",
        "export": "one of: no, yes, planned, in_dev, ?",
        "import": "yes",
        "comment": "Just a few details in a single line about the implementation.",
        "maintainer_name": "Name of the developer/org/company...",
        "maintainer_url": "https://oca.maintainer.org"
    }
}
```
