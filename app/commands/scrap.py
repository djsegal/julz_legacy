"""The scrap command."""

from .base import *

class Scrap(Base):
  """Scrap Julia project"""

  def run(self):
    if not path.exists(self.baseDir):
      print "Project '%s' doesn't exist" % self.options['<app_path>']
      return

    if not self.options['--force']:
      print "'--force' is required for this command"
      return

    rmtree(self.baseDir)
