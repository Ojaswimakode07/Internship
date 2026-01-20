import os
from datetime import datetime

NOTES_FOLDER = "notes"

def create_note():
    if not os.path.exists(NOTES_FOLDER):
        os.mkdir(NOTES_FOLDER)

    content = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"note_{timestamp}.txt"

    with open(os.path.join(NOTES_FOLDER, filename), "w") as file:
        file.write(content)

    print("✅ Note saved successfully")

def view_notes():
    if not os.path.exists(NOTES_FOLDER):
        print("No notes found")
        return

    notes = os.listdir(NOTES_FOLDER)
    if not notes:
        print("No notes available")
        return

    print("\n📄 Saved Notes:")
    for note in notes:
        print("-", note)

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
