from pathlib import Path

import pytest


ROUTE = Path(__file__).parent


@ pytest.fixture(scope = "module")
def route():
  return ROUTE
