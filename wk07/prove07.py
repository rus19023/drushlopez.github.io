fibonacci_list = [0, 1.]
position = 0
number = 0
def fib(n):
        fibonacci_list.append(fibonacci_list([index - 1]) + fibonacci_list([index - 2]))
        number += 1
        
    if number < len(fibonacci_list - 1) and index > 1:
        return "The Fibonacci number is: {}".format(fibonacci_list[len(fibonacci_list - 1)])
    
    
def main():
    position = int(input("Enter a Fibonacci index: "))
    fib(position)
    
    
if __name__ == "__main__":
    main()