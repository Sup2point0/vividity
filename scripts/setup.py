import argparse


def setup_parser():
  parser = argparse.ArgumentParser(
    prog = "Vividity",
    description = "Provides automation for exporting Vividity colour palettes."
  )

  parser.add_argument("--js",
    action = "store",
    default = "palettes.js",
  )
  parser.add_argument("--css")

  return parser
