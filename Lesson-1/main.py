import typer

# create typer app and command
def hello_name(name: str):
	print(f"Hello {name}!")


if __name__ == "__main__":
	# call app