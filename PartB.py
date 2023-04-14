import sys
from PartA import tokenize


'''
Time Complexity: O(n^2) - In this instance, the worst time complexity case within the code is the tokenize function's O(n^2)
complexity. Therefore, this function's time complexity is also O(n^2) since for each text file, each line, and each word, one
iteration of code will be ran for them, respectively.
'''
def intersection(textfile1, textfile2) -> int:
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