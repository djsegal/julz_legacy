"""The generate command."""

from json import dumps

from .base import Base

class Generate(Base):
  """Generate julia files"""

  def run(self):
    print 'Hello, world!'
    print 'You supplied the following options:', dumps(self.options, indent=2, sort_keys=True)
