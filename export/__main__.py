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

## CSS
if argv.css:
  with open(CWD / argv.css, "w") as dest:
    dest.write(Palette.export_css(palettes))

# JS
# route = argv.js
# if route:
#   with open(REPO / route, "w") as dest:
#     dest.write(

# for each in palettes:
