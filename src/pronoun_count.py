import json
from typing import Dict, List
import re
from os import listdir
from os.path import isfile, join

# Main function that counts the occurences of specified pronouns from json files of tweets
def analyze(directory_path: str) -> Dict:

    # A dictonary with the relevant pronounces and their occurences
    result: Dict = {
        'han': 0, 
        'hon': 0, 
        'den': 0,
        'det': 0,
        'denna': 0,
        'denne': 0,
        'hen': 0
        }

    # A list of all files in the specified directory
    files: List = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]

    # The program handles one file at a time and updates the result dictonary after each file
    for file_src in files:
        # Parses the jsons from the file
        tweets = parse_json(f'{directory_path}/{file_src}')
        # Returns a dictonary of relevant word occurances from the current file
        file_result = count_relevant_words(tweets, result)
        # Updates the total result with the result of the file
        result.update(file_result)

    return json.dumps(result)

# Function to parse the json file and return a list of parsed tweets
def parse_json(file_src: str) -> List:
    # Initialize a list for all the parsed tweets
    tweets = list()
    
    # Parse the json file
    with open(file_src, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            tweets.append(json.loads(line.strip()))

    return tweets

# Function that counts the relevant words in each file and returns a dictonary with results
def count_relevant_words(parsed_json: List, result: Dict) -> Dict:
    for tweet in parsed_json:
        # Extracts the text part of the tweet
        text: str = tweet['text']
        # Parse the text to a list of words
        word_list = parse_text(text)
        for word in word_list:
            # Makes sure all words are in lowercase to compare them to the result dictonary
            formatted_word = word.lower()
            # If the word in the dictonary key list it's occurence is incremented in the result array
            if formatted_word in result.keys():
                result[formatted_word] += 1
    
    return result

# Parses the text to a list of words.
def parse_text(sentance: str) -> List:
    return re.findall(r'\w+', sentance)

if __name__ == '__main__':
    analyze('data')