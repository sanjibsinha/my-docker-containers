Let's build a BMI calculator in Python, focusing on clarity, modularity, and explaining the syntax as we go.

```python
# Module: bmi_calculator.py

def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms (float).
        height_m: Height in meters (float).

    Returns:
        BMI value (float) or a string indicating an invalid input.
    """
    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        return "Invalid weight input. Weight must be a positive number."
    if not isinstance(height_m, (int, float)) or height_m <= 0:
        return "Invalid height input. Height must be a positive number."

    bmi = weight_kg / (height_m ** 2)  # ** is the exponentiation operator
    return bmi


def interpret_bmi(bmi):
    """Interprets the BMI value and returns a category.

    Args:
        bmi: The BMI value (float).

    Returns:
        A string representing the BMI category.
    """
    if not isinstance(bmi, (int, float)): #check if bmi is a number
        return "Invalid BMI value for interpretation."

    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:  # Combined comparison
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def get_user_input():
    """Gets weight and height input from the user.

    Returns:
        A tuple containing weight (kg) and height (m) or None if input is invalid.
    """
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_cm = float(input("Enter your height in centimeters: "))
        height_m = height_cm / 100  # Convert cm to meters
        return weight_kg, height_m
    except ValueError: # handle non-numeric inputs
        print("Invalid input. Please enter numbers only.")
        return None



def display_result(bmi, category):
    """Displays the calculated BMI and category.

    Args:
        bmi: The calculated BMI value.
        category: The BMI category.
    """
    if isinstance(bmi, str): # if bmi is a string, then it is an error message
        print(bmi) # print the error message
    else:
        print(f"Your BMI is: {bmi:.2f}")  # f-strings for formatted output
        print(f"You are classified as: {category}")



# --- Main part of the script (usually in a separate file or at the bottom of this one) ---
if __name__ == "__main__":  # Ensures this runs only when the script is executed directly
    user_input = get_user_input()

    if user_input: # if there is a valid input
        weight, height = user_input # unpacking the tuple
        bmi = calculate_bmi(weight, height)
        if not isinstance(bmi, str): # if bmi calculation was successful
           category = interpret_bmi(bmi)
           display_result(bmi, category)
        else:
            display_result(bmi, "") # display the error message from bmi calculation
```

**Explanation and Key Python Concepts:**

1.  **Modules:** The code is organized into functions, which act as mini-modules within the script.  This makes the code reusable and easier to understand.  If you were to put these functions in a separate file (e.g., `bmi_calculator.py`), you could then import them into another script.

2.  **Functions:**
    *   `def function_name(arguments):`: Defines a function.
    *   `"""Docstring"""`:  A multi-line string used for documenting the function.  Good practice!
    *   `return value`: Returns a value from the function.

3.  **Data Types:**
    *   `int`: Integer (e.g., 10).
    *   `float`: Floating-point number (e.g., 3.14).
    *   `str`: String (e.g., "hello").
    *   `tuple`: An ordered, immutable sequence of items. We use it to return multiple values from the `get_user_input()` function.

4.  **Operators:**
    *   `/`: Division.
    *   `**`: Exponentiation (power).
    *   `=`: Assignment.
    *   `==`: Equality comparison.
    *   `<=`, `<`, `>=`, `>`: Comparison operators.

5.  **Conditional Statements:**
    *   `if condition:`: Executes a block of code if the condition is true.
    *   `elif condition:`:  (Else if) Checks another condition if the previous `if` or `elif` conditions were false.
    *   `else:`: Executes a block of code if all previous conditions were false.

6.  **Input/Output:**
    *   `input("prompt")`: Gets input from the user (always returns a string).
    *   `print(value)`: Prints a value to the console.

7.  **Type Conversion:**
    *   `float(value)`: Converts a value to a float.
    *   `int(value)`: Converts a value to an integer (if possible).

8.  **Error Handling:**
    *   `try...except ValueError:`:  Handles potential `ValueError` exceptions that can occur when converting user input (e.g., if they enter text instead of a number).

9.  **String Formatting:**
    *   `f-strings`:  `print(f"Your BMI is: {bmi:.2f}")`  Allows you to embed variables directly into strings.  `.2f` formats the BMI to two decimal places.

10. **`if __name__ == "__main__":` Block:** This is crucial.  It ensures that the code within this block only runs when you execute the script directly (e.g., `python bmi_calculator.py`), and not when you import the functions into another script. This is good practice for creating reusable modules.

**How to Run:**

1.  Save the code as `bmi_calculator.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using `python bmi_calculator.py`.

Now you have a well-structured and documented BMI calculator!  You can easily extend it by adding more features (e.g., storing BMI history, providing personalized advice based on BMI, etc.) because of its modular design. Let me know if you have any other questions.
