"""The generate command."""

from .base import *

class Generate(Base):
  """Generate Julia files"""

  def run(self):
    curGenerator = self.pluralize(self.options['<generator>'])
    curName = self.options['<name>']

    if curGenerator not in self.appDirsList:
      print "\n%s has no valid generator.\n" % curGenerator
      return

    self.printHeader("%s files for '%s'" % (self.singularize(curGenerator), curName))
    print ''

    for nestedDir in self.standardNestedList:
      self.printBullet(self.getLastChunk(nestedDir))
      curDir = nestedDir + "/%s" % curGenerator
      self.printBullet(self.getLastChunk(curDir), 2)
      fileName = self.baseDir + curDir

      templateName = '/'.join([nestedDir, self.singularize(curGenerator)])
      if nestedDir == 'test':
        curName += '_test'
        templateName += '_test'

      curFile = self.openFile(fileName, curName + '.jl', False, 3)
      if not curFile:
        print ''
        continue

      template = self.loadTemplate(templateName)

      curFile.write( template.render(name='John Doe') )

      curFile.close()
      print ''
