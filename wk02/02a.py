

def prompt_number():
    numb = input("Enter a positive number: ")
    while int(numb) < 0:
        print("Invalid entry. The number must be positive.")
        numb = input("Enter a positive number: ")
    return numb


def compute_sum(int1, int2, int3):
    sum = "The sum is: " + str(int1 + int2 + int3)
    return sum


def main():
    num1 = int(prompt_number())
    print()
    num2 = int(prompt_number())
    print()
    num3 = int(prompt_number())
    print()
    print(compute_sum(num1, num2, num3))


if __name__ == "__main__":
    main()
