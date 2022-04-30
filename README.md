# GitLab Kanban Board Command Line Interface

This project provides and command line interface for generating and manipulating Kanban boards on GitLab.It was built to help teams setting up their initial Kanban board with consistent labels and lists. It also has the ability to create stories that track assets.

It was originally created to help content creators track assets for training videos. Each video required a script, slides, lab, and the video itself. All of these assets were created by different people and it got very tedious creating 4 stories for every video to track the 4 assets. This CLI has the ability to specify the story once, and it will automatically create a card for each assets independently.

## Installation

```bash
pip install gitlab-kanban
```

## Usage

You should set the following environment variables so that you don't have to specify them on the command line. This is particularly convenient when working in the same project for a while.


| Parameter| Variable | Description |
|-------|----------|-------------|
| -t/--token | GITLAB_TOKEN | You GitLab authorization token |
| -p/--project | GITLAB_PROJECT | The unique ID for your GitLab project |
| -u/--url | GETLAB_URL | The GitLab url if not the default https://gitlab.com |

By setting those environment variables you can eliminate the need for using `-t`, `-p` on every call.

You can us the `--help` flag to get help on all of the commands.

```text
$ kanban --help

Usage: kanban [OPTIONS] COMMAND [ARGS]...

  GitLab Kanban Board Command Line Interface

Options:
  -t, --token TEXT       GitLab authorization token or set env GITLAB_TOKEN
                         [required]
  -p, --project TEXT     The GitLab project ID or set env GITLAB_PROJECT
                         [required]
  -u, --gitlab-url TEXT  GitLab URL (defaults to https://gitlab.com)
  --help                 Show this message and exit.

Commands:
  create  Creates labels, lists, and issues from a CSV file
  get     Gets labels, lists, and issues for a project
```

Each command has a series of subcommands to create the various artifacts.

### Create command help

```text
$ kanban create --help

Usage: kanban create [OPTIONS] COMMAND [ARGS]...

  Creates labels, lists, and issues from a CSV file

Options:
  --help  Show this message and exit.

Commands:
  issues  Creates issues for a project from a CVS file
  labels  Creates labels for a project from a CVS file
  lists   Creates kanban board lists for a project from a CVS file
```

### Get command help

```text
$ kanban get --help

Usage: kanban get [OPTIONS] COMMAND [ARGS]...

  Gets labels, lists, and issues for a project

Options:
  --help  Show this message and exit.

Commands:
  issues  Returns all of the issues for a project
  labels  Returns all of the labels for a project
  lists   Returns all of the kanban board lists for a project
```

## Development setup

You can create a development environment using a Python virtual environment (`venv`) and `pip` 

```bash
python3 -m venv .venv
source .env/bin/activate
pip install -e '.[dev]'
```
