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

      suffix = ''
      templateName = '/'.join([nestedDir, self.singularize(curGenerator)])
      if nestedDir == 'test':
        suffix += '_test'
        templateName += '_test'

      curFile = self.openFile(fileName, curName + suffix + '.jl', False, 3)
      if not curFile:
        print ''
        continue

      templateVariables = { 'name': curName }
      if nestedDir == 'app':
        curFields = self.options['<field>']
        for i in range(len(curFields)):
          splitField = curFields[i].split(':')
          if len(splitField) > 1:
            splitField[1:] = [ x.title() for x in splitField[1:] ]
          curFields[i] = '::'.join(splitField)

        templateVariables['fields'] = curFields

      template = self.loadTemplate(templateName)

      curFile.write( template.render(templateVariables) )

      curFile.close()
      print ''
