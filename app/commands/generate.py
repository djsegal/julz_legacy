"""The generate command."""

from .base import *

class Generate(Base):
  """Generate Julia files"""

  def run(self):
    for nestedDir in self.standardNestedList:
      self.printBullet(self.getLastChunk(nestedDir))
      nestedDir += "/%s" % self.pluralize(self.options['<generator>'])
      self.printBullet(self.getLastChunk(nestedDir), 2)
      self.openFile(self.baseDir + nestedDir, '%s.jl' % self.options['<name>'], True, 3)
