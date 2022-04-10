import click, subprocess, time

@click.command()
@click.option('-ns', '--namespace', default='default', help='Namespace default is default,to use this option you need to create namespace first')
@click.option('-v', '--version', default='', help='Default is the latest')
@click.option('-n', '--name', default = 'my-hello',help='Release name')
@click.option('-rn', 'reponame', default='')
def cli(namespace, version, name, reponame):
    '''Install a chart'''
    cmd = ["helm", "install", f"{name}", f"{reponame}", "-n", f"{namespace}", f"--version={version}"]
    subprocess.run(cmd, text=True)
