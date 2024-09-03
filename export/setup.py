import argparse


def setup_parser():
  parser = argparse.ArgumentParser(
    prog = "Vividity",
    description = "Provides automation for exporting Vividity colour palettes."
  )

  parser.add_argument("route", default = "TEST")

  parser.add_argument("--css",
    action = "store",
    default = "palettes.css",
  )
  parser.add_argument("--scss",
    action = "store",
    default = "palettes.scss",
  )
  parser.add_argument("--js",
    action = "store",
    default = "palettes.js",
  )

  return parser
