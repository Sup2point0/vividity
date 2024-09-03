from __future__ import annotations
from typing import Iterable

import json
import re
from copy import copy
from dataclasses import dataclass

from jsonschema import validate

from ..config import ROOT


with open(ROOT / "technicals/schema.json", "r") as source:
  SCHEMA = json.load(source)


@ dataclass
class Palette:
  name: str
  shard: str = None
  desc: str = ""
  ver: str = "1.0"

  duality: str = None
  cols: dict[str, str] = None

  def __post_init__(self):
    if self.shard is None:
      self.shard = self.name.lower().replace(" ", "-")
    
    if self.cols is None:
      self.cols = {}
      
  @ staticmethod
  def from_json(data: dict) -> Palette:
    '''Load a colour palette from its JSON data.'''

    data = copy(data)
    data.pop("$schema", None)
    validate(data, SCHEMA)

    return Palette(
      name = data.pop("name"),
      shard = data.pop("shard", None),
      ver = data.pop("ver", "1.0"),
      desc = data.pop("desc", ""),
      duality = data.pop("duality", None),
      cols = data,
    )

  def to_dict(self) -> dict:
    '''Export dictionary representation of the colour palette.'''

    return vars(self)

  def to_css(self) -> str:
    '''Export CSS representation of the colour palette.'''

    styles = [
      f"--col-{key}: {col};"
      for key, col in self.cols.items()
    ]

    return f'''
/* {self.name}
 * {self.ver}
 * {self.desc}
 */
.{self.shard} {{
  {"\n  ".join(styles)}
}}
'''.strip()

  def to_scss(self) -> str:
    '''Export SCSS representation of the colour palette.'''

    styles = [
      f"$col-{key}: {col};"
      for key, col in self.cols.items()
    ]

    return f'''
      /// {self.name}
{"\n".join(styles)}
    '''.strip()
  
  @ staticmethod
  def export_css(palettes: Iterable[Palette]) -> str:
    '''Generate the CSS representation for the provided colour palettes.'''

    return "\n\n".join(each.to_css() for each in palettes)

  @ staticmethod
  def export_js(palettes: Iterable[Palette]) -> str:
    '''Generate the JS representation for the provided colour palettes.'''

    data = [each.to_dict() for each in palettes]
    text = json.dumps(data, indent = 2)
    out = re.sub(r"\"([^-\n]*?)\":", r"\1:", text)
    return out
