"""
GitLab Kanban Board Command Line Interface
"""
import csv
import click
from tqdm import tqdm
from .models import GitLab, Label


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
    label_data = csv_to_dict(input)
    click.echo(f"Found {len(label_data)} labels...")
    click.echo("Sending to GitLab...")
    label = Label(ctx.obj['GITLAB'])
    for entry in tqdm(label_data, total=len(label_data)):
        results = label.create(entry)
    click.echo("Done")

#---------------------------------------------------------------------
# LIST LABELS
#---------------------------------------------------------------------
@labels.command('list')
@click.pass_context
def list_labels(ctx):
    """Returns all of the labels for a project"""
    click.echo(f"Getting labels for project {ctx.obj['PROJECT']}...")
    label = Label(ctx.obj['GITLAB'])
    labels = label.all()
    click.echo(labels)

#---------------------------------------------------------------------
# DELETE LABELS
#---------------------------------------------------------------------
@labels.command('delete')
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The CSV file with the labels to delete")
@click.pass_context
def delete_labels(ctx, input, all):
    """Deletes labels for a project from a CVS file"""
    click.echo(f"Deleting labels for project {ctx.obj['PROJECT']}...")
    click.echo(f"Processing {input}...")
    label_data = csv_to_dict(input)
    click.echo(f"Found {len(label_data)} labels...")
    click.echo("Sending to GitLab...")
    label = Label(ctx.obj['GITLAB'])    
    for entry in tqdm(label_data, total=len(label_data)):
        label.delete_by_name(entry["name"])
    click.echo("Done")



######################################################################
# B O A R D S   C O M M A N D S
######################################################################

@cli.group()
@click.pass_context
def boards(ctx):
    """Create, Get, Update, Delete Kanban Boards"""

#---------------------------------------------------------------------
# LIST BOARDS
#---------------------------------------------------------------------
@boards.command('list')
@click.pass_context
def list_boards(ctx):
    """Returns all of the kanban boards for a project"""
    click.echo(f"Getting kanban boards for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    board_data = gitlab.get('boards')
    click.echo(board_data)

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
    label_data = csv_to_dict(input)
    click.echo(f"Found {len(label_data)} labels...")
    path = f"boards/{board_id}/lists"
    for entry in tqdm(label_data, total=len(label_data)):
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
    board_data = gitlab.get('boards')
    result = [board for board in board_data if board["name"] == name]
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
# CREATE ISSUES
#---------------------------------------------------------------------
@issues.command('create')
@click.option("--input", "-i", type=click.Path(exists=True), required=True, help="The CSV file with issues")
@click.pass_context
def create_issues(ctx, input):
    """Creates issues for a project from a CVS file"""
    click.echo(f"Creating issues for project {ctx.obj['PROJECT']}...")
    click.echo(f"Processing {input}...")
    issue_data = csv_to_dict(input)
    click.echo(f"Found {len(issue_data)} issues...")
    # click.echo(issue_data)
    click.echo("Sending to GitLab...")
    gitlab = ctx.obj['GITLAB']
    for entry in tqdm(issue_data, total=len(issue_data)):
        results = gitlab.post('issues', entry)
        # click.echo(results)
    click.echo("Done")

#---------------------------------------------------------------------
# LIST ISSUES
#---------------------------------------------------------------------
@issues.command('list')
@click.pass_context
def list_issues(ctx):
    """Returns all of the issues for a project"""
    click.echo(f"Getting issues for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    issues = gitlab.get('issues')
    click.echo(issues)


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
