import PyInstaller.__main__
import os
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the spec file path
spec_file = os.path.join(current_dir, "BurmeseOCR.spec")

# PyInstaller command line arguments
args = [
    "script.py",  # Your main script file
    "--name=BurmeseOCR",
    "--onefile",  # Create a single executable
    "--windowed",  # Run without console window
    "--add-data=tessdata;tessdata",  # Include Tesseract data files
    "--icon=assets/icon.ico",  # Application icon
    "--clean",  # Clean PyInstaller cache
    "--noconfirm",  # Replace output directory without confirmation
]

# Add any additional data files or dependencies
additional_data = [
    ("assets/*", "assets"),  # Include assets directory
    ("LICENSE", "."),  # Include license file
    ("README.md", "."),  # Include readme
]

for src, dst in additional_data:
    args.extend(["--add-data", f"{src};{dst}"])

# Run PyInstaller
PyInstaller.__main__.run(args)
