"""The test command."""

from .base import *

class Test(Base):
  """Test Julia code"""

  def run(self):
    call('julia -L ./test/test_helper.jl -e "TestHelper.main();"', shell=True)
