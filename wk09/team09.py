class BalanceError(Exception):
    """     For negative balance errors    """
    def __init__(self, message):
        super().__init__(message)
        self.overdrawn = overdrawn     
        

class OutOfChecksError(Exception):
    """     For no checks left errors    """
    def __init__(self, message):
        super().__init__(message)


class CheckingAccount():
    """  set up checking account with balance and number of checks  """
    def __init__(self, starting_balance, num_checks):
        if starting_balance < 0:
            raise BalanceError("Starting balance cannot be less than zero.")
        self.balance = starting_balance
        self.check_count = num_checks
                
    def deposit(self, amount):
        """ add money to account """
        if amount < 0:
            raise ValueError("Deposit amount cannot be less than 0.")
        self.balance += amount
        
    def write_check(self, amount):
        """  to deduct check amounts from account  """
        if amount < 0:
            raise ValueError("Check amount cannot be less than 0.")
        if self.balance < amount:
            raise BalanceError("Check amount cannot be more than current balance.")
        if self.check_count == 0:
            raise OutOfChecksError("You have no checks left. The cost is $5 for 25 checks.")
        self.balance -= amount        
        self.check_count -= 1
        
    def order_checks(self):
        """  to order more checks  """
        self.balance -= 5
        self.check_count += 25
        print("Deducting $5.00 for 25 checks.")
    
    def display(self):
        """  to show current balance and checks left  """
        print("Current balance: ${:.2f}, Number of checks left: {}".format(self.balance, self.check_count))
    
    def apply_for_credit(self, mount):
        """  to apply for a line of credit when balance is less than check amount  """
        pass    


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  q - Quit")
    print("  n - Create new account")
    print("  s - Show account information")
    print("  d - Deposit money")
    print("  c - Write a check")
    print("  a - Apply for credit")
    print()


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command.upper() != "Q":
        display_menu()
        command = input("Enter a command: ")

        if command.upper() == "N":   
            balance = float(input("Starting balance: "))
            num_checks = int(input("Numbers of checks: "))
            try:
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as ex:
                print("Error: {}".format(str(ex)))
        elif command.upper() == "S":
            acc.display()
        elif command.upper() == "D":
            amount = float(input("Amount: "))
            try:
                acc.deposit(amount)
            except ValueError:
                print("Deposit amount cannot be less than zero, please try again.")
        elif command.upper() == "C":
            amount = float(input("Amount: "))
            try:
                acc.write_check(amount)
            except ValueError:                
                print("Check amount cannot be less than zero, please try again.")
            except OutOfChecksError as ex:
                print("Error: {}".format(str(ex)))
                new_order = input("Would you like to order more checks? (Y or N)")
                if new_order.upper() == "Y":
                    acc.order_checks()                                
        elif command.upper() == "A":
            amount = float(input("Amount: "))
            acc.apply_for_credit(amount)


if __name__ == "__main__":
    main()