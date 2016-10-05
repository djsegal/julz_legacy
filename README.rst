+-----------------------------------------------------------------+----------+
|                                                                 |          |
| **julz**                                                        |          |
|                                                                 |  |julz|  |
| *A command line utility for creating scalable julia apps.*      |          |
|                                                                 |          |
+-----------------------------------------------------------------+----------+

-------------------------

Instillation
~~~~~~~~~~~~

::

   pip install julz

Usage
~~~~~

+-------------------------------------------------------------------+---------------------------------------------+
| Command                                                           | Description                                 |
+===================================================================+=============================================+
| ``julz new <app_path> [options]``                                 | Start new project                           |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz scrap <app_path> [options]``                               | Scrap old project                           |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (i|install) [options]``                                    | Install Julia packages                      |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (u|update) [options]``                                     | Update Julia packages                       |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (g|generate) <generator> <name> [<field>...] [options]``   | Generate Julia file                         |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (d|destroy) <generator> <name> [<field>...] [options]``    | Destroy Julia file                          |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (r|run) [options]``                                        | Run Julia code                              |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (t|test) [options]``                                       | Test Julia code                             |
+-------------------------------------------------------------------+---------------------------------------------+
| ``julz (s|send) [options]``                                       | Send Julia code elsewhere (unimplemented)   |
+-------------------------------------------------------------------+---------------------------------------------+

Project Architecture
~~~~~~~~~~~~~~~~~~~~

-  ``./``
  +  ``README.md``
  +  ``Gemfile``
  +  ``Gemfile.lock``
  +  ``lib``
  +  ``tmp``
  +  ``vendor``
  +  ``config``

    -  ``initializers``
    -  ``application.jl``
    -  ``include_all.jl``
    -  ``export_all_except.jl``
    -  ``environment.jl``
    -  ``environments``
      +  ``development.jl``
      +  ``test.jl``
      +  ``production.jl``

  +  ``app``

    -  ``functions``
    -  ``methods``
    -  ``types``
    -  ``macros``

  +  ``test``

    -  ``test_helper.jl``
    -  ``functions``
    -  ``methods``
    -  ``types``
    -  ``macros``

.. |julz| image:: https://raw.githubusercontent.com/djsegal/julz/master/julz_logo.png
