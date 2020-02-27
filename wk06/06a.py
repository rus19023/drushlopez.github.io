class Book:

    def __init__(self):
        self.author = ""
        self.title = ""
        self.publication_year = ""
        
    def prompt_book_info(self):
        self.title = "Dangerousme" '''input("Please enter book title: ")'''
        self.author = "Me, Myself & I" '''input("Please enter author name: ")'''
        self.publication_year = "1999"  '''input("Please enter year published: ")'''
        return self.title, self.author, self.publication_year
    

    def display_book_info(self):
        return "Title: {}\nAuthor: {}\nPublication year: {}".format(self.title, self.author, self.publication_year)
    
    
class TextBook(Book):
    
    def __init__(self):
        super().__init__()
        self.subject = ""
        
    def prompt_subject(self):
        self.subject = "Coding" '''input("Please enter subject of TextBook: ")'''
        
    def display_subject(self):
        print(self.subject())
        
        
class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ""
        
    def prompt_illusrator(self):
        self.illustrator = "My Sister" '''input("Please enter illustrator's name: ")'''
        return self.illustrator
    
    def display_illustrator(self):
        print(self.illustrator())
    

def main():
    new_book = Book()
    new_book.prompt_book_info()
    new_book.display_book_info()
    

if __name__ == "__main__":
    main()
