import sys
from PartA import tokenize


def intersection(textfile1, textfile2):
    # tokenizing files
    tfile1 = tokenize(textfile1)
    tfile2 = tokenize(textfile2)

    # finding the intersection
    # credit: https://docs.python.org/2/library/sets.html
    returnlist = set(tfile1).intersection(tfile2)
    
    interwords = len(returnlist)    # number of intersecting words

    # printing the number of intersecting words
    print(interwords)

    # returning the number of intersecting words
    return interwords


# code below will only be executed when PartB.py is run #
if __name__ == "__main__":
    try:
        intersection(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        print("Error: File not found.")