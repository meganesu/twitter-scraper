import json

# Load the data from the JSON file into a dictionary named tweets
tweets = json.load(open('tweets.json'))

for t in tweets:
  print(t["text"])
