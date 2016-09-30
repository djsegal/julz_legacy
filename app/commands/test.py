"""The test command."""

from .base import *

class Test(Base):
  """Run Julia code"""

  def run(self):
    call(["julia", "./test/test_helper.jl"])
