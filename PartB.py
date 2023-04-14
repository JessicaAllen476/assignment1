import sys
from PartA import tokenize

# intersection #
def intersection(textfile1, textfile2):
    # tokenizing files
    tfile1 = tokenize(textfile1)
    tfile2 = tokenize(textfile2)

    # finding the intersection
    # credit: https://docs.python.org/2/library/sets.html
    returnlist = set(tfile1).intersection(tfile2)
    printCommonWords(returnlist)

    # return the number of intersecting words
    return len(returnlist)

# printing out intersecting words #
def printCommonWords(intersectionset) -> None:
    print("Common words:")
    # sorting list alphabetically
    sortlist = sorted(intersectionset)
    # printing out list of intersecting words
    for word in sortlist:
        print(word)
    print("\n")

# print out intersection #
def printIntersectionNum(numintersecting):
    print(numintersecting)

# code below will be executed when PartB is run #
if __name__ == "__main__":
    numIntersecting = intersection(sys.argv[1], sys.argv[2])
    printIntersectionNum(numIntersecting)