class GPA():
    def  __init__(self, gpa=0.0):
        self.gpa = gpa
        
   
    def get_gpa(self):
        return self.gpa
    
       
    def set_gpa(self, value):   
        if value < 0.0:
            self.gpa = 0.0
        elif value > 4.0:
            self.gpa = 4.0
        else:
            self.gpa = value
    
    
    def get_letter(self):
        if 0.0 <= self.gpa <= .99:
            return "F"
        elif 1.0 <= self.gpa <= 1.99:
            return "D"
        elif 2.0 <= self.gpa <= 2.99:
            return "C"
        elif 3.0 <= self.gpa <= 3.99:
            return "B"
        elif self.gpa == 4.0:
            return "A"
        else:
            return "Error"
    
    
    def set_letter(self, letter):
        if letter == "F":
            self.gpa = 0.0
        elif letter == "D":
            self.gpa = 1.0
        elif letter == "C":
            self.gpa = 2.0
        elif letter == "B":
            self.gpa = 3.0
        elif letter == "A":
            self.gpa = 4.0
            
def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main()