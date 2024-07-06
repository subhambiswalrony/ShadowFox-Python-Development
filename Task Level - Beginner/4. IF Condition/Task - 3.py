'''
Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"

Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''


city_to_country = {
    "Mumbai": "India",
    "Chennai": "India",
    "Sydney": "Australia",
    "Dubai": "United Arab Emirates"
}

first_city = input("Enter the first city: ")
second_city = input("Enter the second city: ")

if first_city in city_to_country and second_city in city_to_country:
    if city_to_country[first_city] == city_to_country[second_city]:
        print("Both cities are in", city_to_country[first_city])
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the dictionary.")
