import typer

app = typer.Typer()


@app.command()
def pew(name: str = typer.Argument(..., help="Name of the person to Pew"), count: int = typer.Argument(1, help="How many times to pew")):
    print(f"You {count * 'pew '}{name}")
    print(f"RIP: {name}")


@app.command()
def slap(name: str = typer.Argument(..., help="Who to slap"),
         size: str = typer.Argument("small", help="Size of hand to slap with")):
    print(f"You slapped {name} with a {size} hand")
    if size == "small":
        print(f"{name}'s face is slightly red")
    elif size == "medium":
        print(f"{name}'s face is significantly red")
    elif size == "large":
        print(f"{name}'s knocked out")
    else:
        print(f"{name} ")




if __name__ == "__main__":
    app()