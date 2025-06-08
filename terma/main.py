import typer
from backend.interpreter import return_command

app = typer.Typer()


@app.command()
def run(query: str):
    shell_command = return_command(query)
    typer.echo(f"Shell command: {shell_command}")


if __name__ == "__main__":
    app()
