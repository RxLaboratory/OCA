"""Updates the list of implementations in the README and the doc"""

import os
import json

rootPath = os.path.dirname(os.path.abspath(__file__))
rootPath = os.path.dirname(rootPath)

listFile = os.path.join(rootPath, "implementations.json")

markdownFiles = (
    os.path.join(rootPath, "README.md"),
    os.path.join(rootPath, "src-docs", "docs", "index.md"),
)

STATUS = {
    "-": "-",
    "no": "-",
    "yes": "**◉**",
    "planned": "**○**",
    "in_dev": "**◔**",
    "?": "*?*"
}

# Load list

implementations = ()

print("Loading list...")
with open(listFile, "r", encoding="UTF8") as l:
    implementations = json.load(l)
    if "implementations" in implementations:
        implementations = implementations["implementations"]
    else:
        implementations = ()
        print("Invalid implementations file!")

print("Found " + str(len(implementations)) + " implementations.")

implementations = sorted(implementations, key=lambda d: d["host_name"])

# Build table
tab = "| App | Add-on | Exports | Imports | Comments | Maintainer |\n|---|---|---|---|---|---|"

for impl in implementations:
    o = impl.get("export", "-")
    i = impl.get("import", "-")

    if o in STATUS:
        o = STATUS[o]
    else:
        o = "?"

    if i in STATUS:
        i = STATUS[i]
    else:
        i = "?"

    app=impl.get("host_name", "")
    app_url=impl.get("host_url", "")
    if app_url != "":
        app = f"[{app}]({app_url})"

    addon=impl.get("addon_name", "*Native*")
    if addon == "" or addon == "native" or addon == "Native":
        addon = "*Native*"
    addon_url=impl.get("addon_url", "")
    if addon_url != "":
        addon = f"[{addon}]({addon_url})"

    comment=impl.get("comment", "")

    dev=impl.get("maintainer_name", "")
    dev_url=impl.get("maintainer_url", "")
    if dev_url != "":
        dev = f"[{dev}]({dev_url})"

    tab = tab + f"\n| {app} | {addon} | {o} | {i} | {comment} | {dev} |"

status_yes = STATUS["yes"]
status_no = STATUS["no"]
status_p = STATUS["planned"]
status_d = STATUS["in_dev"]
tab = tab + f"\n\nLegend:  \n{status_yes} | Available  \n{status_d} | In development  \n{status_p} | Planned  \n\\{status_no} | Not supported\n\n"

def write(path):
    """Writes the tab in a file"""
    with open(path, 'r', encoding='UTF8') as file:
        lines = file.readlines()
    with open(path, 'w', encoding='UTF8') as file:
        in_block = False
        block_written = False

        for line in lines:

            if not in_block:
                if 'implementation_list:begin' in line:
                    in_block = True
                    block_written = False
                file.write(line)

            if not in_block:
                continue

            if in_block and not block_written:
                file.write(tab)
                block_written = True

            if block_written:
                if 'implementation_list:end' in line:
                    in_block = False
                    file.write(line)
                continue

for md in markdownFiles:
    write(md)
