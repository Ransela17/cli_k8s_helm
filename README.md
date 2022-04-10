# JPD
jpd CLI is simple interface that automates action with helm charts

## How to Install
1. `git clone `
2. `pip install .`
3. execute 'jpd' commands `jpd` See [Examples](#Examples) section for commands to run.
4. In the first command enter a username and password for jfrog platform

## Documentation for required libraries

- Docker -         https://docs.docker.com/get-docker/
- Minikube -       https://minikube.sigs.k8s.io/docs/start/
- Helm -           https://helm.sh/
- Python -         https://docs.python.org/3/library/configparser.html
- Helloworld App - https://artifacthub.io/packages/helm/cloudecho/hello

## Examples for 'jpd' commands

jpd cli implement several commends of the following:

- install default - install default package
- install chart - install with specific arguments
- uninstall 
- Repo commands

```commandline
rans$ jpd
Usage: jpd [OPTIONS] COMMAND [ARGS]...

  Simple CLI to manage an k8s with helm

Options:
  --help  Show this message and exit.

Commands:
  install          Install a chart
  install_default  Install the default chart with all
  repo             This command consists of multiple subcommands to...
  uninstall        Uninstall - Delete Chart
  ```

```commandline
 rans$ jpd repo
Usage: jpd repo [OPTIONS] COMMAND [ARGS]...

  This command consists of multiple subcommands to interact with chart
  repositories.

Options:
  --help  Show this message and exit.

Commands:
  add     Add a chart repository - need provide argument - name and url
  list    List chart repositories
  update  Update information of available charts locally from chart...
  ```