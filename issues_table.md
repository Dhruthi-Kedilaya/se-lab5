# Issues Table — inventory_system.py

## Bandit Security Report

| Issue ID | Description | Severity | Location | Fix Implemented | Status |
|-----------|--------------|-----------|-----------|-----------------|---------|
| B110 | `try-except-pass` detected | Low | Line 19 | Added proper exception handling and logging | Fixed |
| B307 | Use of `eval()` (potential code injection) | Medium | Line 59 | Removed `eval()` and replaced with a safe print statement | Fixed |
| - | No further issues detected | - | - | - | Final Scan Clean |

**Final Bandit Result:** No issues identified.

---

## Flake8 Style Report

| Issue Code | Description | Location | Fix Implemented | Status |
|-------------|--------------|-----------|-----------------|---------|
| F401 | Unused import `logging` | Line 2 | Used `logging` in exception handling | Fixed |
| E302 | Expected 2 blank lines between functions | Multiple | Added proper spacing | Fixed |
| E722 | Bare `except` detected | Line 19 | Replaced with `except KeyError` | Fixed |
| E501 | Line too long | Line 40 | Broke into two lines | Fixed |
| E303 | Too many blank lines | Line 46 | Adjusted blank lines | Fixed |
| W292 | No newline at end of file | Line 61 | Added newline | Fixed |

**Final Flake8 Result:** No errors reported.

---

## Pylint Code Quality Report

| Issue Code | Description | Location | Fix Implemented | Status |
|-------------|--------------|-----------|-----------------|---------|
| C0114 | Missing module docstring | Top of file | Added module-level docstring | Fixed |
| C0116 | Missing function docstrings | Multiple | Added docstrings for all functions | Fixed |
| C0103 | Non-snake_case function names | Multiple | Changed to `snake_case` naming | Fixed |
| W0702 | Bare except used | Line 19 | Replaced with specific exception type | Fixed |
| W0123 | Use of `eval()` | Line 59 | Removed unsafe `eval()` usage | Fixed |
| W1203 | Logging f-string interpolation | Lines 30, 40 | Switched to lazy `%` formatting | Fixed |
| W0603 | Global statement used | Line 52 | Justified use (for shared state) | Acknowledged |
| C0304 | Final newline missing | End of file | Added newline | Fixed |

**Pylint Score:**
- Before Fixes: **4.60 / 10**
- After Fixes: **9.39 / 10**

*All major issues fixed and code quality greatly improved.*

---

## Summary
All three tools (Bandit, Flake8, and Pylint) now report **no major issues**.  
Final code follows PEP8 standards, uses safe exception handling, and avoids security risks.
