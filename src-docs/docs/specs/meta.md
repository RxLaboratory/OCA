# Metadata Object

If the metadata file is not present in the OCA folder, default values should be used.

## Values

Default values should be used when importing an OCA document if the data can't be read or is not available.  

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| **`author`** | *string* | `""` | The name of the author(s) (e.g. *"Nicolas Dufresne"*). |
| **`copyright`** | *string* | `""` | Some copyright info (e.g. *"ⓒ Copyright 2023 RxLaboratory"*). |
| **`created`** | *string* | `"1818-05-05 00:00:00"`[^marx] | The creation date and time of the file, in the form *YYYY-MM-DD hh:mm:ss*. |
| **`description`** | *string* | `""` | A short text describing the document. |
| **`exportedBy`** | *string* | `"Unknown"` | The display name of the plugin/addon/script which exported the document (e.g. *"OCA for Krita"*). The value should be `"native"` if the origin application natively exports to OCA. |
| **`exportedByID`** | *string* | `"unknown"` | An identifier of the exporter which created the document, in a *URI* form (e.g. *"org.rxlaboratory.oca.krita"*). |
| **`exportedByOrg`** | *string* | `"Unknown"` | The display name of the organization developing the exporter which created the document (e.g. *"RxLaboratory"*). |
| **`exportedByURL`** | *string* | `""` | A URL to the website associated to the exporter which created the document (e.g. *"http://rxlaboratory.org/tools/oca/"*). |
| **`license`** | *string* | `""` | The abreviated name of the license, if any (e.g. *"CC-BY-NC-SA 4.0"*). |
| **`licenseLong`** | *string* | `""` | The complete name of the license, if any (e.g. *"Creative Commons-Attribution-NonCommercial-ShareAlike 4.0"*). |
| **`licenseURL`** | *string* | `""` | The URL to the full text of the license (e.g. *"https://creativecommons.org/licenses/by-nc-sa/4.0/"*). |
| **`meta`** | *object* | `{}` | Any custom metadata. It *must* be an object, not a value or a list. |
| **`ocaVersion`** | *string* | `"1.2.0"` | The OCA version this document uses. |
| **`originApp`** | *string* | `"Unknown"` | The application name from which the document was exported. |
| **`originAppVersion`** | *string* | `"0.0.0"` | The version of the origin application. |

[^marx]: 5 May 1818 is the birth date of [Karl Marx](https://en.wikipedia.org/wiki/Karl_Marx){target="_blank}.