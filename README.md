```markdown
# Terminal Directory Tree Explorer

A simple Python script that scans a directory and visually prints all of its folders, subfolders, and files in a formatted, color-coded structure in your terminal.

---

## Features

* Recursive Scanning: Automatically looks inside folders and all of their subfolders.
* Color-Coded Output: Uses the colorama library to highlight items in your terminal:
  * Yellow: Folders
  * Cyan: Files
  * Green: User Prompts
  * Red: Permission Errors
* Visual Indentation: Indents nested folders so you can easily see the structure of your files.
* Error Handling: Catches permission errors so the script does not crash if a folder is locked or restricted.

---

## Requirements and Setup

### 1. Python
Make sure Python 3 is installed on your computer. You can check by running:

```bash
python --version

```

### 2. Install Required Dependencies

This script uses the `colorama` library for colorful text. Install it using pip:

```bash
pip install colorama

```

---

## How to Use

1. Save the code in a file named `explorer.py` (or your preferred filename).
2. Open your terminal or command prompt in that directory.
3. Run the script:

```bash
python explorer.py

```

4. Type the folder path you want to scan when prompted:

```text
Enter the path: /path/to/your/folder

```

---

## Example Output

```text
Enter the path: my_folder
[FOLDER] src
  [FOLDER] components
    [FILE] App.js
  [FILE] index.js
[FOLDER] docs
  [PERMISSION ERROR] restricted_folder
[FILE] README.md

```

---

## How Code Works

* `explore(path, level)`: Uses Python's built-in `os` module to check if a path is a file or a folder. If it is a folder, it lists everything inside and calls itself again (recursion) with extra indentation space until it reaches every file.
* `main()`: Prompts you to enter a path and starts the recursive scanning process.


