# Understanding Python Code Organization

## Quick Summary

| What | Description | Example | Need Import? |
|------|-------------|---------|--------------|
| **Built-in Functions** | Always available, no import needed | `print()`, `len()`, `type()` | ❌ No |
| **Standard Library** | Comes with Python, import to use | `import os`, `import json` | ✅ Yes |
| **Script** | `.py` file you run directly | `python hello.py` | ❌ Not usually |
| **Module** | `.py` file you import into other code | `import mycode` | ✅ Yes |
| **Package** | Folder with modules + `__init__.py` | `import mypackage.module` | ✅ Yes |
| **Third-party Library** | Install with pip, then import | `pip install requests` | ✅ Yes |
| **Framework** | Large library that controls your app | Django, Flask | ✅ Yes |

**Key Resources:**
- **Python Standard Library Docs**: https://docs.python.org/3/library/
- **Third-party Packages (PyPI)**: https://pypi.org/

**In a Nutshell:**
1. Python comes with built-in functions (use immediately) and standard library (import to use)
2. For anything else, search PyPI and install with `pip install package-name`
3. A `.py` file is a script when you run it, a module when you import it
4. Packages are folders containing multiple modules organized together

---

## Introduction

When you install Python and start coding, you'll encounter terms like "script," "module," "package," "library," and "framework." Let's start from the very beginning and build up your understanding step by step.

---

## Your First Python Program

After installing Python, let's write the simplest program:

**hello.py**
```python
print("Hello, World!")
```

Run it:
```bash
python hello.py
```

**Question: Is this a script or a module?**

Answer: **It's both!** 
- When you **run** it (`python hello.py`), it's a **script**
- When you **import** it (`import hello`), it's a **module**

The distinction is about **how you use it**, not what it is.

### When Do You Need Import?

At the beginning, you don't! Your first programs will use **built-in functions** that are always available:

```python
# No imports needed - these work immediately
print("Hello")           # Output text
name = input("Name: ")   # Get user input
length = len("Python")   # Get length
number = int("42")       # Convert to integer
```

**Common built-in functions** (no import required):
`print()`, `input()`, `len()`, `type()`, `int()`, `float()`, `str()`, `range()`, `max()`, `min()`, `sum()`, `abs()`, `round()`, `sorted()`

---

## What Python Gives You Out of the Box

When you install Python, you get two levels of built-in functionality:

### 1. Built-in Functions (Always Available)

These work immediately without any import:

```python
print("Hello")
len([1, 2, 3])
type(42)
max(10, 20, 30)
```

### 2. Standard Library (Import to Use)

Python comes with a huge collection of modules for common tasks. You don't install them—just import and use!

**Official Documentation**: https://docs.python.org/3/library/

**Popular Standard Library Modules:**

```python
# Working with files and directories
import os
import shutil

# Dates and times
import datetime
import time

# Data formats
import json
import csv

# Internet and web
import http
import urllib

# Math and randomness
import math
import random

# System utilities
import sys
```

**Example: Using Standard Library**

```python
import datetime
import random

# Get current date
now = datetime.datetime.now()
print(f"Today is {now}")

# Generate random number
number = random.randint(1, 100)
print(f"Random number: {number}")
```

**Why `datetime.datetime`?**

Notice the double `datetime`? Here's why:
- `datetime` (first) = the **package** name (folder)
- `datetime` (second) = the **class** name inside the package

The `datetime` package contains multiple things: `datetime` class, `date` class, `time` class, etc.

```python
import datetime

# Package contains multiple classes
datetime.datetime.now()   # datetime class
datetime.date.today()      # date class
datetime.time(10, 30)      # time class
```

You can also import just the class:
```python
from datetime import datetime

# Now you only need one datetime
now = datetime.now()
```

**No installation needed!** These modules are already on your computer because they come with Python.

---

## When Standard Library Isn't Enough: Third-party Packages

What if you need functionality that Python doesn't include? That's where **third-party packages** come in!

### PyPI: Python Package Index

**Website**: https://pypi.org/

PyPI is the official repository of third-party Python packages. Think of it as an "app store" for Python code. You can search for packages, read documentation, and see usage examples.

### Installing Third-party Packages

