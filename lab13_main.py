# Cody Young, Nathan Warren-Acord
# Lab 13
# CST 205
# 2018-12-4

# Problem 1 - Mad Libs
# Takes a source text file, removes some words from its strings, and then prompts
# user for words to create a funny mad lib.

def mad_lib():

    # Original input text file
    input_text = []

    # Dictionary to store words to replace from original text file
    deleted_words = {"noun": ["geek", "Rick and Morty", "Star Wars", "jocks", "bullies", "Funko", "fantasy", "sci-fi",
                              "laugh"],
                     "adjective": ["fleeting", "beady", "black-eyed"],
                     "verb": ["running", "laugh", "living", "owning"],
                     "adverb": ["utterly"],
                     "name": ["Brian", "Hoffman", "Count Dooku"]}

    # Dictionary to store and classify user input words (noun, adverb, adjective, name, etc.)
    user_words = {"noun": [],
                  "adjective": [],
                  "verb": [],
                  "adverb": [],
                  "name": []}

    # Get user prompt for strings (noun, adverb, adjective, etc.), store in lists in dictionary
    for word in deleted_words:
        temp = len(deleted_words[word])
        for value in range(0, temp):
            user_input = input("Enter a {}:".format(word))
            user_words[word].append(user_input)

    # Parse input text file, store as list of separate words (input string)
    with open('article.txt', 'r') as file:
        for sentence in file:
            input_text.append(sentence)

    # For each word in list of user strings, replace word in input string
    for list in deleted_words:
        for word in range(0, len(deleted_words[list])):
            input_text = [w.replace(deleted_words[list][word], user_words[list][word]) for w in input_text]

    for sentence in input_text:
        print(sentence)

    return


mad_lib()



