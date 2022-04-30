"""
GitLab Kanban Board Command Line Interface
"""
import click
from .gitlab import GitLab

@click.group()
@click.option("-t", "--token", required=True, envvar="GITLAB_TOKEN", help="GitLab authorization token or set env GITLAB_TOKEN")
@click.option("-p", "--project", required=True, envvar="GITLAB_PROJECT", help="The GitLab project ID or set env GITLAB_PROJECT")
@click.option("-u", "--gitlab-url", required=False, envvar="GETLAB_URL", default="https://gitlab.com", help="GitLab URL (defaults to https://gitlab.com)")
@click.pass_context
def cli(ctx, token, project, gitlab_url):
    """GitLab Kanban Board Command Line Interface"""
    ctx.ensure_object(dict)
    ctx.obj['PROJECT'] = project
    ctx.obj['GITLAB_TOKEN'] = token
    ctx.obj['GITLAB'] = GitLab(project, token, gitlab_url)
    
######################################################################
# C R E A T E
######################################################################

@cli.group()
@click.pass_context
def create(ctx):
    """Creates labels, lists, and issues from a CSV file"""

#---------------------------------------------------------------------
# CREATE LABELS
#---------------------------------------------------------------------
@create.command('labels')
@click.pass_context
def create_labels(ctx):
    """Creates labels for a project from a CVS file"""
    click.echo(f"Creating labels for project {ctx.obj['PROJECT']}...")
    raise click.ClickException("Not implemented yet!")

#---------------------------------------------------------------------
# CREATE ISSUES
#---------------------------------------------------------------------
@create.command('issues')
@click.pass_context
def create_labels(ctx):
    """Creates issues for a project from a CVS file"""
    click.echo(f"Creating issues for project {ctx.obj['PROJECT']}...")
    raise click.ClickException("Not implemented yet!")

#---------------------------------------------------------------------
# CREATE LISTS
#---------------------------------------------------------------------
@create.command('lists')
@click.pass_context
def create_labels(ctx):
    """Creates kanban board lists for a project from a CVS file"""
    click.echo(f"Creating kanban board lists for project {ctx.obj['PROJECT']}...")
    raise click.ClickException("Not implemented yet!")


######################################################################
# G E T
######################################################################

@cli.group()
@click.pass_context
def get(ctx):
    """Gets labels, lists, and issues for a project"""

#---------------------------------------------------------------------
# GET LABELS
#---------------------------------------------------------------------
@get.command('labels')
@click.pass_context
def get_labels(ctx):
    """Returns all of the labels for a project"""
    click.echo(f"Getting labels for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    labels = gitlab.get('labels')
    click.echo(labels)

#---------------------------------------------------------------------
# GET ISSUES
#---------------------------------------------------------------------
@get.command('issues')
@click.pass_context
def get_issues(ctx):
    """Returns all of the issues for a project"""
    click.echo(f"Getting issues for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    issues = gitlab.get('issues')
    click.echo(issues)

#---------------------------------------------------------------------
# GET LISTS
#---------------------------------------------------------------------
@get.command('lists')
@click.pass_context
def get_lists(ctx):
    """Returns all of the kanban board lists for a project"""
    click.echo(f"Getting kanban board lists for project {ctx.obj['PROJECT']}...")
    gitlab = ctx.obj['GITLAB']
    lists = gitlab.get('lists')
    click.echo(lists)
