# `goit-pythonweb-hw-01`

Woolf University, Computer Science
GoIT Noeversity, Python Web course, Lesson 1

## Project overview

This repository contains two academic Python tasks that demonstrate the use of
object-oriented design principles and common software engineering practices.
Both solutions were updated to meet the assignment requirements:

- apply type hints throughout the code,
- replace `print()` with logging at `INFO` level,
- format the source code with `black`.

The project is intentionally small, but it demonstrates several important
concepts used in real Python applications:

- abstraction and inheritance,
- interfaces based on abstract base classes,
- separation of responsibilities,
- logging instead of direct console output,
- readable, standardized code formatting.

## Assignment goals

The course task asked to implement two independent programs:

1. an abstract factory for vehicles,
2. a simple library management console application.

In both cases, the code had to be written with type annotations and should use
logging rather than direct printing to the terminal.

## Task 1: Vehicle factory

### Problem statement

The first task demonstrates the **Abstract Factory** design pattern. The goal
is to create families of related objects without binding the client code to a
concrete class.

### Implementation

The implementation in `task_1.py` contains:

- `Vehicle`: an abstract base class that defines the common interface,
- `Car` and `Motorcycle`: concrete vehicle implementations,
- `VehicleFactory`: an abstract factory that declares creation methods,
- `USVehicleFactory` and `EUVehicleFactory`: concrete factories that create
	vehicles with market-specific model names.

### Design notes

- The `Vehicle` class defines the shared contract through the abstract
	`start_engine()` method.
- The factory classes return objects through the shared `Vehicle` type,
	keeping the client decoupled from the exact implementation.
- Logging is used inside `start_engine()` to report the action at `INFO` level.

### Example usage

```python
from task_1 import EUVehicleFactory

factory = EUVehicleFactory()
car = factory.create_car("Toyota", "Corolla")
car.start_engine()
```

## Task 2: Library manager

### Problem statement

The second task implements a small console-based library system. It supports
adding books, removing books by title, and displaying the current collection.

### Implementation

The implementation in `task_2.py` contains:

- `Book`: a data object describing one book,
- `LibraryInterface`: an abstract interface for library operations,
- `Library`: a concrete in-memory storage implementation,
- `LibraryManager`: a service layer that handles user-facing actions,
- `main()`: a command-line loop for interactive use.

### Design notes

- `LibraryInterface` describes the expected behavior of the storage layer.
- `Library` keeps books in memory using a typed list.
- `LibraryManager` separates user input handling from book storage logic.
- All output is written through the `logging` module at `INFO` level.
- When the library is empty, the program logs a clear informational message
	instead of printing nothing.

### Example usage

Run the module directly and use the interactive menu:

```python
python task_2.py
```

Example session:

```text
Enter command (add, remove, show, exit): add
Enter book title: Clean Code
Enter book author: Robert C. Martin
Enter book year: 2008
Enter command (add, remove, show, exit): show
Title: Clean Code, Author: Robert C. Martin, Year: 2008
```

## Recent fixes

After review, the following improvements were added to finalize the submission:

- `task_1.py` now includes an executable `main()` function with a concrete
	factory usage demo (US and EU factories, object creation, engine start calls).
- `task_1.py` now configures logging via
	`logging.basicConfig(level=logging.INFO, format="%(message)s")` to guarantee
	visible console output when the file is run directly.
- `task_2.py` was adjusted so that `LibraryInterface` is a pure interface
	(method contract only) and no longer stores `books` state.
- `task_2.py` keeps state in `Library`, which is the correct concrete
	implementation for in-memory storage.

## Code quality requirements

The submitted solution follows the assignment rules in the following way:

- **Type hints**: all public classes and methods use explicit type annotations.
- **Logging**: console output is produced via `logging.info()` instead of
	`print()`.
- **Formatting**: the files are formatted with `black` for consistent style.

## Project structure

```text
README.md
task_1.py
task_2.py
task_source.py
```

- `task_source.py` contains the original task examples.
- `task_1.py` contains the vehicle factory solution.
- `task_2.py` contains the library management solution.

## How to run

If you are using the provided virtual environment, run the scripts with:

```bash
.venv/bin/python task_1.py
.venv/bin/python task_2.py
```

If `black` is installed, the files can be formatted again with:

```bash
.venv/bin/python -m black task_1.py task_2.py
```

## Educational value

This assignment is useful for practicing:

- object-oriented programming,
- abstraction and interface design,
- type-safe Python code,
- logging-based output handling,
- clean code formatting and maintainability.

It also shows how a small academic exercise can be structured in a way that is
close to professional Python development practices.
