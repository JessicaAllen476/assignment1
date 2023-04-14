import re

# Tokenize function #
def tokenize(TextFilePath):
    # stores tokens to be returned later
    tokenReturn = []

    # open & read files
    f = open(TextFilePath, 'r')

    # read file line-by-line
    currentLine = f.readline()
    while currentLine:
        # find all words (including words with an apostrophe)
        # credit for regex guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
        words = re.findall(r"[\w\']+", currentLine)

        for word in words:
            # making all words lowercase
            lowWord = word.lower()

            # making words in list lowercase & replacing their former case sensitive forms
            ind = word.index(word)
            words[ind] = lowWord
        
        tokenReturn += words    # update list of tokens

        currentLine = f.readline()  # move onto next line

    f.close()   # close text file

    return tokenReturn



# computeWordFrequencies #
def computeWordFrequencies(TokenList):
    # maps tokens and their count. Will be returned later.
    tokenCountMap = {}

    # entering/updating the frequency of each word in the dictionary
    for word in TokenList:
        inDict = word in tokenCountMap
        
        # if word is not in tokenCountMap, add it to the dictionary as the first instance of it
        if inDict == False:
            tokenCountMap[word] = 1
        # if word exists in tokenCountMap, update the frequency of it
        else:
            freq = tokenCountMap.get(word)
            freq += 1
            tokenCountMap[word] = freq

    return tokenCountMap


# print #
def printFrequencies(TokenCountMap) -> None:
    # sort dictionary from most repeated to least repeated words
    # credit for sorted: https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    sortMap = sorted(TokenCountMap.items(), key=lambda x:x[1], reverse=True)

    # printing each key-value pair
    for pair in sortMap:
        print("{} -> {}".format(pair[0], pair[1]))
    
