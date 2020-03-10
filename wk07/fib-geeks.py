# Function for nth Fibonacci number

def fib(n):
    if n<1:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

# Driver Program

print(fib(2))

#This code is contributed by Saket Modi