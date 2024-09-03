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
if argv.css:
  with open(CWD / argv.css, "w") as dest:
    dest.write(Palette.export_css(palettes))

## SCSS
if argv.css:
  with open(CWD / argv.scss, "w") as dest:
    dest.write(Palette.export_scss(palettes))

## JS
if argv.js:
  with open(CWD / argv.js, "w") as dest:
    dest.write(Palette.export_js(palettes))
