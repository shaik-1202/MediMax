import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to ensure exist
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "test.py"
]

# Iterate over the list of files
for filepath in list_of_files:
    # Create a Path object
    filepath = Path(filepath)
    
    # Get the directory and filename
    filedir, filename = os.path.split(filepath)
    
    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Check if the file exists and is not empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        # Create the file if it doesn't exist or is empty
        with open(filepath, "w") as f:
            f.write("# This is an auto-generated file.\n")
            logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")