import typer
from terma.interpreter import return_command
import subprocess
import importlib.metadata
from typing import Optional
from typing_extensions import Annotated

try:
    __version__ = importlib.metadata.version("terma")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

app = typer.Typer(rich_markup_mode=None,
                  help="Terma: A smart terminal assistant that converts natural language requests into shell commands and executes them.", )


def version_callback(value: bool):
    if value:
        typer.echo(f"Terma {__version__}")
        raise typer.Exit()


@app.callback()
def common(
        ctx: typer.Context,
        version: bool = typer.Option(None, "--version", callback=version_callback),
):
    pass


@app.command(help="Process the user's natural language query and execute the corresponding shell command.")
def exec(query):
    shell_command = return_command(query)
    typer.echo(f"Recommended Command(s): {shell_command}")

    run = typer.prompt("Execute? (y/n)")
    affirmative = ["y", "Y", "yes", "Yes", "YES"]

    if run in affirmative:
        try:
            result = subprocess.run(shell_command, shell=True, capture_output=True)
            typer.echo(result.stdout.decode())
        except subprocess.CalledProcessError as e:
            typer.echo(f"\nError occurred while executing the command:\n{e.stderr}", err=True)


if __name__ == "__main__":
    app()
