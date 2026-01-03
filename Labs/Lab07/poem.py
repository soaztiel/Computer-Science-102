# Author: Anthony Cavallo
# Date: 11/09/2025
# Description: Reads a poem file and writes summary
# Code of honesty: I certify that this lab is entirely my own work.
def main():
    filename = "Snowball.txt"

    try:
        infile = open(filename, "r")
    except:
        print("Could not find the file:", filename)
        return

    title = infile.readline().strip()
    author = infile.readline().strip()

    lines = []
    for line in infile:
        line = line.strip()
        if line != "":
            lines.append(line)
    infile.close()

    outfile = open("poem_output.txt", "w")
    outfile.write("Title: " + title + "\n")
    outfile.write("Author: " + author + "\n")
    outfile.write("Number of lines: " + str(len(lines)) + "\n\n")
    outfile.write("First 3 lines:\n")

    for i in range(min(3, len(lines))):
        outfile.write(str(i + 1) + ". " + lines[i] + "\n")

    outfile.close()

    print("File poem_output.txt has been created.")
main()

