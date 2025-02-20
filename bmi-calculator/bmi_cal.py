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