# 2D Project Folder Creator

A simple Python script that automatically creates a clean and organized folder structure for 2D graphic design projects.

I made this for my own design workflow to avoid manually creating the same folders every time I start a new client/project.

## Folder Structure

```text
PROJECT NAME/
├── 01_ASSETS/
│   ├── Images/
│   ├── Logos/
│   ├── Fonts/
│   └── References/
├── 02_OPEN FILE/
├── 03_RENDER/
│   ├── Preview/
│   ├── Mockup/
│   └── Final/
└── 04_PACKAGE/
```

## What It Does

The script:

- Asks for the client/project name
- Automatically creates the project folder
- Creates all required subfolders
- Removes characters that Windows doesn't allow in folder names
- Prevents overwriting an existing project folder
- Keeps the folder structure consistent across projects

## Files

```text
2D Project.py
```

The main Python script that creates the folder structure.

```text
Create 2D Project.bat
```

A Windows batch file that allows you to launch the Python script by simply double-clicking it.

## Requirements

- Python 3.x
- Windows

No external Python libraries are required.

## How to Use

### Option 1 — Using the BAT file

The easiest way to use it:

1. Download both files from this repository.
2. Keep the `.py` and `.bat` files in the same folder.
3. Double-click `Create 2D Project.bat`.
4. Enter your client/project name when prompted.
5. The folder structure will be created automatically.

### Option 2 — Running the Python file

You can also run the Python script directly from Command Prompt or PowerShell:

```bash
python "2D Project.py"
```

Then enter the client/project name when prompted.

Example:

```text
Client / project name: ABC Brand Diwali
```

The script will create:

```text
ABC Brand Diwali/
├── 01_ASSETS/
├── 02_OPEN FILE/
├── 03_RENDER/
└── 04_PACKAGE/
```

## Customization

The folder structure can be changed from the `LAYOUT` section of the script.

```python
LAYOUT = {
    "01_ASSETS": {"Images": {}, "Logos": {}, "Fonts": {}, "References": {}},
    "02_OPEN FILE": {},
    "03_RENDER": {"Preview": {}, "Mockup": {}, "Final": {}},
    "04_PACKAGE": {},
}
```

You can rename, add, or remove folders according to your own workflow.

## Why I Made This

As a graphic designer, I often create multiple projects for different clients. Creating the same folder structure manually for every project becomes repetitive.

This little script saves a few steps and helps keep projects organized from the beginning.

## License

Feel free to use, modify, and adapt the script for your own workflow.
