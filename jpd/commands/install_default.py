import click, subprocess, time

@click.command()
@click.option('-ns', '--namespace', default='default', help='To use this option you need to create namespace first')
@click.option('-v', '--version', default='', help='Default is the latest')
@click.option('-n', '--name', default ='my-hello', help='Release name')
@click.option('--setter', is_flag=False, flag_value='', help = 'Configuration data for override')
def cli(namespace, version, name, setter):
    '''Install the default chart with all'''
    cmd = ["helm", "repo", "add", "cloudecho", "https://cloudecho.github.io/charts/"]
    subprocess.run(cmd, text=True)

    cmd = ["helm", "repo", "update"]
    subprocess.run(cmd, text=True)

    cmd = ["helm", "install", f"{name}", "cloudecho/hello", "-n", f"{namespace}", f"--version={version}"]
    if setter is not None:
        commend = '--set ' + str(setter)
        cmd.append(commend)
    subprocess.run(cmd, text=True)
