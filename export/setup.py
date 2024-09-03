import argparse


def setup_parser():
  parser = argparse.ArgumentParser(
    prog = "Vividity",
    description = "Provides automation for exporting Vividity colour palettes."
  )

  parser.add_argument("--root",
    action = "store",
    default = "",
  )
  parser.add_argument("--css",
    action = "store",
  )
  parser.add_argument("--scss",
    action = "store",
  )
  parser.add_argument("--js",
    action = "store",
  )

  parser.add_argument("flags",
    action = "store",
    nargs = "*"
  )

  return parser
