'''
Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

height = input("Enter height in meters: ")
weight = input("Enter weight in kilograms: ")

if height.replace(".", "", 1).isdigit() and weight.replace(".", "", 1).isdigit():
    height = float(height)
    weight = float(weight)
    bmi = weight / (height ** 2)

    if bmi >= 30:
        category = "Obesity"
    elif 25 <= bmi < 30:
        category = "Overweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    else:
        category = "Underweight"

    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
else:
    print("Invalid input. Please enter valid numeric values.")
