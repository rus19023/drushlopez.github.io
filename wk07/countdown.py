def countdown(num):
    if num == 0:
        return

    # We could use an "else" here, but we really don't have to because
    # the return statement from the line above will end the function
    # right there for the base case. Then, anything that follows is the
    # recursive case

    print(num)
    countdown(num - 1)
    
    
def main():
     index = 10
     #int(input("Enter a number to countdown from: "))
     countdown(index)
    
    
if __name__ == "__main__":
    main()