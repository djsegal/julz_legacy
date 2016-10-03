"""The base command."""

import jinja2

import re

import inflect

from os import makedirs, path, remove, stat

from subprocess import call

from shutil import rmtree

class Base(object):
  """A base command."""

  def __init__(self, options, *args, **kwargs):
    self.options = options
    self.args = args
    self.kwargs = kwargs

    pathParam = '--path'
    self.baseDir = './' if not self.isPresentParam(pathParam) \
      else self.getRelativePath(pathParam)

    if self.isPresentParam('<app_path>'):
      self.baseDir += self.options['<app_path>']

    self.standardNestedList = 'app test'.split()
    self.shallowNestedList = 'vendor tmp lib'.split()
    self.specialNestedList = 'config test'.split()

    self.nestedDirsList = set( self.standardNestedList +
      self.specialNestedList + self.shallowNestedList )

    self.nestedDirs = { d: '/'.join([self.baseDir, d]) for d in self.nestedDirsList }

    self.appDirsList = 'functions types methods macros'.split()

  def run(self):
    print '\n This method has not been implemented yet.\n'
    return

  def openFile(self, curDir, curFile, autoClose=False, depth=2, verbose=True):
    fileName = '%s/%s' % (curDir, curFile)
    curSuffix = ''

    if not self.isEmptyFile(fileName):
      print "\nThere is already a file named \"%s\". " % fileName
      inputText = "Overwrite? (enter 'h' for help) [Ynaqdh] "
      overwriteOption = raw_input(inputText)
      self.eraseLines(3)

      overwriteFile = overwriteOption.strip()[0].lower() == 'y'
      if overwriteFile:
        curSuffix += " (overwritten)"
        remove(fileName)
      else:
        curSuffix += " (skipped)"
        if verbose: self.printBullet(self.getLastChunk(fileName) + curSuffix, depth)
        return False

    openedFile = open(fileName, 'a')
    if verbose: self.printBullet(self.getLastChunk(fileName) + curSuffix, depth)
    if not autoClose : return openedFile
    openedFile.close()

  def makeSubDir(self, subDir, depth=1):
    makedirs(subDir)
    self.openFile(subDir, '.keep', True, 2, False)
    self.printBullet(self.getLastChunk(subDir), depth)

  def getLastChunk(self, curItem):
    if ( '/' not in curItem ) : return curItem
    return curItem.rsplit('/', 1)[-1]

  def printHeader(self, header, curAction='Making'):
    print "\n%s %s:" % (curAction, header)

  def printBullet(self, bullet, depth=1):
    bulletSymbol = '-' if '.jl' in bullet else '+'
    prefix = '  ' * depth + bulletSymbol + ' '
    print "%s%s" % ( prefix, bullet )

  def getRelativePath(self, pathParam):
    relativePath = self.options[pathParam]
    if relativePath.endswith('/'): return relativePath
    return "%s/" % relativePath

  def isPresentParam(self, param):
    if param not in self.options: return False
    if self.options[param] == None: return False
    return True

  def pluralize(self, word):
    if inflect.engine().singular_noun(word): return word
    return inflect.engine().plural(word)

  def singularize(self, word):
    singularWord = inflect.engine().singular_noun(word)
    if singularWord: return singularWord
    return word

  def loadTemplate(self, templateName, suffix=".jl"):
    env = jinja2.Environment(loader=jinja2.PackageLoader('app', 'templates'))
    template = env.get_template('%s%s' % (templateName, suffix))
    return template

  def isEmptyFile(self, fileName):
    if not path.isfile(fileName): return True
    return stat(fileName).st_size == 0

  def eraseLines(self, numLines=1):
    cursorUpOne = '\x1b[1A'
    eraseLine = '\x1b[2K'

    compositeErase = cursorUpOne + eraseLine
    print(compositeErase * numLines + cursorUpOne)
