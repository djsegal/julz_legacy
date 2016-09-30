"""The base command."""

import jinja2

import re

from os import makedirs, path

from shutil import rmtree

class Base(object):
  """A base command."""

  def __init__(self, options, *args, **kwargs):
    self.options = options
    self.args = args
    self.kwargs = kwargs

  def run(self):
    raise NotImplementedError('You must implement the run() method yourself!')

  def openFile(self, curDir, curFile, autoClose=False, depth=2, verbose=True):
    openedFile = open('/'.join([curDir, curFile]), 'a')
    if verbose: self.printBullet(self.getLastChunk(curFile), depth)
    if not autoClose : return openedFile
    openedFile.close()

  def makeSubDir(self, subDir, depth=1):
    makedirs(subDir)
    self.openFile(subDir, '.keep', True, 2, False)
    self.printBullet(self.getLastChunk(subDir), depth)

  def getLastChunk(self, curItem):
    if ( '/' not in curItem ) : return curItem
    return curItem.rsplit('/', 1)[-1]

  def printHeader(self, header):
    print "\nMaking %s:" % header

  def printBullet(self, bullet, depth=1):
    bulletSymbol = '-' if '.jl' in bullet else '+'
    prefix = '  ' * depth + bulletSymbol + ' '
    print "%s%s" % ( prefix, bullet )

  def getRelativePath(self):
    pathParam = '--path'
    if pathParam not in self.options: return './'

    relativePath = self.options[pathParam]
    if relativePath.endswith('/'): return relativePath
    return "%s/" % relativePath
