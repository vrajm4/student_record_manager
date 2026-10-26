import csv
import os
import pickle
import zipfile

TXT_FILE = "activity_log.txt"
CSV_FILE = "students.csv"
PICKLE_FILE = "students.pkl"
ZIP_FILE = "student_backup.zip"


def ensure_files():
    """Create the CSV with a header and the text log if they do not exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll No", "Name", "Course", "Marks"])
    if not os.path.exists(TXT_FILE):
        # Example of writing without a with statement.
        file = open(TXT_FILE, "a", encoding="utf-8")
        file.write("Student Record Manager started.\n")
        file.close()


def add_student():
    roll = input("Roll number: ").strip()
    name = input("Student name: ").strip()
    course = input("Course/branch: ").strip()
    try:
        marks = float(input("Marks (0-100): "))
        if not 0 <= marks <= 100:
            raise ValueError
    except ValueError:
        print("Marks must be a number between 0 and 100.")
        return

    # CSV append mode: existing records are preserved.
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow([roll, name, course, marks])

    # TXT append mode for activity logging.
    with open(TXT_FILE, "a", encoding="utf-8") as file:
        file.write(f"Added student: {roll} - {name}\n")
    print("Student added.")


def view_students():
    # CSV read mode.
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("No student records found.")
        return

    print("\n{:<12} {:<22} {:<18} {:>8}".format("Roll No", "Name", "Course", "Marks"))
    print("-" * 64)
    for row in rows[1:]:
        if len(row) >= 4:
            print("{:<12} {:<22} {:<18} {:>8}".format(*row))


def search_student():
    target = input("Enter roll number to search: ").strip()
    found = False
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            if row["Roll No"].strip().lower() == target.lower():
                print("Found:", row)
                found = True
    if not found:
        print("No matching student.")


def show_text_file_pointer_demo():
    """Demonstrates tell() and seek() with a text file."""
    sample = "file_pointer_demo.txt"
    with open(sample, "w", encoding="utf-8") as file:
        file.write("Python File Handling")

    with open(sample, "r", encoding="utf-8") as file:
        print("\nFile pointer demo")
        print("Initial position:", file.tell())
        print("First 6 characters:", file.read(6))
        print("Position after reading:", file.tell())
        file.seek(0)
        print("After seek(0), position:", file.tell())
        print("Full content:", file.read())


def save_pickle():
    # Load CSV records, then serialize the list of dictionaries into a binary file.
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    with open(PICKLE_FILE, "wb") as file:
        pickle.dump(records, file)
    print(f"Saved {len(records)} record(s) to {PICKLE_FILE} using pickle.")


def load_pickle():
    if not os.path.exists(PICKLE_FILE):
        print("Pickle file not found. Choose 'Save records to pickle' first.")
        return
    # Only unpickle files you trust. Pickle files can execute malicious code.
    with open(PICKLE_FILE, "rb") as file:
        records = pickle.load(file)
    print(f"Loaded {len(records)} record(s) from pickle:")
    for record in records:
        print(record)


def create_zip_backup():
    files_to_backup = [CSV_FILE, TXT_FILE]
    if os.path.exists(PICKLE_FILE):
        files_to_backup.append(PICKLE_FILE)

    with zipfile.ZipFile(ZIP_FILE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in files_to_backup:
            archive.write(filename)
    print(f"Backup created: {ZIP_FILE} ({', '.join(files_to_backup)})")


def unzip_backup():
    if not os.path.exists(ZIP_FILE):
        print("Backup ZIP not found. Create a backup first.")
        return
    output_dir = "unzipped_backup"
    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(ZIP_FILE, "r") as archive:
        archive.extractall(output_dir)
    print(f"Extracted backup files to '{output_dir}'.")


def view_log():
    print("\nActivity log:")
    # Demonstration of read() from a TXT file.
    with open(TXT_FILE, "r", encoding="utf-8") as file:
        content = file.read()
    print(content if content else "(empty log)")


def menu():
    ensure_files()
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search by roll number")
        print("4. Demonstrate tell() and seek()")
        print("5. Save records using pickle")
        print("6. Load records using unpickle")
        print("7. Create ZIP backup")
        print("8. Unzip backup")
        print("9. View activity log")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            show_text_file_pointer_demo()
        elif choice == "5":
            save_pickle()
        elif choice == "6":
            load_pickle()
        elif choice == "7":
            create_zip_backup()
        elif choice == "8":
            unzip_backup()
        elif choice == "9":
            view_log()
        elif choice == "0":
            print("Exiting Student Record Manager.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()
