def prompt_search():
    search_word = input("Enter a word to search for: ")
    return search_word


def prompt_filename():
    '''filename_to_read = input("Enter filename: ")'''
    filename_to_read = "home/cs241/ta02/spiritual-treasures.txt"
    return filename_to_read


def parse_file(filename):
    search_for = prompt_search()
    search_count = 0
    total_words = 0
    search_again.lower() = "y"
    while search_again = "y":
        readfile = open(prompt_filename(), "r", encoding="utf-8")
        if search_again.lower() == "y":
            for line in readfile:
                words = line.split()
                for word in words:
                    if search_for.lower() in word.lower():
                        search_count += 1
                    total_words += 1
            search_again = input("Do you want to search for another word? (y/n)")
        readfile.close()
        found1 = "Total nfumber of words in this file is " + str(total_words)
        found1 += ".\nSearch word " + search_for
        found1 += " occurs this many times in this file: " + str(search_count)
    return found1


def main():
    filename1 = prompt_filename()
    print("Opening file {}".format(filename1))
    print(parse_file(filename1))


if __name__ == "__main__":
    main()
