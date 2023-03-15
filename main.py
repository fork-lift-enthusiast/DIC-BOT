import requests
import json
from pprint import pprint
# Open the sample JSON file
# Using the open() function
file = open("words_dictionary.json.txt", 'r')
 #add to text file 
def AppendToFile(word, definition):
    myFile = open("words_plus_definitions ","a") 
    myFile.write(name + "definition: " +definition + "\n")
    myFile.close()

# Convert the JSON data into Python object
# Here it is a dictionary
json_data = json.load(file)
 
# Check the type of the Python object
# Using type() function 
print(type(json_data))
 
# Iterate through the dictionary
# And print the key: value pairs
for key, value in json_data.items():
    word = f"{key}"
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ word +"?key=207a976f-67d9-4375-b8fd-ce6c8ca3f5bc"
    response = requests.get(url)
    response.raise_for_status() # check for errors
        # Load JSON data into a Python variable.
    jsonData = json.loads(response.text)
    try:
        definition = jsonData['shortdef'][0]
    except (TypeError, KeyError):
        print("could not read ")
    # or substitute a placeholder, or raise a new exception, etc.
    pprint(jsonData)
    
    #AppendToFile(word, definition)
   
    
# set = {
#      value,
#      value, 
#      vaue,
#  }
# Close the opened sample JSON file
# Using close() function
file.close()
