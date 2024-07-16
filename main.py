import demo.cli


OUTPUT_PATH = './docs-output'


def generate_command(command):
    params = '\n'.join([f' - {param.name}' for param in command.params])
    with open(f'{OUTPUT_PATH}/{command.name}.md', 'w') as f:
        f.write(f'# {command.name}\n\n{command.help}\n\n## Usage\n\n{params}')


def generate_recursive(command):
    generate_command(command)
    if hasattr(command, 'commands'):
        for sub_name, sub_command in command.commands.items():
            generate_recursive(sub_command)


def main():
    # User defined - can be defaulted to 'cli'
    cli_super = demo.cli.cli
    return generate_recursive(cli_super)


if __name__ == '__main__':
    main()
