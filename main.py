import demo.cli
from typing import List
from click import Context, Option


OUTPUT_PATH = './docs-output'

base_template = """\
# {title}

{description}

## CLI Usage

```
{cli_usage}
```
"""

subcommands_template = """
## Subcommands

{subcommands}
"""

options_template = """
## Options and Flags

{options}
"""

command_template = base_template + options_template
group_template = base_template + subcommands_template + options_template


def get_context(command, context_path: List[Context]) -> Context:
    parent = context_path[-1] if context_path else None
    return Context(command, info_name=command.name, parent=parent)


def sort_params(params: list) -> list:
    params = sorted(params, key=lambda p: str(type(p)))
    return sorted(params, key=lambda p: p.required, reverse=True)


def format_param(param) -> str:
    is_option = type(param) is Option
    return f"""\
- `{param.opts[0]}`{f' - {param.help}' if is_option else ''}
  - {'required' if param.required else f'default - `{param.default}`' if is_option else 'optional'}
  - type - `{str(param.type).lower()}`
"""


def generate_command(command, context_path: List[Context]):
    usage = command.get_usage(get_context(command, context_path)).replace('Usage: ', '')
    sorted_params = sort_params(command.params)
    params = ''.join([format_param(param) for param in sorted_params])
    is_group = hasattr(command, 'commands')
    template = group_template if is_group else command_template
    subcommands = '\n'.join([f'- {cmd}' for cmd in command.commands.keys()]) if is_group else None

    with open(f'{OUTPUT_PATH}/{command.name}.md', 'w') as f:
        f.write(
            template.format(
                title=command.name,
                description=command.help.strip(),
                cli_usage=usage,
                subcommands=subcommands,
                options=params if params else "This command has no options."
            )
        )


def generate_recursive(command, context_path: List[Context]):
    generate_command(command, context_path)
    if hasattr(command, 'commands'):
        for sub_name, sub_command in command.commands.items():
            generate_recursive(sub_command, context_path + [get_context(command, context_path)])


def main():
    # User defined - can be defaulted to 'cli'
    cli_super = demo.cli.cli
    return generate_recursive(cli_super, [])


if __name__ == '__main__':
    main()
