import typer

"""
create typer app, turn hello_name into a command and call you Typer app
"""

# turn me into a command
def hello_name(name: str):
	print(f"Hello {name}!")


if __name__ == "__main__":
	# call app