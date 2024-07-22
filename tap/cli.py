import click
from os import getcwd
from pathlib import Path
from demo.cli import cli as demo_cli
from generate import generate_recursive


DEMO_OUTPUT_PATH = Path('docs-output')


@click.group()
def cli():
    """
    Generate API doc pages from your click-based tool
    """
    pass


@cli.command('demo', help='Run on the demo cli')
def demo():
    return generate_recursive(demo_cli, DEMO_OUTPUT_PATH, [])


@cli.command('gen', help='Generate from a cli tool')
@click.option('base_command', '-c', type=click.Command, required=True,
              help='The base command name of the cli tool')
@click.option('base_dir', '-d', '--base-dir', type=Path, default=Path(getcwd()),
              help='The base directory of the cli tool')
def generate(base_command: click.Command, base_dir: Path):
    return generate_recursive(base_command, base_dir, [])


if __name__ == '__main__':
    exit(cli())
