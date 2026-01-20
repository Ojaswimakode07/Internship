<b>Note Manager – Python Utility</b>
<b>Overview</b>

<b>Note Manager</b> is a lightweight Python-based application designed to help users create, store, and manage personal notes efficiently. The project provides both a <b>Command Line Interface (CLI)</b> and a simple <b>Graphical User Interface (GUI)</b>, allowing users to interact with the system in their preferred way.

The primary goal of this project is to demonstrate core software development concepts such as <b>problem analysis, clean and modular coding practices, file handling, and basic user interaction</b> using Python’s standard libraries.

<b>Problem Statement</b>

In daily academic and professional life, users frequently create short notes such as ideas, reminders, and tasks. These notes are often saved without a consistent structure or organization. Over time, this leads to <b>scattered and disorganized information</b>, making retrieval and management difficult.

Manually organizing such notes is time-consuming and inefficient. Therefore, a <b>simple and structured note management system</b> is required to store and access notes in a reliable and organized manner.

<b>Solution Description</b>

The <b>Note Manager</b> application provides a straightforward solution by allowing users to create notes that are automatically saved with <b>timestamp-based filenames</b>, ensuring uniqueness and preventing overwriting.

All notes are stored as <b>plain text files</b> inside a dedicated folder, making them easy to access, read, and manage without requiring any external tools. The application supports both <b>CLI and GUI modes</b> to accommodate different user preferences while keeping the design minimal and functional.

<b>Features</b>

Create and save notes quickly

Automatic timestamp-based file naming

View previously saved notes using the CLI

Supports both Command Line and Graphical interfaces

Uses only Python standard libraries

Lightweight, portable, and easy to run

<b>Technology Stack</b>

<b>Programming Language:</b> Python 3

<b>Libraries Used:</b>

<b>os</b> – for directory and file handling

<b>datetime</b> – for timestamp generation

<b>tkinter</b> – for building the graphical interface

All libraries used are part of <b>Python’s standard library</b>, ensuring that the application runs without additional dependencies.

<b>Project Structure</b>
note-manager/
│
├── notes.py        # Command Line Interface implementation
├── notes_gui.py    # Graphical User Interface implementation
├── notes/          # Folder where all notes are stored
└── README.md       # Project documentation

<b>How to Run the Application</b>
<b>Prerequisites</b>

Python 3 must be installed on the system

Verify installation using:

python --version

<b>Running the Command Line Version</b>

Navigate to the project directory

Run:

python notes.py


<b>Available options:</b>

Add a new note

View existing notes

Exit the application

<b>Running the Graphical Interface Version</b>

Navigate to the project directory

Run:

python notes_gui.py


A graphical window will open where users can write and save notes using a <b>simple and intuitive interface</b>.

<b>Design Decisions</b>

Python was chosen for its <b>simplicity, readability, and wide availability</b>

Timestamp-based filenames ensure <b>unique note storage</b>

Plain text storage improves <b>transparency and accessibility</b>

The GUI is intentionally <b>minimal</b> to prioritize functionality

No external libraries are used to keep the project <b>lightweight and portable</b>
