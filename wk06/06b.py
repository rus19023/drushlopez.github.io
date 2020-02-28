"""
A phone has a number made up of area code, prefix and suffix
"""
class Phone:
    def __init__(self, area_code = "555", prefix = "555", suffix = "5555"):
        self.area_code = area_code
        self.prefix = prefix
        self.suffix = suffix
     
    """
    get phone number from user
    """
    def prompt_number(self):
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")
        return self.area_code, self.prefix, self.suffix
     
    """
    display phone number in this format: (555)555-5555
    """
    def display(self):
        print("Phone info:")
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))
        
        
"""
A smart phone has a phone number from phone class plus an email
"""
class SmartPhone(Phone):
    def __init__(self, email = "info@email.com"):
        super().__init__()
        self.email = email
    
    """
    get email from user
    """
    def prompt(self):
        super().prompt_number()
        self.email = input("Email: ")
        return self.email
        
    """
    display email
    """
    def display(self):
        super().display()
        print(self.email)
 
 
"""
create a phone, prompt for user entry,
  display what was entered, repeat for smartphone
"""
def main():
    home = Phone()
    print("Phone:")
    home.prompt_number()
    print()
    home.display()
    print()
    celly = SmartPhone()
    print("Smart phone:")
    celly.prompt()
    print()
    celly.display()    
        
  
if __name__ == '__main__':
    main()      
        

        
        
        
        
