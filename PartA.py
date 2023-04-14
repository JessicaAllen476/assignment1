import sys
import re

# checks if word is a contraction
def isContraction(word) -> bool:
    if ("'" in word):
        return True
    else:
        return False

# removes apostrophe and combines into one token
def shortenContraction(cword):
    return cword.replace("'", "")

def tokenize(textfilepath):
    # stores tokens to be returned later
    returnlist = []

    # open & read file
    f = open(textfilepath, 'r')

    # reading file line by line
    currentline = f.readline()
    while currentline:
        # captures all words with alphanumeric characters, including words with apostrophes
        # credit for regex guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
        words = re.findall(r"[a-zA-Z\'\d]+", currentline)

        for word in words:
            # check if the word is a contraction
            if (isContraction(word) == True):
                word = shortenContraction(word)
            # adding word to list of words
            # additionally, making word lowercase to avoid case sensitivities
            returnlist.append(word.lower())

        currentline = f.readline()  # move onto next line

    f.close     # close file

    return returnlist


def computeWordFrequencies(tokenlist):
    # will store key-value pairs of tokens
    returndict = {}

    # entering/updating the frequency of words in dictionary
    for word in tokenlist:
        indict = word in returndict
        # if word is not in returndict, add it to dictionary as its first instance
        if indict == False:
            returndict[word] = 1
        # if it is in the dictionary, +1 to its number of instances
        else:
            freq = returndict.get(word)
            freq += 1
            returndict[word] = freq

    return returndict



def printFrequencies(tokencountmap) -> None:
    # credit for sorted: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    # sort dictionary alphabetically
    sortMap = sorted(tokencountmap.items())
    # sort dictionary from most repeated to least repeated words
    sortMap = sorted(sortMap, key=lambda x:x[1], reverse=True)

    # printing each key-value pair
    for pair in sortMap:
        print("{} -> {}".format(pair[0], pair[1]))

    
# code below will run only run during PartA.py execution #
if __name__ == "__main__":
    # takes argument from command line, tokenizes it, computes word frequencies, and prints them
    try:
        tokenized = tokenize(sys.argv[1])
    except FileNotFoundError:
        # prints an error message if an invalid text file name is given at the command line
        print("Error: File not found.")
    else:
        # if inputted correctly, executes the code
        countfreq = computeWordFrequencies(tokenized)
        printFrequencies(countfreq)