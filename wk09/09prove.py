f = open("census.csv", "r")
census = {}

# This was is probably even easier
for line in f:  # gets one line at a time from the file
    print(line)  # we can print it or do anything else we want with it here
    words = line.split(",")
    print(words[3])


def main():
    pass

if __name__ == "__main__":
    main()