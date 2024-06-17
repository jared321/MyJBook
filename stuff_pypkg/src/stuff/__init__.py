from importlib.metadata import version

__version__ = version("stuff")

from .compute import compute

from .load_tests import load_tests
from .test import test
