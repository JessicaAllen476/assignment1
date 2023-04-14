import re

# Tokenize function #
def tokenize(TextFilePath):
    # list will hold tokens and be returned later
    tokenList = []

    # open & read text file
    f = open(TextFilePath, 'r')

    # reading file line by line
    currentLine = f.readline()
    while currentLine:
        # find all words (including words with an apostrophe)
        # credit for regex guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet
        words = re.findall(r'[\w\']+', currentLine)

        for word in words:
            # making all words case insensitive
            lowWord = word.lower()
            # making words in list lowercase & replacing their former case sensitive form
            ind = words.index(word)
            words[ind] = lowWord
            
        tokenList += words          # update list of tokens

        currentLine = f.readline()  # moved onto next line

    f.close()   # closes textfile

    return tokenList


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
    # sort dict
    
