# SE-Lab5

## Static Code Analysis using Pylint, Bandit, and Flake8

### About
This repository contains work for Lab 5 of the Software Engineering course focused on improving Python code quality, security, and style by performing static analysis. The tools used include:

- **Pylint**: for code quality checks and logical errors
- **Flake8**: for enforcing PEP 8 style guidelines and formatting
- **Bandit**: for detecting common security vulnerabilities in Python code

### Contents
- `inventory_system.py`: The Python program analyzed and improved during the lab.
- `pylint_report.txt`: Pylint's static analysis output report.
- `bandit_report.txt`: Bandit's security scan report.
- `flake8_report.txt`: Flake8 style and formatting issues report.
- `issues_table.md`: Documented issues found and their fixes.
- `reflection.md`: Reflections on the static analysis process and learnings.

### Lab Objectives
- Understand and apply static code analysis to Python source code without executing it.
- Identify and fix issues like mutable default arguments, overly broad exceptions, and insecure coding patterns.
- Use Pylint, Bandit, and Flake8 effectively to improve code quality.
- Analyze static reports and prioritize fixes based on issue severity.
- Reflect on how static analysis contributes to maintainability and robustness.

### How to Use
1. Open this repository in GitHub Codespaces or clone locally.
2. Install required tools:
 ```bash
   pip install pylint flake8 bandit
  ```
3.Run analyses
 ```bash
   pylint inventory_system.py
  flake8 inventory_system.py
  bandit -r inventory_system.py

  ```
   
