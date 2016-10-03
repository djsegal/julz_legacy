"""The test command."""

from .base import *

class Test(Base):
  """Test Julia code"""

  def run(self):
    juliaCall = 'julia -L ./test/test_helper.jl -e \''
    juliaCall += 'using .TestHelper; TestHelper.main();\''

    call(juliaCall, shell=True)
