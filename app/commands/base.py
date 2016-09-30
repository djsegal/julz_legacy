"""The base command."""


class Base(object):
  """A base command."""

  def __init__(self, options, *args, **kwargs):
    self.options = options
    self.args = args
    self.kwargs = kwargs

  def run(self):
    raise NotImplementedError('You must implement the run() method yourself!')

  def getRelativePath(self):
    pathParam = '--path'
    if pathParam not in self.options: return './'

    relativePath = self.options[pathParam]
    if relativePath.endswith('/'): return relativePath
    return "%s/" % relativePath
