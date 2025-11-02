# 🧩 Lab 5 – Static Code Analysis

## 🎯 Objective

To enhance Python code quality, security, and style by using **static analysis tools**:*Pylint*, *Bandit*, and *Flake8* to detect and fix common programming issues in the given `inventory_system.py` file.

---

## 🧰 Tools Used

| Tool       | Purpose                                                   |
| ---------- | --------------------------------------------------------- |
| **Pylint** | Detects code quality, logical errors, and naming issues   |
| **Flake8** | Enforces PEP8 style, spacing, and indentation standards   |
| **Bandit** | Identifies common security vulnerabilities in Python code |

---

## 🧾 Known Issues Table

| **Issue**                                                | **Type**                  | **Tool(s)**                                  | **Line(s)**                                          | **Description**                                                        | **Fix Approach**                                                                                                                                                                               |
| -------------------------------------------------------- | ------------------------- | -------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C0114: Missing module docstring                          | Documentation             | Pylint (C0114)                               | 1                                                    | No docstring (description) at the top of the file                      | Added a short description at the top:<br>`"""Inventory System - A simple demo for static code analysis lab."""`                                                                                |
| Missing function docstrings                              | Documentation             | Pylint (C0116)                               | Multiple (each function definition)                  | Functions did not have descriptive docstrings explaining their purpose | Added one-line docstrings for every function such as:<br>`def add_item(item="default", qty=0, logs=None):`<br>`    """Add quantity of an item to the inventory."""`                            |
| Function naming not in snake_case                        | Style / Naming Convention | Pylint (C0103)                               | All function definitions (addItem, removeItem, etc.) | Function names violated PEP8 naming conventions                        | Renamed all functions and updated calls:<br>`def add_item(...), def remove_item(...), def get_qty(...), def load_data(...), def save_data(...), def print_data(...), def check_low_items(...)` |
| Dangerous default value `[]`                             | Bug / Logic               | Pylint (W0102)                               | Function definition of `add_item`                    | Mutable default list persisted across function calls                   | Changed to:<br>`def add_item(item="default", qty=0, logs=None):`<br>`    if logs is None: logs = []`                                                                                           |
| Improper spacing and blank lines between functions       | Style / Formatting        | Flake8 (E302, E305)                          | Between function definitions                         | Functions were not separated by two blank lines as per PEP8            | Added two-line gaps between functions                                                                                                                                                          |
| Missing encoding when opening files                      | Security                  | Pylint (W1514, R1732)                        | `load_data()`, `save_data()`                         | Files opened without specifying encoding or context managers           | Added encoding and context managers:<br>`with open(file, "r", encoding="utf-8") as f:`                                                                                                         |
| Unused import logging                                    | Code Quality              | Pylint (W0611), Flake8 (F401)                | 2                                                    | `logging` module imported but unused                                   | Used logging in `add_item()`:<br>`logging.basicConfig(level=logging.INFO)`<br>`logging.info("Item added successfully")`                                                                        |
| Bare except block                                        | Code Quality / Security   | Pylint (W0702), Flake8 (E722), Bandit (B110) | `remove_item()`                                      | Catching all exceptions silently                                       | Replaced with specific exception type:<br>`except KeyError:`                                                                                                                                   |
| Use of eval() (unsafe function)                          | Security                  | Bandit (B307)                                | `main()`                                             | `eval()` executes arbitrary code, posing security risk                 | Removed `eval("print('eval used')")`                                                                                                                                                           |
| Use of % string formatting instead of f-strings          | Readability               | Pylint (C0209)                               | `add_item()`                                         | Outdated string formatting method used                                 | Replaced with f-string:<br>`logs.append(f"{datetime.now()}: Added {qty} of {item}")`                                                                                                           |
| Iterating over dictionary keys instead of using .items() | Code Quality              | Pylint (C0206)                               | 54 & 61                                              | Iterated only keys instead of key-value pairs                          | Updated loops:<br>`for item, qty in stock_data.items(): print(f"{item} -> {qty}")`<br>`for item, qty in stock_data.items(): if qty < threshold: result.append(item)`                           |

---

## Reflection questions:

### 1️. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues were adding docstrings, fixing spacing, and renaming functions to follow `snake_case`. The problems were straightforward and were mainly documentation changes.
The hardest issues were related to handling mutable default arguments and restructuring file operations with context managers because of how Python handles mutable objects and resource management.

---

### 2️. Did the static analysis tools report any false positives?

There were no clear false positives. However, some style suggestions such as iterating with `.items()` were technically optional.They did not cause bugs, but improved efficiency.

---

### 3️. How would you integrate static analysis tools into your actual software development workflow?

Static analysis tools like **Pylint**, **Bandit**, and **Flake8** can be integrated into a **Continuous Integration (CI)** pipeline using GitHub Actions or pre-commit hooks.
Each commit or pull request could automatically run these tools to ensure that no new code violates style or security guidelines before merging.

---

### 4️. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes:

* The code became more **readable**, **consistent**, and **secure**.
* Potential runtime errors from unsafe `eval()` and bare `except:` blocks were eliminated.
* File operations became more **robust** with proper encoding and resource handling.
* Logging replaced print statements for better monitoring.
* The new code is up to date with the **PEP8 standards**, improving maintainability and efficiency of the code.

---

## Final Deliverables

The repository contains the following files:

```
inventory_system.py : old file with errors
pylint_report.txt : pylint report of the old inventory_system file
bandit_report.txt : bandit report of the old inventory_system file
flake8_report.txt : flake8 report of the old inventory_system file

cleaned_inventory_system.py : new final file with all the necessary changes
pylint_cleaned_report.txt : pylint report of the new cleaned_inventory_system file
bandit_cleaned_report.txt : bandit report of the new cleaned_inventory_system file
flake8_cleaned_report.txt : flake8 report of the new cleaned_inventory_system file

README.md : README file lissues of the code + Reflection questions based on the project
```

---

## ✅ Conclusion

Through this lab, I learned how static code analysis ensures **quality, security, and maintainability**.
By using **Pylint, Flake8, and Bandit**, I identified and resolved a wide range of issues — from naming and documentation to logic and security.
The process reinforced the importance of automated analysis tools in maintaining high coding standards for any software project.
