import typer

app = typer.Typer()


"""
create a new function called pew that takes a name and a count argument for how many times to print pew
use typer.Argument for count that sets a default and add the help parameter

add that function as a command to your app
 
"""

@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()