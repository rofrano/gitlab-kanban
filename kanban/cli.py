"""
GitLab Kanban Board Command Line Interface
"""
import csv
import click
import urllib.parse
from tqdm import tqdm
from .models import GitLab


@click.group()
@click.option("-t", "--token", required=True, envvar="GITLAB_TOKEN", help="GitLab authorization token or set env GITLAB_TOKEN")
@click.option("-p", "--project", required=True, envvar="GITLAB_PROJECT", help="The GitLab project ID or set env GITLAB_PROJECT")
@click.option("-u", "--gitlab-url", required=False, envvar="GITLAB_URL", default="https://gitlab.com", help="GitLab URL [optional] defaults to https://gitlab.com")
@click.pass_context
def cli(ctx, token, project, gitlab_url):
    """GitLab Kanban Board Command Line Interface"""
    ctx.ensure_object(dict)
    ctx.obj['PROJECT'] = project
    ctx.obj['GITLAB_TOKEN'] = token
    ctx.obj['GITLAB'] = GitLab(project, token, gitlab_url)
    
######################################################################
# L A B E L S   C O M M A N D S
######################################################################

@cli.group()
@click.pass_context
def labels(ctx):
    """Create, Get, Update, Delete Labels"""

#---------------------------------------------------------------------
# CREATE LABELS
#---------------------------------------------------------------------
@labels.command('create')
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The CSV file with labels")
@click.pass_context
def create_labels(ctx, input):
    """Creates labels for a project from a CVS file"""
    click.echo(f"Creating labels for project {ctx.obj['PROJECT']}...")
    click.echo(f"Processing {input}...")
    labels = csv_to_dict(input)
    click.echo(f"Found {len(labels)} labels...")
    click.echo("Sending to GitLab...")
    gitlab = ctx.obj['GITLAB']
    for entry in tqdm(labels, total=len(labels)):
        results = gitlab.post('labels', entry)
    click.echo("Done")

#---------------------------------------------------------------------
# GET LABELS
#---------------------------------------------------------------------
@labels.command('get')
@click.pass_context
def get_labels(ctx):
    """Returns all of the labels for a project"""
    click.echo(f"Getting labels for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    labels = gitlab.get('labels')
    click.echo(labels)

#---------------------------------------------------------------------
# DELETE LABELS
#---------------------------------------------------------------------
@labels.command('delete')
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The CSV file with labels")
@click.pass_context
def delete_labels(ctx, input):
    """Deletes labels for a project from a CVS file"""
    click.echo(f"Deleting labels for project {ctx.obj['PROJECT']}...")
    click.echo(f"Processing {input}...")
    labels = csv_to_dict(input)
    click.echo(f"Found {len(labels)} labels...")
    click.echo("Sending to GitLab...")
    gitlab = ctx.obj['GITLAB']
    for entry in tqdm(labels, total=len(labels)):
        name = urllib.parse.quote(entry["name"])
        results = gitlab.delete(f'labels/{name}')
    click.echo("Done")




######################################################################
# B O A R D S   C O M M A N D S
######################################################################

@cli.group()
@click.pass_context
def boards(ctx):
    """Create, Get, Update, Delete Kanban Boards"""

#---------------------------------------------------------------------
# GET BOARDS
#---------------------------------------------------------------------
@boards.command('get')
@click.pass_context
def get_boards(ctx):
    """Returns all of the kanban boards for a project"""
    click.echo(f"Getting kanban boards for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    boards = gitlab.get('boards')
    click.echo(boards)

#---------------------------------------------------------------------
# CREATE BOARDS
#---------------------------------------------------------------------
@boards.command('create')
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The CSV file with list labels")
@click.option("--name", "-n", required=True, help="The name of the kanban board")
@click.pass_context
def create_boards(ctx, input, name):
    """Creates kanban board for a project from a CVS file of labels"""
    click.echo(f"Creating kanban board for project {ctx.obj['PROJECT']}...")
    click.echo(f"Processing {input}...")
    gitlab = ctx.obj['GITLAB']
    # generate board
    board = {
        "name": name
    }
    click.echo("Sending to GitLab...")
    results = gitlab.post('boards', board)
    board_id = results["id"]
    board['id'] = board_id
    click.echo(f"Board {board_id} created")
    click.echo(board)

    # Create the labels
    click.echo("Creating labels...")
    labels = csv_to_dict(input)
    click.echo(f"Found {len(labels)} labels...")
    path = f"boards/{board_id}/lists"
    for entry in tqdm(labels, total=len(labels)):
        label = gitlab.post('labels', entry)
        data = { "label_id": label["id"]}
        results = gitlab.post(path, data)

    # Get the new board
    path = f"boards/{board_id}"
    results = gitlab.get(path)
    click.echo(f"New board {name} created")
    click.echo(results)


#---------------------------------------------------------------------
# DELETE BOARDS
#---------------------------------------------------------------------
@boards.command('delete')
@click.option("--name", "-n", required=True, help="The name of the kanban board")
@click.pass_context
def delete_boards(ctx, name):
    """Deletes kanban board from a project"""
    click.echo(f"Deleting kanban board for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    # Find the board
    click.echo(f"Finding board {name}...")
    boards = gitlab.get('boards')
    result = [board for board in boards if board["name"] == name]
    click.echo(f"Deleting board {name}...")
    if result:
        board = result[0]
        click.echo(f"Deleting {board['name']} with ID: {board['id']}")
        results = gitlab.delete(f"boards/{board['id']}")
        click.echo(results)
    click.echo(f"Board {name} deleted.")


######################################################################
# I S S U E S   C O M M A N D S
######################################################################

@cli.group()
@click.pass_context
def issues(ctx):
    """Create, Get, Update, Delete Issues"""

#---------------------------------------------------------------------
# GET ISSUES
#---------------------------------------------------------------------
@issues.command('get')
@click.pass_context
def get_issues(ctx):
    """Returns all of the issues for a project"""
    click.echo(f"Getting issues for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    issues = gitlab.get('issues')
    click.echo(issues)

#---------------------------------------------------------------------
# CREATE ISSUES
#---------------------------------------------------------------------
@issues.command('create')
@click.pass_context
def create_issues(ctx):
    """Creates issues for a project from a CVS file"""
    click.echo(f"Creating issues for project {ctx.obj['PROJECT']}...")
    raise click.ClickException("Not implemented yet!")


######################################################################
# U T I L I T I E S
######################################################################
def csv_to_dict(filename: str) -> list:
    """Converts a CSV file to a dictionary"""
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
