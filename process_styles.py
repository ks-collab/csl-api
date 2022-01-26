from glob import glob
import xml.etree.ElementTree as ET
import json

xmlns = "http://purl.org/net/xbiblio/csl"

styles = []

def process_directory(path):
    for path in glob(f"{path}/*.csl"):
        root = ET.parse(path).getroot()
        title = next(root.iter(f'{{{xmlns}}}title')).text
        updated = next(root.iter(f'{{{xmlns}}}updated')).text
        filename = path
        styles.append({
            "filename": filename,
            "title": title,
            "updated_at": updated
        })


process_directory("styles")
process_directory("styles/dependent")

print(f"Found {len(styles)} styles")

styles.sort(key=lambda x: x["title"])

with open("styles.json", "w") as outfile:
    json.dump(styles, outfile, indent=2)
