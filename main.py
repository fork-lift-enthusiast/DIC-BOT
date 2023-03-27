import requests
import json
from pprint import pprint
file = open("words_dictionary.txt", 'r')

#add to text file 
# def AppendToFile(word, definition):
#     myFile = open("words_plus_definitions ","a") 
#     myFile.write(name + "definition: " +definition + "\n")
#     myFile.close()

# Convert the JSON data into Python object
# Here it is a dictionary
json_data = json.load(file)
file.close
# Check the type of the Python object
# Using type() function 
print(type(json_data))
count = 0
# Iterate through the dictionary
# And print the key: value pairs
while True:
    try: 
        
        for key, value in json_data.items():
            word = f"{key}"


            url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ word +"?key=207a976f-67d9-4375-b8fd-ce6c8ca3f5bc"
            response = requests.get(url)
            response.raise_for_status()
            jsonData = json.loads(response.text)

            shortdefs = jsonData[0].get('shortdef', [])
            definition_str = '\n'.join(shortdefs)

            with open("words_temp.txt", "w") as myFile:
                myFile.write(word + ": " + definition_str)
            print(shortdefs)
            myFile.close()
    except:
        count = count+1
        print(count)
    
    #AppendToFile(word, definition)
   
    
# set = {
#      value,
#      value, 
#      vaue,
#  }
# Close the opened sample JSON file
# Using close() function


