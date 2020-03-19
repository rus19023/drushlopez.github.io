#  file_to_open = input("Enter file: ")
readfile = open("census.csv", "r")
num_lines = 0
num_words = 0
for line in readfile:
    num_lines += 1
    words = line.split()
    for i in words:
        num_words += 1
readfile.close()
print("The file contains", num_lines, "lines and", num_words, "words.")
