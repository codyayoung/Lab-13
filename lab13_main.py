# Cody Young, Nathan Warren-Acord
# Lab 13
# CST 205
# 2018-12-4

# Problem 1 - Mad Libs
# Takes a source text file, removes some words from its strings, and then prompts
# user for word to create a funny mad lib.

def mad_lib():

    # Original input text file
    input_text = []

    # Dictionary to store words to replace from original text file
    deleted_words = {"noun": ["geek", "Rick and Morty", "Star Wars", "jocks", "bullies", "Funko", "fantasy", "sci-fi"],
                     "adjective": ["fleeting", "beady", "black-eyed"],
                     "verb": ["running", "laugh", "living", "owning"],
                     "adverb": ["utterly"],
                     "name": ["Brian", "Hoffman", "Count Dooku"]}

    # Dictionary to classify user input words (noun, adverb, adjective, name, etc.)
    user_words = {"noun": [],
                  "adjective": [],
                  "verb": [],
                  "adverb": [],
                  "name": []}

    # Parse input text file, store as list of separate words (input string)
    with open('article.txt', 'r') as file:
        for sentence in file:
            for word in sentence.split():
                input_text.append(word)

    # Get user prompt for strings (noun, adverb, adjective, etc.), store in lists in dictionary
    for word in deleted_words:
        

    # For each word in list of user strings, replace word in input string
    # Return resulting string
    return






