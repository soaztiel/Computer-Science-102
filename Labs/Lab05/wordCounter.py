# Author: Anthony Cavallo
# Date: 10/14/2025
# Description: A simple word counter.
# Code of honesty: I certify that this lab is entirely my own work.

text = input("Enter a series of text or paragraphs: ")

text = text.lower()

text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")
text = text.replace(";", "")
text = text.replace(":", "")
text = text.replace("'", "")
text = text.replace('"', "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count.keys()):
    print(word, ":", word_count[word])

print("Thank you for using the word count program!")