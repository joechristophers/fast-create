#!/usr/bin/env python3

import os
import sys

def create_project_structure(project_name):
    base_dirs = [
        "models",
        "schemas",
        "auth",
        "database",
        "security",
        "routers",
        "utilities"
    ]
    auth_files = ["login.py", "signup.py", "oauth2.py", "auth_token.py"]
    security_files = ["hashing.py"]
    database_files = ["database.py"]
    middleware_file = "middleware.py"
    app_file = "app.py"

    os.makedirs(project_name, exist_ok=True)

    for directory in base_dirs:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    # Creating auth files
    for file in auth_files:
        open(os.path.join(project_name, "auth", file), "w").close()

    # Creating security files
    for file in security_files:
        open(os.path.join(project_name, "security", file), "w").close()

    # Creating database files
    for file in database_files:
        open(os.path.join(project_name, "database", file), "w").close()

    # Creating middleware file
    open(os.path.join(project_name, middleware_file), "w").close()

    # Creating main app file
    open(os.path.join(project_name, app_file), "w").close()

    print(f"FastAPI project '{project_name}' created successfully!")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "new":
        print("Usage: fast-create new <project_name>")
        sys.exit(1)

    project_name = sys.argv[2]
    create_project_structure(project_name)

if __name__ == "__main__":
    main()
