import datetime


class Date:

    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 1999

    def prompt(self):
        while self.day < 1 or self.day > 31:
            self.day = int(input("Day: "))
            break
        while self.month < 1 or self.month > 12:
            self.month = int(input("Month: "))
            break
        while self.year < 2000 or self.year > 3001:
            self.year = int(input("Year: "))
            self.year = str(self.year)
            print(self.year)
            break

    def display(self):
        self.day = str(datetime.datetime.strptime(str(self.month), '%d'))
        print(self.day)
        self.month = datetime.datetime.strptime(str(self.month), '%m')
        print(self.month)
        self.year = datetime.datetime.strptime(str(self.year), '%Y')
        whole_date = "{}-{}-{}".format(self.year, self.month, self.day)
        print("whole_date: ", whole_date)
        whole_date = datetime.datetime.strptime(whole_date, '%m/%d/%y')
        print("whole_date: ", whole_date)

    def display_long(self):
        whole_date = "{}-{}-{}".format(self.year, self.month, self.day)
        long_date = datetime.datetime.strptime(whole_date, '%A, %B %w, %Y')
        print("long_date: ", long_date)
