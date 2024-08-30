from config import ROOT
from classes import Palette
from setup import setup_parser


REPO = ROOT.parent

parser = setup_parser()
argv = parser.parse_args()


route = ROOT / "palettes"
palettes = list(route.glob("**/*.json"))

# JS
route = argv.js
if route:
  with open(REPO / route, "w") as dest:
    dest.write(

for each in palettes:
