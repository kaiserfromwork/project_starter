# Project Starter

---

### **Project Plan: `Project Starter`**

Project Objective:

- A script to automate the initial steps of a new coding project that is hosted on GitHub.

---

### **1. Scope and Goals**

**Minimum Viable Product (MVP):**

- Core Functionality
    - This script automatically creates a new GitHub repository with a standard files:
        - README.md
        - .gitignore
    - This script setups a virtual environment for development.
    - This script creates a predefined core structure of folders and files.
    - This script setups a CI environment using ruff, pytest with coverage check.
    - This script deals with python based projects.
    - This script makes the initial commit and push to the GitHub repository
- Error Handling
    - This script will notify the user about any errors that occurs during the automation process.
    - The next step will only be completed once the current steps is done.
    - Any errors during the run time of the script will interrupt the process.
    - Any errors will be logged and made available for the user.

**Future Features:**

- Allow the user to decide between difference code language
- Allow the user to customize certain specs of the folder structure and CI environment

---

### **2. Research and Design**

**Technology Stack:**

- **Language: Python**
- **Libraries/Tools:**
    - GitHub API
    - Ruff, Pytest and coverage check for CI integration
    - bash

**Interface Design (User Experience):**

- A popup notification once is completed or fails.
- In case of features beyond MVP:
    - User will be able to customize what folders, languages, CI structure the script will create.

---

### **3. Development Plan**

**Environment Control:**

- Virtual Environment to manage dependencies and avoid conflict.

**Version Control:**

- GitHub:
    - Workflow: Create branches to implement new features, and after review, merge them into the main development branch.

**Task List :**

- **To Do (MVP):**
    - Create a GitHub repository using GitHub API
    - Notify if repository was successfully created or not.
    - Create standard files like:
        - README.md
        - .gitignore
    - Clone the repository locally
    - Create a Virtual Environment
    - Create standard structure folder and files
        - main.py
        - pyproject.toml
        - test/
        - github/workflow/
            - python.yml
        - requirements.txt
    - Commit changes to the pository
        - git add .
        - git commit -m “commit message”
        - git push
    - Notify that script automated the project start setup successfully

---

### **4. Execution and Testing**

**Development Process:**

- Built test incrementally feature by feature until MVP.
- Test Driven development.
- Once MVP is implemented will refactor and implement more functionalities
- Use ruff for linting and formatting
