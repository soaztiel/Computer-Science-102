# Author: Anthony Cavallo
# Date: 11/09/2025
# Description: Counts term frequency from a text file (no stopword removal)
# Code of honesty: I certify that this lab is entirely my own work.

def main():
    filename = "backgammon.txt"
    word_counts = {}

    try:
        infile = open(filename, "r")
    except:
        print("Could not find the file:", filename)
        return

    for line in infile:
        line = line.strip().lower()
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] = word_counts[word] + 1
            else:
                word_counts[word] = 1

    infile.close()

    print("Number of unique words:", len(word_counts))
    print("Word frequencies:\n")

    for word in sorted(word_counts):
        print(word + ":", word_counts[word])

main()