import requests
import json

# Open the text file containing the dictionary in read mode
with open("words_dictionary.txt", 'r') as file:
    # Convert the JSON data into Python object
    # Here it is a dictionary
    json_data = json.load(file)

# Create a dictionary to store the words and their definitions
word_dict = {}

# Iterate through the dictionary
# And retrieve the definitions
for word in json_data:
    try:
        # Construct the URL for the API request using the word as a parameter
        url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=207a976f-67d9-4375-b8fd-ce6c8ca3f5bc"

        # Send the request and convert the response to JSON
        response = requests.get(url)
        response.raise_for_status()
        jsonData = response.json()

        # Extract the definition string from the JSON data
        if isinstance(jsonData, list) and len(jsonData) > 0 and isinstance(jsonData[0], dict):
            shortdefs = jsonData[0].get('shortdef', [])
            definition_str = '\n'.join(shortdefs)
        else:
            definition_str = ""

        # Add the word and its definition to the dictionary
        word_dict[word] = definition_str

    except Exception as e:
        print(f"Error occurred: {e}")

# Convert the dictionary to a JSON-formatted string
word_dict_str = json.dumps(word_dict)

# Open a file to store the definitions in write mode
with open("definitions.txt", "w") as def_file:
    # Write the string to the definitions file
    def_file.write(word_dict_str)
