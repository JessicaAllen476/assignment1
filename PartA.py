import sys
import re

# tokenize function #
def tokenize(textfilepath):
    # stores tokens to be returned later
    returnlist = []

    # open & read file line by line
    f = open(textfilepath, 'r')

    # reading file line by line
    currentline = f.readline()
    while currentline:
        # captures all words with alphanumeric characters, including words with apostrophes
        # credit for regex guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
        words = re.findall(r"[a-zA-Z\'\d]+", currentline)

        for word in words:
            # making all words lowercase
            lowword = word.lower()
            # making words in list lowercase & replacing their previous case sensitive form
            ind = words.index(word)
            words[ind] = lowword

        returnlist += words     # update list of tokens
        currentline = f.readline()  # move onto next line

    f.close     # close file

    return returnlist

# computeWord function #
def computeWordFrequencies(tokenlist):
    # will store key-value pairs of tokens
    returndict = {}

    # entering/updating the frequency of words in dictionary
    for word in tokenlist:
        indict = word in returndict
        # if word is not in returndict, add it to dictionary as first instance
        if indict == False:
            returndict[word] = 1
        # if it is in the dictionary +1 to number of instances
        else:
            freq = returndict.get(word)
            freq += 1
            returndict[word] = freq

    return returndict


# print #
def printFrequencies(tokencountmap) -> None:
    # credit for sorted: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    # sort dictionary alphabetically
    sortMap = sorted(tokencountmap.items())
    # sort dictionary from most repeated to least repeated words
    sortMap = sorted(sortMap, key=lambda x:x[1], reverse=True)

    # printing each key-value pair
    for pair in sortMap:
        print("{} -> {}".format(pair[0], pair[1]))
    
# code below will run only during PartA testing, not when PartA is imported to PartB
if __name__ == "__main__":
    # takes argument from command line, tokenizes it, computes word frequencies, and prints them
    try:
        tokenized = tokenize(sys.argv[1])
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        countfreq = computeWordFrequencies(tokenized)
        printFrequencies(countfreq)