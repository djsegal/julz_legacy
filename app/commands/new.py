"""The new command."""

import jinja2

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
          raise "There is already a project named \"%s\"." % self.options['APP_PATH']

      self.makeSubDir(baseDir)
      mainFile = open('/'.join([baseDir, 'main.jl']), 'a')

      env = jinja2.Environment(loader=jinja2.PackageLoader('app', 'templates'))
      template = env.get_template('main.jl')

      mainFile.write( template.render(name='John Doe') )

      mainFile.close()

      nestedDirsList = 'test app'.split()
      nestedDirs = { d: '/'.join([baseDir, d]) for d in nestedDirsList }
      for nestedDir in nestedDirs.values():
        self.makeSubDir(nestedDir)

      appDirsList = 'helpers functions types methods modules'.split()

      for nestedDir in nestedDirs.keys():
        appDirs = { d: '/'.join([nestedDirs[nestedDir], d]) for d in appDirsList }
        for appDir in appDirs.values():
          self.makeSubDir(appDir)

    def makeSubDir(this, subDir):
      makedirs(subDir)
      open('/'.join([subDir, '.keep']), 'a').close()
