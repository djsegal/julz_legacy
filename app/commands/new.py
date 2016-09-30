"""The new command."""

import jinja2

import re

from json import dumps

from .base import Base

from os import makedirs, path

from shutil import rmtree

class New(Base):
  """Start new Julia project"""

  def run(self):
    baseDir = self.options['APP_PATH']

    if path.exists(baseDir):
      if self.options['--force']:
        rmtree(baseDir)
      else:
        print "There is already a project named \"%s\"." % self.options['APP_PATH']
        return

    self.makeAppDir(baseDir)

    standardNestedList = 'app test'.split()
    shallowNestedList = 'vendor tmp lib'.split()
    specialNestedList = 'config'.split()

    nestedDirsList = standardNestedList + specialNestedList + shallowNestedList
    nestedDirs = { d: '/'.join([baseDir, d]) for d in nestedDirsList }

    appDirsList = 'functions types methods'.split()

    self.makeBaseDirs(nestedDirs, baseDir)
    self.makeStandardSubDirs(appDirsList, standardNestedList, nestedDirs)
    self.makeSpecialSubDirs(specialNestedList, nestedDirs)

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
      print "  + %s" % self.getLastChunk(nestedDir)
      appDirs = { d: '/'.join([nestedDirs[nestedDir], d]) for d in appDirsList }
      for appDir in appDirs.values():
        self.makeSubDir(appDir, 2)
      if nestedDir != lastItem: print ""

  def makeSpecialSubDirs(self, specialNestedList, nestedDirs):
    self.printHeader("special sub directories")
    for nestedDir in specialNestedList:
      print "  + %s" % self.getLastChunk(nestedDir)

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

  def makeSubDir(self, subDir, depth=1):
    makedirs(subDir)
    self.openFile(subDir, '.keep', True, 2, False)
    self.printBullet(self.getLastChunk(subDir), depth)

  def getLastChunk(self, curItem):
    if ( '/' not in curItem ) : return curItem
    return curItem.rsplit('/', 1)[-1]

  def printHeader(self, header):
    print "\nMaking %s:" % header

  def openFile(self, curDir, curFile, autoClose=False, depth=2, verbose=True):
    openedFile = open('/'.join([curDir, curFile]), 'a')
    if verbose: self.printBullet(self.getLastChunk(curFile), depth)
    if not autoClose : return openedFile
    openedFile.close()

  def printBullet(self, bullet, depth):
    bulletSymbol = '-' if '.jl' in bullet else '+'
    prefix = '  ' * depth + bulletSymbol + ' '
    print "%s%s" % ( prefix, bullet )
