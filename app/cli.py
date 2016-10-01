"""
julz

Usage:
  julz new <app_path> [options]
  julz scrap <app_path> [options]
  julz generate <generator> <name> [<field>...] [options]
  julz destroy <generator> <name> [<field>...] [options]
  julz run [options]
  julz test [options]
  julz send [options]
  julz install [options]
  julz update [options]
  julz hello
  julz -h | --help
  julz --version
  julz g <generator> <name> [<field>...] [options]
  julz d <generator> <name> [<field>...] [options]
  julz r [options]
  julz t [options]
  julz s [options]
  julz i [options]
  julz u [options]

Options:
  -f --force                        Overwrite files that already exist
  -h --help                         Show this screen.
  --version                         Show version.
  --path=<path>                     Relative path to use for julia project

Examples:
  julz hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/djsegal/julz
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
  """Main CLI entrypoint."""
  import commands
  options = docopt(__doc__, version=VERSION)

  # Here we'll try to dynamically match the command the user is trying to run
  # with a pre-defined command class we've already created.
  for k, v in options.iteritems():
    if hasattr(commands, k) and v:
      module = getattr(commands, k)
      commands = getmembers(module, isclass)
      command = [command[1] for command in commands if command[0] != 'Base'][0]
      command = command(options)
      command.run()
