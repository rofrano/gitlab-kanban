# GitLab Kanban Board Command Line Interface

This project provides and command line interface for generating and manipulating Kanban boards on GitLab.It was built to help teams setting up their initial Kanban board with consistent labels and lists. It also has the ability to create stories that track assets.

It was originally created to help content creators track assets for training videos. Each video required a script, slides, lab, and the video itself. All of these assets were created by different people and it got very tedious creating 4 stories for every video to track the 4 assets. This CLI has the ability to specify the story once, and it will automatically create a card for each assets independently.

## Installation

```bash
pip install gitlab-kanban
```

## Usage

You can us the `--help` flag to get help on all of the commands.

```bash
kanban --help

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
  create  Creates labels, lists, and issues
  get     Gets labels, lists, and issues
```

## Contributing

You can create a development environment using a Python virtual environment (`venv`) and `pip` 

```bash
python3 -m venv .venv
source .env/bin/activate
pip install -e '.[dev]'
```
