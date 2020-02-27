"""
This file contains the following classes:
    CreditCard
    Address

and then it contains a main function.

Your task it to break it into three files, then tar them up, and submit.
"""

class Address:
    """ Contains a street address """
    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def display(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))


class CreditCard:
    """ Contains a credit card that has two addressess"""
    def __init__(self):
        self.name = ""
        self.number = ""
        self.mailing_address = Address()
        self.billing_address = Address()

    def display(self):
        print(self.name)
        print(self.number)
      
        print("Mailing Address:")
        self.mailing_address.display()

        print("Billing Address:")
        self.billing_address.display()

def main():
    cc = CreditCard()

    cc.name = input("Name: ")
    cc.number = input("Number: ")
    
    print("Mailing Address:")
    cc.mailing_address.street = input("Street: ")
    cc.mailing_address.city = input("City: ")
    cc.mailing_address.state = input("State: ")
    cc.mailing_address.zip = input("Zip: ")
    
    print("Billing Address:")
    cc.billing_address.street = input("Street: ")
    cc.billing_address.city = input("City: ")
    cc.billing_address.state = input("State: ")
    cc.billing_address.zip = input("Zip: ")

    cc.display()

if __name__ == "__main__":
    main()
