import click, os, docker

__author__ = "Ran Sela"

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

DOCKER_CLIENT = docker.DockerClient(base_url='unix://var/run/docker.sock')
RUNNING = 'running'


### Check if minikube is runing
def is_running(container_name):
    """
    verify the status of a sniffer container by it's name
    :param container_name: the name of the container
    :return: Boolean if the status is ok
    """
    container = DOCKER_CLIENT.containers.get(container_name)

    container_state = container.attrs['State']

    container_is_running = container_state['Status'] == RUNNING

    return container_is_running


#########
# MyCLI Class - Custom Multi Commands - From Click Library
#########

class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')


@click.command(cls=MyCLI)
def cli():
    """
    Simple CLI to manage an k8s with helm
    """
    try:
        if not is_running('minikube'):
            click.echo('There is Problem with Docker - Please Restart Docker!')
    except ImportError as e:
        click.echo('Error - Problem to run the cli')



