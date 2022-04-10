import click, subprocess

# --- add Repositories command --- #
@click.command()
@click.argument('name', default ='my-hello')
@click.confirmation_option(prompt="Are you sure you want to delete?")
def cli(name):
    """Uninstall - Delete Chart"""
    cmd = ["helm", "delete", f"{name}"]
    subprocess.run(cmd, text=True)


