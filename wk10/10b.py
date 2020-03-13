"""
File: sorting.py
Original Author: Br. Burton, designed to be completed by others.
Sorts a list of numbers.
"""

def sort(numbers):
    """ 
    Fill in this method to sort the list of numbers
    """
    for i in range(1,len(numbers)):
        # print("list length: {}".format(len(numbers)))
        current_number = numbers[i]
        swap_index = i
        # print("current_number: {}".format(current_number))
        # print("swap_index: {}".format(swap_index))
        while swap_index>0 and numbers[swap_index-1]>current_number:
            numbers[swap_index]=numbers[swap_index-1]
            swap_index = swap_index-1

        numbers[swap_index]=current_number


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()