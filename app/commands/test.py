"""The test command."""

from .base import *

class Test(Base):
  """Test Julia code"""

  def run(self):
    call(["julia", "./test/test_helper.jl"])
