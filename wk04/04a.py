class Person:

    def __init__(self):
        self.name = "anonymous"
        self.born_year = "unknown"

    def display(self):
        return "{} (b. {})".format(self.name, self.born_year)


class Book:

    def __init__(self):
        self.author = Person()
        self.title = "untitled"
        self.publisher = "unpublished"

    def display(self):
        print(self.title)
        print(("Publisher:"))
        print(self.publisher)
        print("Author:")
        print(self.author.display())


def main():
    new_book = Book()
    new_book.display()
    print()
    print("Please enter the following:")
    new_book.author.name = input("Name: ")
    new_book.author.born_year = input("Year: ")
    new_book.title = input("Title: ")
    new_book.publisher = input("Publisher: ")
    print()
    new_book.display()


if __name__ == "__main__":
    main()