Use `pip` (Python's package installer):

```bash
pip install requests     # For HTTP requests
pip install pandas       # For data analysis
pip install flask        # For web applications
```

**Then import and use:**

```python
import requests

response = requests.get('https://api.example.com/data')
print(response.status_code)
```

### How to Find, Install, and Use Third-party Packages

**Step 1: Search PyPI**
- Go to https://pypi.org/
- Search for what you need (e.g., "http requests", "excel files", "pdf")

**Step 2: Read the Package Page**
Each package on PyPI has:
- Description of what it does
- Installation command (usually `pip install package-name`)
- Usage examples
- Link to full documentation
- Version history and dependencies

**Step 3: Install with pip**
```bash
pip install package-name
```

**What Does pip Download?**

When you run `pip install requests`, pip downloads a **distribution** - a packaged bundle containing:
- **Python files** (`.py`) - modules and packages
- **Compiled code** (`.so`, `.pyd`) - binary extensions for performance
- **Metadata** - information about the package (setup.py or pyproject.toml)
- **Documentation** - README, license, etc.

pip installs it to a special folder (`site-packages`) where Python looks for modules.

**Step 4: Import and Use**
```python
import package_name
# or
from package_name import something
```

**Step 5: Learn How to Use It**

Three ways to learn the API:

1. **PyPI Page** - Quick usage examples
2. **Documentation** - Full guide (link on PyPI page)
3. **In Python** - Use `help()`:
   ```python
   import requests
   help(requests.get)  # Shows function documentation
   ```

---

## The Building Blocks in Detail

### 1. Script vs Module: Same File, Different Usage

Any `.py` file can be both a script and a module:

**calculator.py**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

PI = 3.14159

# This is the key pattern
if __name__ == '__main__':
    # This code only runs when executed as a script
    print("Testing calculator...")
    print(f"5 + 3 = {add(5, 3)}")

# let's see what __name__ prints
print(f"__name__ is: {__name__}")
```

**Used as a script:**
```bash
python calculator.py
# Output: 
# Testing calculator...
# 5 + 3 = 8
# __name__ is: __main__
```

**Used as a module:**
```python
import calculator
# Output when importing:
# __name__ is: calculator

# The code inside 'if __name__ == '__main__':' doesn't run
# because __name__ is 'calculator', not '__main__'

result = calculator.add(10, 20)
print(result)  # Output: 30
```

### Understanding `__name__` and `if __name__ == '__main__':`

This is one of Python's most important patterns. To understand it, you first need to know how Python executes scripts.

**How Python Executes Scripts**

When you run `python myfile.py`, Python executes the file **line by line, top to bottom**:

```python
# example.py
print("Line 1 executes")
print("Line 2 executes")

def greet():
    print("This does NOT execute automatically!")

print("Line after function definition executes")
# Note: greet() was never called, so its code never runs
```

**Output when you run `python example.py`:**
```
Line 1 executes
Line 2 executes
Line after function definition executes
```

**Key Point**: Functions are **defined** but not **called** automatically. Only code at the "top level" (not inside functions) runs when you execute the script.

---

**The Problem This Solves**

When you import a module, Python also executes it top to bottom:

```python
# helper.py
def add(a, b):
    return a + b

print("Calculating...")  # Oops! This runs when imported
result = add(5, 3)
print(f"Result: {result}")  # This too!
```

```python
# main.py
import helper  # Output: Calculating... Result: 8
# We didn't want that to run when importing!
```

**The Solution: `if __name__ == '__main__':`**

`__name__` is a special variable Python automatically sets:
- When you **run** the file directly: `__name__` = `'__main__'`
- When you **import** the file: `__name__` = the module name (e.g., `'helper'`)

```python
# helper.py
def add(a, b):
    return a + b

# This only runs when executed directly
if __name__ == '__main__':
    print("Calculating...")
    result = add(5, 3)
    print(f"Result: {result}")
```

Now:
- `python helper.py` → Prints "Calculating..." and "Result: 8"
- `import helper` in another file → Nothing prints, just defines `add()` function

---

**When to Use It**

- ✅ Files that can be both run as scripts AND imported as modules
- ✅ Put test code, examples, or main execution logic inside the if block
- ❌ Not needed in pure library modules that only define functions/classes

**Best Practice Pattern:**
```python
# my_script.py

def process_data():
    """Main work function"""
    print("Processing...")
    return "Done"

def helper_function():
    """Utility function"""
    pass

# Only runs when executed directly, not when imported
if __name__ == '__main__':
    result = process_data()
    print(result)
```

---

### 2. Package: Organizing Multiple Modules

As your project grows, you organize related modules into folders called **packages**.

**Example Structure:**

```
my_math_package/
    __init__.py
    basic.py
    advanced.py
    geometry/
        __init__.py
        shapes.py
        calculations.py
```

**basic.py**
```python
def add(a, b):
    return a + b
```

**geometry/shapes.py**
```python
def circle_area(radius):
    return 3.14159 * radius ** 2
```

**Using the Package:**

```python
# Import module from package
from my_math_package import basic
result = basic.add(5, 3)

# Import directly from nested module
from my_math_package.geometry.shapes import circle_area
area = circle_area(10)

# Import with full path
import my_math_package.geometry.shapes
area = my_math_package.geometry.shapes.circle_area(10)
```

### What is `__init__.py` and When Is It Needed?

**`__init__.py`** is a special file that marks a directory as a Python package.

**Python 3.3+**: `__init__.py` is **optional** for basic packages (called "namespace packages")
**Best Practice**: Still include it for clarity and compatibility

**What Does `__init__.py` Do?**

1. **Empty file** - Just marks the directory as a package
   ```python
   # __init__.py (empty)
   ```

2. **Package initialization** - Run code when package is imported
   ```python
   # __init__.py
   print("Initializing my_math_package...")
   
   # Set package version
   __version__ = "1.0.0"
   ```

3. **Control what's available** - Define package's public API
   ```python
   # my_math_package/__init__.py
   from .basic import add, subtract
   from .advanced import power, root
   
   # Now users can do: from my_math_package import add
   # Instead of: from my_math_package.basic import add
   ```

**When Do You Need `__init__.py`?**

| Situation | Need `__init__.py`? |
|-----------|---------------------|
| Simple package in Python 3.3+ | ❌ Optional (but recommended) |
| Package with initialization code | ✅ Yes |
| Want to control package API | ✅ Yes |
| Python 2.x compatibility | ✅ Yes |
| Professional projects | ✅ Yes (best practice) |

---

### 3. Binary vs Pure Python Modules

You might have noticed some modules don't have `.py` files you can see. What's going on?

**Two Types of Modules:**

1. **Pure Python Modules** - Written in `.py` files
2. **Built-in/Extension Modules** - Compiled into Python binary (written in C)

**Can You Run a Standard Library Module Like `python os.py`?**

Technically yes, but nothing happens! Here's why:

```bash
# Find where os.py is located
python -c "import os; print(os.__file__)"
# Example output: /Users/nitesh.kumar/.pyenv/versions/3.12.0/lib/python3.12/os.py

# Try running it directly
python /Users/nitesh.kumar/.pyenv/versions/3.12.0/lib/python3.12/os.py
# Output: (nothing happens!)

# This is the correct way to use it
python -c "import os; print(os.getcwd())"
```

**Why Does Nothing Happen?**

Remember: **Python executes code line by line, but doesn't call functions automatically.**

Standard library modules like `os.py` only **define** functions and classes - they don't execute anything at the top level:

```python
# Simplified view of os.py structure:

def getcwd():
    """Get current directory"""
    # ... implementation ...

def listdir(path):
    """List directory contents"""
    # ... implementation ...

def mkdir(path):
    """Create directory"""
    # ... implementation ...

# No if __name__ == '__main__': block!
# Just function definitions, no actual execution
```

When you run `python os.py`:
1. Python reads the file top to bottom
2. Defines all the functions (but doesn't call them)
3. Reaches end of file
4. Exits (nothing to output!)

**Contrast with a Script:**

```python
# my_script.py

def process():
    print("Processing...")

# This actually runs when you execute the file
print("Script starting...")
process()
print("Script done!")
```

Running `python my_script.py` outputs text because it has top-level code that executes.

**Key Differences:**

| Type | Has Executable Code? | Run Directly? | Examples |
|------|---------------------|---------------|----------|
| **Library Module** | ❌ Only definitions | ❌ Nothing happens | `os`, `json`, `datetime` |
| **Your Script** | ✅ Yes, with logic | ✅ Executes | `python myscript.py` |
| **Built-in Binary** | N/A (compiled C code) | ❌ No `.py` file | `sys`, `math` |

**Check for yourself:**

```python
import sys
print(sys.__file__)  # Output: (nothing - sys is built-in, no .py file!)

import os
print(os.__file__)   # Shows path to os.py file
```

**Pure Python vs Binary:**

- **Pure Python** (`.py`) - Easy to read and modify, slower
- **Binary/Compiled** (`.so`, `.pyd`, built-in) - Fast, but can't easily read/modify

**Why Use Binary Modules?**
- **Performance** - Math operations, system calls
- **Security** - Harder to modify core Python behavior
- **Integration** - Access C libraries and system APIs

---

### 4. Library and Framework

**Library**: A collection of modules/packages you install and use:
- `requests` - HTTP library
- `pandas` - data analysis
- `pillow` - image processing

**Framework**: A large structure that controls your app:
- **Django** - Full web framework
- **Flask** - Lightweight web framework  
- **PyTorch** - Machine learning framework

**Key Difference:**
- **Library**: You call it
- **Framework**: It calls your code


---

## Import Patterns Explained

### 1. Import Entire Module

```python
import math

result = math.sqrt(16)  # Use with module prefix
print(math.pi)
```

**Use when**: You need multiple things from a module

---

### 2. Import Specific Items

```python
from math import sqrt, pi

result = sqrt(16)  # Use directly, no prefix
print(pi)
```

**Use when**: You only need a few specific functions

---

### 3. Import with Alias

```python
# Standard conventions
import numpy as np
import pandas as pd

# Avoiding long names
from datetime import datetime as dt

# Avoiding conflicts
from math import sqrt as math_sqrt
from numpy import sqrt as np_sqrt
```

**Use when**: 
- Following standard conventions (`np`, `pd`)
- Names are too long
- Avoiding naming conflicts

---

### 4. Import from Packages

```python
# Method 1: Full path
import my_package.module_a
my_package.module_a.function()

# Method 2: Import module
from my_package import module_a
module_a.function()

# Method 3: Import function directly
from my_package.module_a import function
function()
```

---

### ⚠️ Avoid: Import Everything

```python
from math import *  # DON'T DO THIS

# Problems:
# - Unclear what you're importing
# - Can overwrite existing names
# - Makes debugging harder
```

---

## Import Best Practices

### ✅ Organize Your Imports

```python
# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import numpy as np
import pandas as pd

# 3. Your own modules
from my_package import my_module
```

### ✅ Use Standard Aliases

```python
import numpy as np           # ✅ Standard
import pandas as pd          # ✅ Standard
import matplotlib.pyplot as plt  # ✅ Standard
```

### ❌ Common Mistakes

```python
# ❌ Don't name your file same as standard library
# Don't create: math.py, os.py, sys.py

# ❌ Don't use circular imports
# file_a.py imports file_b.py
# file_b.py imports file_a.py

# ❌ Don't import * in production code
from module import *
```

---

## Real-World Example

**data_processor.py**
```python
# Standard library
import json
from datetime import datetime

# Third-party
import pandas as pd
import requests

def fetch_and_process():
    """Fetch data from API and process it"""
    # Fetch
    response = requests.get('https://api.example.com/data')
    data = response.json()
    
    # Process
    df = pd.DataFrame(data)
    df['timestamp'] = datetime.now()
    
    # Save
    df.to_csv('output.csv', index=False)
    print(f"Processed {len(df)} records")

if __name__ == '__main__':
    fetch_and_process()
```

---

## Quick Reference

| Concept | What It Is | Example |
|---------|-----------|---------|
| **Script** | File you run | `python myscript.py` |
| **Module** | File you import | `import mymodule` |
| **Package** | Folder with modules | `import mypackage.module` |
| **Built-in** | No install, no import | `print()`, `len()` |
| **Standard Library** | No install, yes import | `import os`, `import json` |
| **Third-party** | Install + import | `pip install requests` |

---

## Summary: Your Learning Path

```
1. Start → Write simple scripts with built-in functions
           ↓
2. Need more → Import from Standard Library (os, json, datetime)
           ↓
3. Organize → Split your code into modules
           ↓
4. Scale → Group modules into packages
           ↓
5. Extend → Install third-party packages from PyPI
           ↓
6. Share → Package your code for others
```

**Remember:**
- A `.py` file is a **script** when you run it, a **module** when you import it
- Use `if __name__ == '__main__':` to make files work as both
- Standard Library is free and included - explore it! (https://docs.python.org/3/library/)
- For everything else, search PyPI (https://pypi.org/)

Happy coding! 🐍

