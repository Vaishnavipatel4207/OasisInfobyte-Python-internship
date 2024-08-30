
def calculate_bmi(weight, height):
    """Calculate the BMI using the formula weight (kg) / height (m)^2."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        # Input weight and height from the user
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))
        
        # Validate inputs
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Get classification
        category = classify_bmi(bmi)
        
        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()



