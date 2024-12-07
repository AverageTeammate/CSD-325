# Jacob Cannamela
# CSD325
# 12/6/2024
# Module 9 tutorial assignment 


import requests
import json

# call the api
response = requests.get("http://api.open-notify.org/astros.json")

# print results 
print(response.status_code)

# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())