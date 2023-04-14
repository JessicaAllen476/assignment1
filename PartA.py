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

    return tokenCountMap


# print #
def printFrequencies(TokenCountMap) -> None:
    # sort dict
    
