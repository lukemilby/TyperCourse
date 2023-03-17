
# Welcome to the Interactive Typer Tutorial!
In this tutorial, you will learn how to use Typer, a framework for building command-line interface (CLI) tools in Python. You will also become familiar with two other essential tools for software development: Git and pytest.

The tutorial is divided into several lessons, each containing a main.py file and a test file. Your goal is to write code in the main.py file to make the program work correctly, and then run the test file using pytest to ensure that your implementation passes the test.

### Course Lessons
* [Lesson 1](/Lesson%201)
  * Simple Typer app to print
    * running typer and using help
* [Lesson 2](/Lesson%202)
  * Typer app that pew's and slaps your favorite person
    * Setting up a Typer application
    * Typer command decorator
    * Arguments
    * Options
### How to Use Git
Git is a version control system that allows you to track changes to your code and collaborate with others. To get started, you will need to clone the repository for this tutorial:

```bash
git clone https://github.com/your-username/typer-tutorial.git
```
Once you have cloned the repository, you can switch to the directory for the first lesson:

```bash
cd typer-tutorial/lesson-1
```

At the end of each lesson, you should commit your changes to Git:

```bash
git add main.py
git commit -m "Completed lesson 1"
```
You can then push your changes to the remote repository:

```bash
git push origin main
```
## How to Test using Pytest

Pytest is a testing framework for Python that makes it easy to write and run tests. To run the tests for each lesson, navigate to the lesson directory and run the following command:

```bash
pytest test_lesson.py
```

If your implementation passes the test, you will see a message indicating that all tests have passed. Otherwise, pytest will display an error message indicating which test(s) failed and why.

Congratulations on taking your first steps in learning Typer, Git, and pytest! Let's get started with [Lesson 1](/Lesson%201).