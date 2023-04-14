from PartA import tokenize

# intersection #
def intersection(TextFile1, TextFile2):
    # tokenizing files
    tfile1 = tokenize(TextFile1)
    tfile2 = tokenize(TextFile2)

    # finding the intersection
    # credit: https://docs.python.org/2/library/sets.html
    returnlist = set(tfile1).intersection(tfile2)

    # return the number of intersecting words
    return len(returnlist)