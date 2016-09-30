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

  def makeAppDir(this, baseDir):
    this.printHeader("app directory")
    this.makeSubDir(baseDir)

  def makeBaseDirs(this, nestedDirs, baseDir):
    this.printHeader("base directories")
    for nestedDir in nestedDirs.values():
      this.makeSubDir(nestedDir)

  def makeStandardSubDirs(this, appDirsList, standardNestedList, nestedDirs):
    this.printHeader("standard sub directories")
    lastItem = standardNestedList[-1]

    for nestedDir in standardNestedList:
      print "  + %s" % this.getLastChunk(nestedDir)
      appDirs = { d: '/'.join([nestedDirs[nestedDir], d]) for d in appDirsList }
      for appDir in appDirs.values():
        this.makeSubDir(appDir, 2)
      if nestedDir != lastItem: print ""

  def makeSpecialSubDirs(this, specialNestedList, nestedDirs):
    this.printHeader("special sub directories")
    for nestedDir in specialNestedList:
      print "  + %s" % this.getLastChunk(nestedDir)

      if nestedDir == 'config':
        this.makeConfigFolder(nestedDirs)
      else:
        print "\n%s not implemented yet.\n" % nestedDir
        return

  def makeConfigFolder(this, nestedDirs):
    configDir = nestedDirs['config']

    applicationFile = this.openFile(configDir, 'application.jl')
    env = jinja2.Environment(loader=jinja2.PackageLoader('app', 'templates'))
    template = env.get_template('application.jl')

    applicationFile.write( template.render(name='John Doe') )
    applicationFile.close()

    this.openFile(configDir, 'environment.jl', True)

    environmentsDir = '/'.join([configDir, 'environments'])
    this.makeSubDir(environmentsDir, 2)

    defaultEnvironments = 'development test production'.split()
    for curEnvironment in defaultEnvironments:
      this.openFile(environmentsDir, '%s.jl' % curEnvironment, True, 3)
    print ""

  def makeSubDir(this, subDir, depth=1):
    makedirs(subDir)
    this.openFile(subDir, '.keep', True, 2, False)
    this.printBullet(this.getLastChunk(subDir), depth)

  def getLastChunk(this, curItem):
    if ( '/' not in curItem ) : return curItem
    return curItem.rsplit('/', 1)[-1]

  def printHeader(this, header):
    print "\nMaking %s:" % header

  def openFile(this, curDir, curFile, autoClose=False, depth=2, verbose=True):
    openedFile = open('/'.join([curDir, curFile]), 'a')
    if verbose: this.printBullet(this.getLastChunk(curFile), depth)
    if not autoClose : return openedFile
    openedFile.close()

  def printBullet(this, bullet, depth):
    bulletSymbol = '-' if '.jl' in bullet else '+'
    prefix = '  ' * depth + bulletSymbol + ' '
    print "%s%s" % ( prefix, bullet )
