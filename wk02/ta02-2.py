def prompt_filename():
    return input("Enter filename: ")


def main():
    filename = prompt_filename()
    print("Opening file", filename)
    parse_file(filename)


def parse_file(file):
    readfile = open(file, "r")
    for line in readfile:
        print(line)
        words = line.split()
        for i in words:
            print(words[i])
    readfile.close()


if __name__ == "__main__":
    main()
