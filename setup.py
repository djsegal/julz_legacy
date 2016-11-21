"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from app import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
  long_description = file.read()


class RunTests(Command):
  """Run all tests."""
  description = 'run tests'
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    """Run all tests!"""
    errno = call(['py.test', '--cov=app', '--cov-report=term-missing'])
    raise SystemExit(errno)

setup(
  name = 'julz',
  version = __version__,
  description = 'A command line utility for creating ambitious julia apps.',
  long_description = long_description,
  url = 'https://github.com/djsegal/julz',
  author = 'dan segal',
  license = 'UNLICENSE',
  classifiers = [
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    'License :: Public Domain',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
  ],
  keywords = 'cli',
  packages = find_packages(exclude=['docs', 'tests*']),
  package_data={'': ['templates/*', 'templates/**/*']},
  install_requires = ['docopt', 'jinja2', 'inflect'],
  extras_require = {
    'test': ['coverage', 'pytest', 'pytest-cov'],
  },
  entry_points = {
    'console_scripts': [
      'julz=app.cli:main',
    ],
  },
  cmdclass = {'test': RunTests},
)
