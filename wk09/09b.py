class NegativeNumberError(Exception):
    """     For negative balance errors    """
    def __init__(self, message):
        super().__init__(message)
        

def get_inverse(n):
    if n == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if n < 0:
        raise NegativeNumberError("The value cannot be negative")
    return 1 / n


def main():
    try:
        n = float(input("Enter a number: "))
        result = get_inverse(n)
        print("The result is: {}".format(result))
    except ValueError:
            print("Error: The value must be a number")
    except ZeroDivisionError as ex:
            print("Error: {}".format(str(ex)))
    except NegativeNumberError as ex:
            print("Error: {}".format(str(ex)))

            
if __name__ == "__main__":
    main()    