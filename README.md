Note Manager – Python Utility
Overview

Note Manager is a lightweight Python-based application designed to help users create, store, and manage personal notes efficiently. The project provides both a Command Line Interface (CLI) and a simple Graphical User Interface (GUI), allowing users to interact with the system in their preferred way.

The primary goal of this project is to demonstrate core software development concepts such as problem analysis, clean and modular coding practices, file handling, and basic user interaction using Python’s standard libraries.

Problem Statement

In daily academic and professional life, users frequently create short notes such as ideas, reminders, and tasks. These notes are often saved without a consistent structure or organization. Over time, this leads to scattered and disorganized information, making retrieval and management difficult.

Manually organizing such notes is time-consuming and inefficient. Therefore, a simple and structured note management system is required to store and access notes in a reliable and organized manner.

Solution Description

The Note Manager application provides a straightforward solution by allowing users to create notes that are automatically saved with timestamp-based filenames, ensuring uniqueness and preventing overwriting.

All notes are stored as plain text files inside a dedicated folder, making them easy to access, read, and manage without requiring any external tools. The application supports both CLI and GUI modes to accommodate different user preferences while keeping the design minimal and functional.

Features

Create and save notes quickly

Automatic timestamp-based file naming

View previously saved notes using the CLI

Supports both Command Line and Graphical interfaces

Uses only Python standard libraries

Lightweight, portable, and easy to run

Technology Stack

Programming Language: Python 3

Libraries Used:

os – for directory and file handling

datetime – for timestamp generation

tkinter – for building the graphical interface

All libraries used are part of Python’s standard library, ensuring that the application runs without additional dependencies.

Project Structure
note-manager/
│
├── notes.py        # Command Line Interface implementation
├── notes_gui.py    # Graphical User Interface implementation
├── notes/          # Folder where all notes are stored
└── README.md       # Project documentation

How to Run the Application
Prerequisites

Python 3 must be installed on the system

You can verify the installation by running:

python --version

Running the Command Line Version

Navigate to the project directory

Run the following command:

python notes.py


Available options:

Add a new note

View existing notes

Exit the application

Running the Graphical Interface Version

Navigate to the project directory

Run the following command:

python notes_gui.py


A graphical window will open where users can write and save notes using a simple and intuitive interface.

Design Decisions

Python was chosen for its simplicity, readability, and wide availability

Timestamp-based filenames ensure unique note storage

Plain text storage improves transparency and accessibility

The GUI is intentionally minimal to prioritize functionality over complexity

No external libraries are used to keep the project lightweight and portable
