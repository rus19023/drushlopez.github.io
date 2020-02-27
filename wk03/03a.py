class Student:
    """ Student class for keeping student records. """

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.id = 0


def prompt_student():
    new_student = Student()
    new_student.first_name = input("Please enter your first name: ")
    new_student.last_name = input("Please enter your last name: ")
    new_student.id = input("Please enter your id number: ")
    return new_student


def display_student(student):
    print()
    print("Your information:")
    print(student.id, "-", student.first_name, student.last_name)


def main():
    user = prompt_student()
    display_student(user)


if __name__ == "__main__":
    main()
