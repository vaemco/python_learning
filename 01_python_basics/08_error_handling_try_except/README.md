# Error Handling: Try and Except

This module covers how to handle exceptions in Python to prevent programs from crashing due to runtime errors.

## Contents

- **`division_error_handling.py`**: safe way to perform arithmetic when input might be invalid (e.g., text or division by zero).
- **`roi_error_handling.py`**: demonstrates iterating through a dataset and gracefully skipping bad records.
- **`safe_division.py`**: encapsulates error handling within a function.
- **`salary_calc_error_handling.py`**: advanced example showing type validation and error handling in a salary calculation script.

## Key Concepts

- **Try/Except Blocks**: Catching errors (`ValueError`, `ZeroDivisionError`, `TypeError`) before they crash the script.
- **Else Block**: Running code only if no error occurred.
- **Data sanitization**: Robustly processing lists of dictionaries that may contain malformed data.
