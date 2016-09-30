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

    self.makeAppDir(self.baseDir)

    self.makeBaseDirs(self.nestedDirs, self.baseDir)
    self.makeStandardSubDirs(self.appDirsList, self.standardNestedList, self.nestedDirs)
    self.makeSpecialSubDirs(self.specialNestedList, self.nestedDirs)

  def makeAppDir(self, baseDir):
    self.printHeader("app directory")
    self.makeSubDir(baseDir)

  def makeBaseDirs(self, nestedDirs, baseDir):
    self.printHeader("base directories")
    for nestedDir in nestedDirs.values():
      self.makeSubDir(nestedDir)

  def makeStandardSubDirs(self, appDirsList, standardNestedList, nestedDirs):
    self.printHeader("standard sub directories")
    lastItem = standardNestedList[-1]

    for nestedDir in standardNestedList:
      self.printBullet(self.getLastChunk(nestedDir))
      appDirs = { d: '/'.join([nestedDirs[nestedDir], d]) for d in appDirsList }
      for appDir in appDirs.values():
        self.makeSubDir(appDir, 2)
      if nestedDir != lastItem: print ""

  def makeSpecialSubDirs(self, specialNestedList, nestedDirs):
    self.printHeader("special sub directories")
    for nestedDir in specialNestedList:
      self.printBullet(self.getLastChunk(nestedDir))

      if nestedDir == 'config':
        self.makeConfigFolder(nestedDirs)
      else:
        print "\n%s not implemented yet.\n" % nestedDir
        return

  def makeConfigFolder(self, nestedDirs):
    configDir = nestedDirs['config']
    self.makeApplicationModule(configDir)
    self.makeEnvironmentFiles(configDir)
    print ""

  def makeApplicationModule(self, configDir):
    applicationFile = self.openFile(configDir, 'application.jl')
    env = jinja2.Environment(loader=jinja2.PackageLoader('app', 'templates'))
    template = env.get_template('application.jl')

    applicationFile.write( template.render(name='John Doe') )
    applicationFile.close()

  def makeEnvironmentFiles(self, configDir):
    self.openFile(configDir, 'environment.jl', True)
    environmentsDir = '/'.join([configDir, 'environments'])
    self.makeSubDir(environmentsDir, 2)

    defaultEnvironments = 'development test production'.split()
    for curEnvironment in defaultEnvironments:
      self.openFile(environmentsDir, '%s.jl' % curEnvironment, True, 3)
