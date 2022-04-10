import subprocess
import click


# --- Repositories Group command called repo  --- #
@click.group()
def cli():
    """This command consists of multiple subcommands to interact with chart repositories."""
    pass

@cli.command()
@click.argument('name', nargs=1)
@click.argument('url', nargs=1)
def add(name, url):
    '''Add a chart repository - need provide argument - name and url'''
    cmd = ['helm', 'add', f'{name}', f'{url}']
    subprocess.run(cmd, text=True)

@cli.command()
def list():
    '''List chart repositories'''
    cmd = ['helm', 'repo', 'list']
    subprocess.run(cmd, text=True)

@cli.command()
def update():
    '''Update information of available charts locally from chart repositories'''
    cmd = ['helm', 'repo', 'update']
    subprocess.run(cmd, text=True)
