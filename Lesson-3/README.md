# Lesson 2

### Arguments

One of the key features of Typer is the `Argument` class. This class represents a positional argument that can be passed to a command. 
You can use the Argument class to define 
* name 
* help text
* data type
* default values 

When the user invokes your command, Typer will parse the command-line arguments and pass them to your function as arguments.

The `Argument` class is highly customizable and supports a wide range of data types
* strings
* integers
* floats
* booleans
* file paths. 

Additionally, you can define the number of arguments that your 
command expects, specify whether an argument is required or optional, 
and even provide a callback function to validate the input value.

Overall, the `Argument` class in Typer is a powerful tool for building \
command-line interfaces that are easy to use and highly customizable. 
It allows you to define the behavior of your commands in a clear and concise way,
making it easier for users to interact with your application from the command line.