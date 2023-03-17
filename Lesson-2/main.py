import typer

app = typer.Typer()


"""
create a new command called pew that takes a name and a count for how many times to print pew
use typer.Argument for count that sets a default and add the help parameter 
"""
@app.command()
def pew(name:str, count:int = typer.Argument(1, help="how many times to pew")):
    print(f"You {'pew ' * count}{name}")

@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()