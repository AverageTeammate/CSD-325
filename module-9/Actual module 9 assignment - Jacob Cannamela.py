# Jacob Cannamela
# CSD325
# 12/6/2024
# Module 9 Assignment 

import requests
import json



# call the api
response = requests.get("https://pokeapi.co/api/v2/pokemon-form")
print(response.json())

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# display the new formatting
print("\nNew Formatting:\n")
jprint(response.json())