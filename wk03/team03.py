class Fraction:
    ''' Class for working with fractions/rational numbers. '''

    def __init__(self, numerator=5, denominator=1):
        '''initialize the fraction class'''
        self.numerator = numerator
        self.denominator = denominator

    def reduce(self):
        if self.numerator % self.denominator == 0:
            self.numerator = self.numerator // self.numerator
            self.denominator = self.denominator // self.numerator
            self.reduced = str(int(self.numerator)) + "/" + str(int(self.denominator))
            return 'Reduced Fraction is: {}'.format(str(self.reduced))
        else:
            return 'Fraction cannot be reduced: {}/{}'.format(str(self.numerator), str(self.denominator))

    def display_decimal(self):
        ''' displays the fraction in decimal form '''
        self.decimal = self.numerator / self.denominator
        return 'Fraction in decimal form: {}'.format(str(self.decimal))

    def display(self):
        ''' display the fraction in fractional form, for example 2/3 '''
        if self.numerator > self.denominator:
            self.whole_part = int(self.numerator // self.denominator)
            self.remainder = self.numerator % self.denominator
            if self.remainder == 0:
                return 'Fraction is a whole number:', self.whole_part
            else:
                return 'Fraction is a mixed number: {} {}/{}'.format(self.whole_part, self.remainder, self.denominator)
        else:
            return 'Fraction is: {}/{}'.format(str(self.numerator), str(self.denominator))

    def multiply_by(self):
        f2 = Fraction()
        f2.prompt()
        f3 = Fraction()
        f3.numerator = f2.numerator * self.numerator
        f3.denominator = f2.denominator * self.denominator
        f3.reduce()
        return f3.display(), f3.display_decimal()

    def prompt(self):
        ''' get user input for numerator and denominator '''
        self.numerator = int(input("Enter numerator: "))
        self.denominator = int(input("Enter denominator: "))


def main():
    f4 = Fraction()
    print(f4.display())
    f1 = Fraction()
    f1.prompt()
    print(f1.display())
    print(f1.display_decimal())
    print(f1.reduce())
    print(f1.multiply_by())
    print()

# If this is the main program being run, call our main function above


if __name__ == "__main__":
    main()
