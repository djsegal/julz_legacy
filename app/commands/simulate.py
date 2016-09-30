"""The simulate command."""

from .base import *

class Simulate(Base):
  """Run Julia code"""

  def run(self):
    call(["julia", "./config/application.jl"])
