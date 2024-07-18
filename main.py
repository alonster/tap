import demo.cli
from click import Context


OUTPUT_PATH = './docs-output'

command_template = """
# {title}

{description}

## CLI Usage

```
{cli_usage}
```

## Options and Flags

{options}
"""


def generate_command(command, context_path: list[Context]):
    parent = context_path[-1] if context_path else None
    context = Context(command, info_name=command.name, parent=parent)
    params = '\n'.join([f' - {param.name}' for param in command.params])
    with open(f'{OUTPUT_PATH}/{command.name}.md', 'w') as f:
        f.write(
            command_template.format(
                title=command.name,
                description=command.help,
                cli_usage=command.get_usage(context),
                options=params
            )
        )


def generate_recursive(command, context_path: list[Context]):
    parent = context_path[-1] if context_path else None
    context = Context(command, info_name=command.name, parent=parent)
    generate_command(command, context_path)
    if hasattr(command, 'commands'):
        for sub_name, sub_command in command.commands.items():
            generate_recursive(sub_command, context_path + [context])


def main():
    # User defined - can be defaulted to 'cli'
    cli_super = demo.cli.cli
    return generate_recursive(cli_super, [])


if __name__ == '__main__':
    main()
