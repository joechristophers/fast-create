#!/usr/bin/env python3

import os
import sys
import shutil

def create_project_structure(project_name):
    
    temp_dir = 'temp'

    os.makedirs(project_name, exist_ok=True)
    for item in os.listdir(temp_dir):
        source = os.path.join(temp_dir, item)
        destination = os.path.join(project_name, item)

        if os.path.isdir(source):
            shutil.copytree(source, destination, dirs_exist_ok=True)
        else:
            shutil.copy2(source, destination)

    shutil.copy(project_name, )


    print(f"FastAPI project '{project_name}' created successfully!")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "new":
        print("Usage: fast-create new <project_name>")
        sys.exit(1)

    project_name = sys.argv[2]
    create_project_structure(project_name)

if __name__ == "__main__":
    main()
