![julz](https://raw.githubusercontent.com/djsegal/julz/master/julz_logo.png) | ***A command line utility for creating ambitious julia apps.***
--- | --------

---------------

### Usage

---------------

| Command  | Description |
| ------------- | ------------- |
| `julz new <app_path> [options]` | Start new project |
| `julz scrap <app_path> [options]` | Scrap old project |
| `julz (i|install) [options]` | Install Julia packages |
| `julz (u|update) [options]` | Update Julia packages |
| `julz (g|generate) <generator> <name> [<field>...] [options]` | Generate Julia file |
| `julz (d|destroy) <generator> <name> [<field>...] [options]` | Destroy Julia file |
| `julz (r|run) [options]` | Run Julia code |
| `julz (t|test) [options]` | Test Julia code |
| `julz (s|send) [options]` | Send Julia code elsewhere (unimplemented) |

---------------

### Project Architecture

---------------

- `./`
  - `Gemfile`
  - `Gemfile.lock`
  - `lib`
  - `tmp`
  - `vendor`
  - `config`
    - `application.jl`
    - `environment.jl`
    - `environments`
      - `development.jl`
      - `test.jl`
      - `production.jl`
  - `app`
    - `functions`
    - `methods`
    - `types`
  - `test`
    - `test_helper.jl`
    - `functions`
    - `methods`
    - `types`

---------------

### Todo

- [ ] Fill out Todo List
