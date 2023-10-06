# OCA

Open Cel Animation format

*OCA* is an open format to ease the exchange of traditionnal/frame-by-frame/cel animation between different applications.

You can [read the documentation here](http://oca.rxlab.guide) for more information and specifications of the format.

## Open

The format is completely open, that means everyone can export to or export from OCA very easily, and there's no license or whatever to use the format.

The code provided in the `lib` folder is licensed under the GNU-GPLv3 license (for now), which means you must comply to this license or any compatible free and open source license to use it. If you can't, you'll have to write your code for handling OCA completely from scratch.

## Implementations

<!-- implementation_list:begin -->
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
