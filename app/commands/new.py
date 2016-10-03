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
    self.makeGemfile()
    self.makeBaseDirs()
    self.makeStandardSubDirs()
    self.makeSpecialSubDirs()

  def makeAppDir(self):
    self.printHeader("app directory")
    self.makeSubDir(self.baseDir)

    readme = self.openFile(self.baseDir, 'README.md')
    if not readme: return

    template = self.loadTemplate('README.md', '')
    readme.write( template.render({ 'name': self.options['<app_path>'] }) )
    readme.close()

  def makeGemfile(self):
    self.printHeader("gemfile")
    self.openFile(self.baseDir, 'Gemfile.lock', True)

    gemfile = self.openFile(self.baseDir, 'Gemfile')
    if not gemfile: return

    template = self.loadTemplate('Gemfile', '')
    gemfile.write( template.render() )
    gemfile.close()

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
      elif nestedDir == 'test':
        self.makeTestHelperModule()
      else:
        print "\n%s not implemented yet.\n" % nestedDir
        return

  def makeConfigFolder(self):
    configDir = self.nestedDirs['config']

    initializersDir = '/'.join([configDir, 'initializers'])
    self.makeSubDir(initializersDir, 2)

    configFiles = 'application include_all export_all_except'.split()
    for curFileName in configFiles:
      self.makeConfigFile(configDir, curFileName)

    self.makeEnvironmentFiles(configDir)
    print ""

  def makeConfigFile(self, configDir, curFileName):
    configFile = self.openFile(configDir, '%s.jl' % curFileName)
    if not configFile: return

    template = self.loadTemplate('config/%s' % curFileName)
    configFile.write( template.render() )
    configFile.close()

  def makeEnvironmentFiles(self, configDir):
    self.openFile(configDir, 'environment.jl', True)
    environmentsDir = '/'.join([configDir, 'environments'])
    self.makeSubDir(environmentsDir, 2)

    defaultEnvironments = 'development test production'.split()
    for curEnvironment in defaultEnvironments:
      self.openFile(environmentsDir, '%s.jl' % curEnvironment, True, 3)

  def makeTestHelperModule(self):
    testDir = self.nestedDirs['test']
    testHelperFile = self.openFile(testDir, 'test_helper.jl')
    if not testHelperFile: return

    template = self.loadTemplate('test/test_helper')
    testHelperFile.write( template.render() )
    testHelperFile.close()
