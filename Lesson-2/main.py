import typer

app = typer.Typer()


@app.command()
def pew(name: str = typer.Argument(..., help="Name of the person to Pew"), count: int = typer.Argument(1, help="How many times to pew")):
    print(f"You {count * 'pew '}{name}")

@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()