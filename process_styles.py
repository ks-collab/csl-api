from glob import glob
import xml.etree.ElementTree as ET
import json

PATH_TO_STYLES = "./styles/"
XML_NAMESPACE = "http://purl.org/net/xbiblio/csl"

styles = []

for path in glob(f"{PATH_TO_STYLES}*.csl"):
    tree = ET.parse(path)
    root = tree.getroot()
    title = list(root.iter(f'{{{XML_NAMESPACE}}}title'))[0].text
    updated = list(root.iter(f'{{{XML_NAMESPACE}}}updated'))[0].text
    filename = path[len(PATH_TO_STYLES):]
    styles.append({
        "filename": filename,
        "title": title,
        "updated_at": updated
    })
    styles.sort(key=lambda x: x["title"])

with open("styles.json", "w") as outfile:
    json.dump(styles, outfile, indent=2)