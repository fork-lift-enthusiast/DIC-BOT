"""
import requests
import json
from pprint import pprint
<<<<<<< Updated upstream
dictionary = open("words_dictionary.json.txt")
print(type(dictionary))
# for key in dictionary: 
#     # word = key
    
    
    
#     print(key)
'''
# Call an API
url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ word +"?key=207a976f-67d9-4375-b8fd-ce6c8ca3f5bc"
response = requests.get(url)
response.raise_for_status() # check for errors
# Load JSON data into a Python variable.
jsonData = json.loads(response.text)
pprint(jsonData)
'''
=======
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
    word = f"{key}"
    print(word)
 #  set = {
#      value,
#      value, 
#      vaue,
#  }
# Close the opened sample JSON file
# Using close() function
file.close()

import requests
proxy_servers = {
    'http': 'http://proxy.sample.com:8080',
    'https': 'http://secureproxy.sample.com:8080'
}
s = requests.Session()
s.proxies = proxy_servers
response = s.get('https://trends.google.com/home?geo=US')
import pandas as pd 
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
print("test")


words = ['melancholy']
# payload
pytrends.build_payload(words, cat=0, timeframe='today 12-m')


pytrends.build_payload(kw_list=['pizza', 'bagel'], timeframe=['2022-09-04 2022-09-10', '2022-09-18 2022-09-24'])
print(pytrends.multirange_interest_over_time())

"""

import json
from pytrends.request import TrendReq

# Set up the pytrends client with your authentication credentials
pytrends = TrendReq()

# Read the JSON file and parse it
with open('words_dictionary.json.txt') as f:
    try:
        data = json.load(f)
    except ValueError as e:
        print("Error parsing JSON file:", str(e))
        exit()

# Extract all the words from the data
words = []
for item in data:
    if not isinstance(item, dict):
        print("Error: item is not a dictionary:", item)
        continue
    if 'words' not in item:
        print("Error: 'words' key not found in item:", item)
        continue
    words.extend(item['words'])

# Retrieve the trends data for each word
trends_data = {}
for word in words:
    pytrends.build_payload([word], timeframe='today 5-y')
    interest_over_time_df = pytrends.interest_over_time()
    if interest_over_time_df.empty:
        # No data available for the word
        continue
    # Calculate the average score for the word
    average_score = interest_over_time_df[word].mean()
    trends_data[word] = average_score

# Create a dictionary with words that have an average score less than 10
result = {word: score for word, score in trends_data.items() if score < 10}

# Print the resulting dictionary
print(result)