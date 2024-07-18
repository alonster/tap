import click


@click.group()
def cli():
    """
    A simple CLI tool for demonstrating Tap.
    """
    pass


@cli.command('hello', help='Say Hi')
@click.argument('name', type=str)
def print_name(name: str):
    click.echo(f'Hello {name}!')


@cli.command('count', help='Count to number')
@click.option('reverse', '--reverse/--no-reverse', default=False, help='Count in reverse')
@click.argument('number', type=int)
@click.argument('towards', type=str, required=False)
def count(number: int, reverse: bool, towards: str):
    numbers = [str(num + 1) for num in range(number)]
    if reverse:
        numbers.reverse()
    click.echo(f'Counting{" towards " + towards}: {" ".join(numbers)}!')
