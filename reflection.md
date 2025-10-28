#  Reflection — inventory_system.py

### Name: Dhruthi Rajesh Kedilaya  
### Date: October 28, 2025  

---

### Overview
In this lab, I performed static code analysis on `inventory_system.py` using **Pylint**, **Flake8**, and **Bandit**.  
The goal was to identify and fix coding style issues, security flaws, and potential best-practice violations.

---

### Process
1. **Initial Scan:**  
   - Ran Bandit, Flake8, and Pylint to find issues.  
   - Identified problems like missing docstrings, unsafe `eval()` usage, unused imports, and improper spacing.  

2. **Fix Phase:**  
   - Added proper docstrings and module comments.  
   - Replaced bare `except` with specific exceptions (`KeyError`).  
   - Removed the dangerous `eval()` call and replaced it with a safe print statement.  
   - Cleaned up code style (PEP8 compliance) — fixed blank lines, indentation, and function naming.  
   - Used logging correctly with lazy `%` formatting.

3. **Re-Scan:**  
   - Reran all three tools and confirmed no major issues remained.  
   - Pylint score improved from **4.60 → 9.39**.  
   - Bandit reported **zero security warnings** after fixes.  
   - Flake8 reported **no style violations**.

---

### Key Learnings
- Static analysis tools help catch subtle bugs and improve readability early.  
- Avoid using unsafe functions like `eval()`.  
- Always handle exceptions specifically instead of using bare `except`.  
- Following **PEP8** makes the code more consistent and easier to maintain.  
- Writing docstrings and using logging properly improves project professionalism.

---

### Conclusion
After all fixes, the code is now secure, readable, and compliant with Python best practices.  
The experience helped me understand how automated tools can enhance both **code quality** and **security**.

**Final Quality Score:** 9.39 / 10  
**No security issues detected.**
