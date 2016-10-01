"""The install command."""

from .base import *

class Install(Base):
  """Install Julia package(s)"""

  def run(self):
    self.printHeader('gems', 'Installing')
    print ''

    f = open('./Gemfile', 'r')
    for line in f:
      line = line.strip().replace('"', '')
      splitLine = line.split()

      if len(splitLine) == 0 or splitLine[0] != 'gem': continue
      splitLine.pop(0)

      if len(splitLine) > 1:
        print("Versioning is not currently implemented")
        return

      curGem = splitLine[0]
      self.printBullet(curGem)
      call("julia -e 'Pkg.add(\"%s\")'" % curGem, shell=True)
      self.eraseLines()

    print ''
