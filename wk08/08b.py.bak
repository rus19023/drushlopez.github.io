class GPA():
    def  __init__(self, gpa=0.0):
        self._gpa = gpa


    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, value):
        if value < 0.0:
            self._gpa = 0.0
        elif value > 4.0:
            self._gpa = 4.0
        else:
            self._gpa = value

    gpa = property(_get_gpa, _set_gpa)

    @property
    def letter(self):
        if 0.0 <= self._gpa <= .99:
            return "F"
        elif 1.0 <= self._gpa <= 1.99:
            return "D"
        elif 2.0 <= self._gpa <= 2.99:
            return "C"
        elif 3.0 <= self._gpa <= 3.99:
            return "B"
        elif self._gpa == 4.0:
            return "A"
        else:
            return "Error"

    @letter.setter
    def letter(self, letter):
        if letter == "F":
            self._gpa = 0.0
        elif letter == "D":
            self._gpa = 1.0
        elif letter == "C":
            self._gpa = 2.0
        elif letter == "B":
            self._gpa = 3.0
        elif letter == "A":
            self._gpa = 4.0


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()