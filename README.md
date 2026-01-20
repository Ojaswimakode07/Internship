<u><b>Overview</b></u>

This project is a simple Python-based utility developed to create and manage personal notes efficiently. It supports both a Command Line Interface (CLI) and a basic Graphical User Interface (GUI), allowing users to choose their preferred mode of interaction.

The project is designed to demonstrate fundamental software development concepts such as problem understanding, clean coding, file handling, and basic user interaction.

<u><b>Problem Statement</b></u>

During regular study and work activities, short notes such as ideas, reminders, and tasks are often created quickly and saved without proper structure. Over time, this results in disorganized information that becomes difficult to track or retrieve.

Manually organizing such notes is inefficient. Therefore, a simple and structured system is required to store notes in an organized and consistent manner.

<u><b>Solution Description</b></u>

This utility allows users to create notes that are automatically saved with a timestamp-based filename. Notes are stored as text files inside a dedicated folder, making them easy to access, read, and manage.

The application provides both a command-line interface and a graphical user interface, ensuring flexibility and ease of use for different users.

<u><b>Features</b></u>

Create and store notes easily

Automatic timestamp-based file naming

View all saved notes through the CLI

Supports both CLI and GUI usage

Uses only Python standard libraries

<u><b>Technology Stack</b></u>

Programming Language: Python 3

Libraries Used: os, datetime, tkinter

All libraries used are part of the Python Standard Library, ensuring portability and ease of execution.

<u><b>Project Structure</b></u>
note-manager/
│
├── notes.py        # Command line version
├── notes_gui.py    # Graphical interface version
├── notes/          # Automatically created folder for storing notes
└── README.md

<u><b>How to Run the Application</b></u>
<u><b>Prerequisites</b></u>

Python 3 must be installed on the system

You can verify the installation using:

python --version

<u><b>Running the Command Line Version</b></u>

Navigate to the project directory and run:

python notes.py


Available options:

Add a new note

View existing notes

Exit the application

<u><b>Running the Graphical Interface Version</b></u>

From the project directory, run:

python notes_gui.py


A window will open where notes can be written and saved using the graphical interface.

<u><b>Design Decisions</b></u>

Python was selected for its simplicity and readability

Timestamp-based filenames ensure uniqueness and prevent overwriting

Notes are stored as plain text files for transparency and easy access

The GUI is intentionally minimal to focus on core functionality

No external libraries are used, keeping the project lightweight and portable
