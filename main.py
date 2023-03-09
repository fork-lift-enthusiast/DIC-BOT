import requests
import json
from pprint import pprint
# Open the sample JSON file
# Using the open() function
file = open("words_dictionary.json.txt", 'r')
 
# Convert the JSON data into Python object
# Here it is a dictionary
json_data = json.load(file)
 
# Check the type of the Python object
# Using type() function 
print(type(json_data))
 
# Iterate through the dictionary
# And print the key: value pairs
for key, value in json_data.items():
    word = (\n {key}")
    print (word)
 #  set = {
#      value,
#      value, 
#      vaue,
#  }
# Close the opened sample JSON file
# Using close() function
file.close()

