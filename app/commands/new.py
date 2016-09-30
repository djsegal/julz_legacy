"""The new command."""

from .base import *

class New(Base):
  """Start new Julia project"""

  def run(self):
    if path.exists(self.baseDir):
      if self.options['--force']:
        rmtree(self.baseDir)
      else:
        print "There is already a project named \"%s\"." % self.options['<app_path>']
        return

    self.makeAppDir()
    self.makeBaseDirs()
    self.makeStandardSubDirs()
    self.makeSpecialSubDirs()

  def makeAppDir(self):
    self.printHeader("app directory")
    self.makeSubDir(self.baseDir)

  def makeBaseDirs(self):
    self.printHeader("base directories")
    for nestedDir in self.nestedDirs.values():
      self.makeSubDir(nestedDir)

  def makeStandardSubDirs(self):
    self.printHeader("standard sub directories")
    lastItem = self.standardNestedList[-1]

    for nestedDir in self.standardNestedList:
      self.printBullet(self.getLastChunk(nestedDir))
      appDirs = { d: '/'.join([self.nestedDirs[nestedDir], d]) for d in self.appDirsList }
      for appDir in appDirs.values():
        self.makeSubDir(appDir, 2)
      if nestedDir != lastItem: print ""

  def makeSpecialSubDirs(self):
    self.printHeader("special sub directories")
    for nestedDir in self.specialNestedList:
      self.printBullet(self.getLastChunk(nestedDir))

      if nestedDir == 'config':
        self.makeConfigFolder()
      else:
        print "\n%s not implemented yet.\n" % nestedDir
        return

  def makeConfigFolder(self):
    configDir = self.nestedDirs['config']
    self.makeApplicationModule(configDir)
    self.makeEnvironmentFiles(configDir)
    print ""

  def makeApplicationModule(self, configDir):
    applicationFile = self.openFile(configDir, 'application.jl')
    if not applicationFile: return

    template = self.loadTemplate('application')
    applicationFile.write( template.render() )
    applicationFile.close()

  def makeEnvironmentFiles(self, configDir):
    self.openFile(configDir, 'environment.jl', True)
    environmentsDir = '/'.join([configDir, 'environments'])
    self.makeSubDir(environmentsDir, 2)

    defaultEnvironments = 'development test production'.split()
    for curEnvironment in defaultEnvironments:
      self.openFile(environmentsDir, '%s.jl' % curEnvironment, True, 3)
