import re
from pathlib import Path

# ---------------------------------------------------------------------------
# YOUR LAYOUT  -  change the names here if you ever want different folders
# ---------------------------------------------------------------------------
LAYOUT = {
    "01_ASSETS": {"Images": {}, "Logos": {}, "Fonts": {}, "References": {}},
    "02_OPEN FILE": {},
    "03_RENDER": {"Preview": {}, "Mockup": {}, "Final": {}},
    "04_PACKAGE": {},
}
# (For lowercase names like your old folders, use: "assets", "open file", "render")


def make_folders(base: Path, tree: dict) -> None:
    for name, children in tree.items():
        path = base / name
        path.mkdir(parents=True, exist_ok=True)
        if children:
            make_folders(path, children)


def clean(name: str) -> str:
    """Remove characters Windows doesn't allow in folder names."""
    return re.sub(r'[<>:"/\\|?*]', "", name).strip()


def main() -> None:
    here = Path(__file__).resolve().parent  # the folder this file is sitting in

    print(f"Creating in: {here}\n")
    name = clean(input("Client / project name: "))

    if not name:
        print("\nNo name entered, nothing created.")
    else:
        project = here / name
        if project.exists():
            print(f"\n'{name}' already exists. Nothing was changed.")
        else:
            make_folders(project, LAYOUT)
            print(f"\nDone! '{name}' is ready.")

    input("\nPress Enter to close...")


if __name__ == "__main__":
    main()
