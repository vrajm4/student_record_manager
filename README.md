# Student Record Manager — Python File Handling Mini Project

## Overview
A menu-driven Python application for storing and managing student records. It demonstrates TXT and CSV file operations, file modes, `with` and manual file closing, file pointers (`tell()` / `seek()`), pickling/unpickling, and ZIP backup/extraction.

## Requirements
- Python 3.8 or later
- No third-party packages required

## Run
1. Extract the project folder.
2. Open a terminal in the folder.
3. Run: `python student_record_manager.py`

## Features
1. Add student records to `students.csv`.
2. View all saved students.
3. Search by roll number.
4. Demonstrate `tell()` and `seek()`.
5. Save records as a serialized object in `students.pkl`.
6. Load the serialized records using `pickle`.
7. Compress data files into `student_backup.zip`.
8. Extract the ZIP archive into `unzipped_backup/`.
9. Maintain a text activity log in `activity_log.txt`.

## Concepts covered
- `r`: read an existing file
- `w`: write/create a file (overwrites existing contents)
- `a`: append to a file
- `rb` / `wb`: read/write binary files
- `with open(...)`: automatically closes the file
- `open()` + `close()`: manual file handling
- `csv.reader`, `csv.writer`, `csv.DictReader`
- `tell()`: returns the current file pointer position
- `seek(0)`: moves the pointer to the beginning
- `pickle.dump()` / `pickle.load()`: serialize and deserialize Python objects
- `zipfile.ZipFile`: create and extract ZIP archives

## Safety note
Only unpickle files from trusted sources. A malicious pickle file can execute code when loaded. ZIP extraction should also be restricted to archives you trust.
