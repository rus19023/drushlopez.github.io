class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)
        

class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CheckingAccount():
    def __init__(self, starting_balance, num_checks):
        if starting_balance < 0:
            raise BalanceError("Starting balance cannot be less than zero.")
        self.balance = starting_balance
        self.check_count = num_checks
                
    def deposit(self, amount):
        self.balance += amount
        
    def write_check(self, amount):
        if self.balance < amount:
            raise BalanceError("Check amount cannot be more than current balance.")
        if self.check_count == 0:
            raise OutOfChecksError("You have no checks left.")
        self.balance -= amount        
        self.check_count -= 1
        
    def order_checks(self):
        self.balance -= 5
        self.check_count += 25
        print("Deducting $5.00 for 25 checks.")
    
    def display(self):
        print("Current balance: ${:.2f}, Number of checks left: {}".format(self.balance, self.check_count))
    
    def apply_for_credit(self, mount):
        pass    


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Desposit money")
    print("  check - Write a check")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":   
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))
            try:
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as ex:
                print("Error: {}".format(str(ex)))
        elif command == "display":
            acc.display()
        elif command == "deposit":
            amount = float(input("Amount: "))
            acc.deposit(amount)
        elif command == "check":
            amount = float(input("Amount: "))
            try:
                acc.write_check(amount)
            except OutOfChecksError as ex:
                print("Error: {}".format(str(ex)))
                new_order = input("Would you like to order more checks? (Y or N)")
                if new_order.upper() == "Y":
                    acc.order_checks()                                
        elif command == "credit":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()