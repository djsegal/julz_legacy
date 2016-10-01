"""The update command."""

from .base import *

class Update(Base):
  """Update Julia package(s)"""

  def run(self):
    self.printHeader('gems', 'Updating')
    print ''

    call('julia -e "Pkg.update()"', shell=True)
