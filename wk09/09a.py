is_valid = False
while not is_valid:
    try:
        number = int(input("Enter a number: "))
        is_valid = True
    except ValueError:
        print("The value entered is not valid")
print("The result is: {}".format(number * 2))
