# wordcount.py
# Count the number of lines, words, and characters in a text file.


def wordcount(filename):

    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()


    wrds = data.count(" ") + 1
    char = len(data) + 1

    print("Processing file:", fname)
    print("Characters:", char)
    print("Wordcount:", wrds)

