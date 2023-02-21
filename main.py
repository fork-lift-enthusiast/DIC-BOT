import requests
import json
from pprint import pprint
count = 0
dictionary = open("words_dictionary.json.txt")
for key in dictionary: 
    word = key
    # Call an API
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ word +"?key=207a976f-67d9-4375-b8fd-ce6c8ca3f5bc"
    response = requests.get(url)
    response.raise_for_status() # check for errors

    # Load JSON data into a Python variable.
    jsonData = json.loads(response.text)
    pprint(jsonData)
    
