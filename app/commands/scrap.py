"""The scrap command."""

from .base import *

class Scrap(Base):
  """Scrap Julia project"""

  def run(self):
    if not path.exists(self.baseDir):
      print "\n Project '%s' doesn't exist\n" % self.options['<app_path>']
      return

    if not self.options['--force']:
      print "\n '--force' is required for this command\n"
      return

    self.printHeader("app directory", " Deleting")
    rmtree(self.baseDir)
    print("\n ...and done.\n")
