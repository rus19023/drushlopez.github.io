"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others, edited by Doris Rush-Lopez.
Sorts a list of strings.
"""

def sort(words):
    """ 
    Fill in this method to sort the list of numbers
    """
    for word in words:
        print("list length: {}".format(len(words)))
        current_word = words[word]
        swap_index = word
        print("current_word: {}".format(current_word))
        print("swap_index: {}".format(swap_index))
        while swap_index>0 and words[swap_index-1]>current_word:
            words[swap_index]=words[swap_index-1]
            swap_index = swap_index-1

        words[swap_index]=current_word


def prompt_for_words():
    """
    Prompts the user for a list of words and returns it.
    :return: The list of words.
    """

    words = []
    
    test1 = ""

    while test1.lower() != 'q':
        test1 = input("Enter a series of words, or q to quit: ")

        if test1.lower() != 'q':
            words.append(test1)

    return words

def display(words):
    """
    Displays the words in the list
    """
    print("The list is:")
    for test1 in words:
        print(test1)

def main():
    """
    Tests the sorting process
    """
    words = prompt_for_words()
    sort(words)
    display(words)

if __name__ == "__main__":
    main()