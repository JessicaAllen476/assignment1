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
    
    # printing the number of intersecting words
    interwords = len(returnlist)
    print(interwords)

    # return the number of intersecting words
    return interwords

# code below will be executed when PartB is run #
if __name__ == "__main__":
    try:
        intersection(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        print("Error: File not found.")