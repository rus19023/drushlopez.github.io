'''  Tests the assignment and date classes. '''

from assignment import Assignment


def main():
    homework = Assignment()
    homework.prompt()
    print()
    homework.display()
    '''homework.long_display()'''


if __name__ == "__main__":
    main()
