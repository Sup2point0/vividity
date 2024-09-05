import json
from pathlib import Path

from config import ROOT
from classes import Palette
from setup import setup_parser


CWD = Path.cwd()

## load
sources = (ROOT / "palettes").glob("**/*.json")
palettes = []

for path in sources:
  with open(path, "r") as source:
    data = json.load(source)

  palettes.append(Palette.from_json(data))

## parse
parser = setup_parser()
argv = parser.parse_args()

print(f">> Vividity / exporting...")

## CSS
if argv.css or "css" in argv.flags:
  route = CWD / argv.root / (argv.css or "palettes.css")
  with open(route, "w") as dest:
    dest.write(Palette.export_css(palettes))

## SCSS
if argv.scss or "scss" in argv.flags:
  route = CWD / argv.root / (argv.scss or "palettes.scss")
  with open(route, "w") as dest:
    dest.write(Palette.export_scss(palettes))

## JS
if argv.js or "js" in argv.flags:
  route = CWD / argv.root / (argv.js or "palettes.js")
  with open(route, "w") as dest:
    dest.write(Palette.export_js(palettes))


print(">> Vividity / done!")
