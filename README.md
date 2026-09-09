````markdown
# Python Assignment

This repository contains my HackerRank Python solutions completed as part of my Python training and practice.

The solutions are organized by problem, with separate files for the solution logic, program execution, and unit testing.

## Project Structure

```text
Python_Assignment/
│
├── src/
│   ├── lists/
│   │   ├── util.py
│   │   └── driver.py
│   ├── calendar/
│   │   ├── util.py
│   │   └── driver.py
│   └── ...
│
├── tests/
│   ├── lists/
│   │   └── test_lists.py
│   ├── calendar/
│   │   └── test_calendar.py
│   └── ...
│
└── README.md
````

## Code Organization

### `src/`

Contains the implementation of each HackerRank problem.

* `util.py` – Contains the main function and problem-solving logic.
* `driver.py` – Handles user input and displays the output.

### `tests/`

Contains unit test cases for each HackerRank problem.

The tests are written using Python's built-in `unittest` framework and are used to verify the functions independently.

## Topics Covered

The assignment includes problems related to:

* Python Basics
* Lists, Tuples, Sets and Dictionaries
* Strings and String Manipulation
* Functions
* Collections
* Itertools
* Date and Time
* Regular Expressions
* NumPy
* Unit Testing

## Running the Programs

A particular problem can be executed using its `driver.py` file:

```bash
python src/question_name/driver.py
```

## Running Tests

To run the test case for a particular problem:

```bash
python -m unittest tests/question_name/test_question_name.py
```

To run all available tests:

```bash
python -m unittest discover
```

## Technologies Used

* Python
* NumPy
* `unittest`
* Python Standard Library

## Purpose

The purpose of this repository is to practice Python programming and problem-solving through HackerRank challenges while maintaining a structured and testable codebase.

```
```
