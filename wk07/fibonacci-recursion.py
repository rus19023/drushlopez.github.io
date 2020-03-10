fibonacci_list = [0, 1]
def fib(n):
    counter = 0
    if n == 0:
        print("The Fibonacci number is: 0")
    if n == 1:
        print("The Fibonacci number is: 1")
    if counter == n:
        return
    n1 =
    n3 = n1 + n2
    n2 = n3 
    counter += 1   

    
    print("The Fibonacci number is: {}".format(n3))

    fib(n + 1)
    
    
def main():
    position = 8 
        #int(input("Enter a Fibonacci index: "))
    fib(position)
    
    
if __name__ == "__main__":
    main()