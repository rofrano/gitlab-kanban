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
    """Creates labels, lists, and issues"""

#---------------------------------------------------------------------
# CREATE LABELS
#---------------------------------------------------------------------
@create.command('labels')
@click.pass_context
def create_labels(ctx):
    """Creates labels"""
    click.echo("Creating label...")

#---------------------------------------------------------------------
# CREATE ISSUES
#---------------------------------------------------------------------
@create.command('issues')
@click.pass_context
def create_labels(ctx):
    """Creates issues"""
    click.echo("Creating issues...")

#---------------------------------------------------------------------
# CREATE LISTS
#---------------------------------------------------------------------
@create.command('lists')
@click.pass_context
def create_labels(ctx):
    """Creates lists"""
    click.echo("Creating lists...")


######################################################################
# G E T
######################################################################

@cli.group()
@click.pass_context
def get(ctx):
    """Gets labels, lists, and issues"""

#---------------------------------------------------------------------
# GET LABELS
#---------------------------------------------------------------------
@get.command('labels')
@click.pass_context
def get_labels(ctx):
    """Get the labels for a project"""
    click.echo("Getting labels...")
    gitlab = ctx.obj['GITLAB']
    labels = gitlab.get('labels')
    click.echo(labels)

#---------------------------------------------------------------------
# GET ISSUES
#---------------------------------------------------------------------
@get.command('issues')
@click.pass_context
def get_issues(ctx):
    """Getting issues"""
    click.echo("Getting issues...")
    gitlab = ctx.obj['GITLAB']
    issues = gitlab.get('issues')
    click.echo(issues)

#---------------------------------------------------------------------
# GET LISTS
#---------------------------------------------------------------------
@get.command('lists')
@click.pass_context
def get_lists(ctx):
    """Getting lists"""
    click.echo("Getting lists...")
    gitlab = ctx.obj['GITLAB']
    lists = gitlab.get('lists')
    click.echo(lists)

