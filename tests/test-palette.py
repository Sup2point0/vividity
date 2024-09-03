from scripts.classes.palette import Palette


DATA = {
  "name": "Test",
  "shard": "test",
  "ver": "2.0",
  "desc": "testing",
  "duality": "light",

  "prot": "0",
  "text": "1",
  "text-deut": "2",
  "back": "3",
  "back-deut": "4",
  "link": "5",
  "link-hover": "6",
}


def test_init():
  p = Palette(name = "Test")

  assert p.name == "Test"


def test_init_from_json():
  p = Palette.from_json(DATA)

  assert p.shard == "test"
  assert p.name == "Test"
  assert p.desc == "testing"
  assert p.duality == "light"

  assert p.cols["prot"] == "0"
  assert p.cols["text"] == "1"


def test_to_css(route):
  p = Palette.from_json(DATA)

  with open(route / "out" / "test.css", "w") as dest:
    dest.write(p.to_css())


def test_to_scss(route):
  p = Palette.from_json(DATA)

  with open(route / "out" / "test.scss", "w") as dest:
    dest.write(p.to_scss())


def test_export_css(route):
  p = [
    Palette.from_json(DATA),
    Palette.from_json(DATA)
  ]

  with open(route / "out" / "tests.css", "w") as dest:
    dest.write(Palette.export_css(p))


def test_export_js(route):
  p = [
    Palette.from_json(DATA),
    Palette.from_json(DATA)
  ]

  with open(route / "out" / "tests.js", "w") as dest:
    dest.write(Palette.export_js(p))
