from scripts.classes.palette import Palette


def test_init():
  p = Palette(name = "Test")

  assert p.name == "Test"


def test_init_from_json():
  data = {
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

  p = Palette.from_json(data)

  assert p.shard == "test"
  assert p.name == "Test"
  assert p.desc == "testing"
  assert p.duality == "light"

  assert p.cols
