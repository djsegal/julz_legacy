"""The run command."""

from .base import *

class Run(Base):
  """Run Julia code"""

  def run(self):
    call('julia -L ./config/application.jl -e "Application.main();"', shell=True)
