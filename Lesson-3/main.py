import typer

app = typer.Typer()


"""
create a function called loud_printer. Printer should take string to print and have a option to print a single word each line
loud_printer should take an option to yell. yell should always be used.

add the printer to the typer app commands.

"""


@app.command()
def hello(name: str):
    print(f"Hello {name}")

if __name__ == "__main__":
    app()