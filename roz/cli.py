"""Main CLI entry point for Roz."""

import click

from roz import __version__
from roz.commands.cloud import cloud
from roz.commands.search import search


@click.group()
@click.version_option(version=__version__, prog_name="roz")
def cli():
    """Roz - An Agentic Coding CLI tool."""
    pass


cli.add_command(cloud)
cli.add_command(search)


def main():
    """Entry point for the CLI."""
    cli()


if __name__ == "__main__":
    main()
