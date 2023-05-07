import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

while True:
    project_name = input("Enter project name: ")
    if project_name != "":
        break

logging.info(f"Creating project {project_name}")

# List of files

list_of_files = [
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f'test/__init__.py',
    f'test/unit/__init__.py',
    f'test/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'setup.py',
    'project.yoml',
    'setup.cfg',
    'tox.ini',
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file {filepath}")
    
    else:
        logging.info(f"File {filepath} already exists")