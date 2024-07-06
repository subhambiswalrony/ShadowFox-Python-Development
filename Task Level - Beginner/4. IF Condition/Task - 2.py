'''
Write a program to determine which country a city belongs to. Given
list of cities per country: Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
                                  UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
                                India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
'''

city_country = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}

city_name = input("Enter a city name: ")

if city_name in city_country:
    country = city_country[city_name]
    print(f"{city_name} is in {country}")
else:
    print("City not found in the database.")
