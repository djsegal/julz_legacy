"""The destroy command."""

from .base import *

class Destroy(Base):
  """Destroy Julia files"""

  def run(self):
    curGenerator = self.pluralize(self.options['<generator>'])
    curName = self.options['<name>']

    if curGenerator not in self.appDirsList:
      print "\n%s has no valid generator.\n" % curGenerator
      return

    self.printHeader("%s files for '%s'" % (self.singularize(curGenerator), curName), 'Deleting')
    print ''

    for nestedDir in self.standardNestedList:
      self.printBullet(self.getLastChunk(nestedDir))
      curDir = nestedDir + "/%s" % curGenerator
      self.printBullet(self.getLastChunk(curDir), 2)
      fileName = self.baseDir + curDir

      if nestedDir == 'test':
        curName += '_test'

      curFile = '%s/%s/%s.jl' % (self.baseDir, curDir, curName)
      curSuffix = " (didn't exist)"
      if path.isfile(curFile):
        curSuffix = " (deleted)"
        remove(curFile)

      self.printBullet(self.getLastChunk(curFile) + curSuffix, 3)
      print ''
