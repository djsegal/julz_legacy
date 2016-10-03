"""The test command."""

from .base import *

class Test(Base):
  """Test Julia code"""

  def run(self):
    juliaCall = 'julia -L ./test/test_helper.jl -e \''
    juliaCall += 'include("./config/application.jl"); '
    juliaCall += 'using .Application; using Base.Test; '
    juliaCall += 'TestHelper.main();\''

    call(juliaCall, shell=True)
