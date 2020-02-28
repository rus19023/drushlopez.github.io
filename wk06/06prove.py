from collections import deque
"""
A student has a name and course
"""
class Student:
    def __init__(self, name = "", course = ""):
        self.name = name
        self.course = course
     
    """
    get  student's name and course
    """
    def prompt(self):
        self.name = input("Name: ")
        self.course = input("Course: ")
        return self.name, self.course
     
    """
    display student name and course
    """
    def display(self):
        new_student = "{} with {}".format(self.name, self.course)
        return new_student
        
        
"""
A Help system has students in a queue waiting for the next TA
"""
class HelpSystem(Student):
    waiting_list = deque([])
    def __init__(self , waiting_list):
        super().__init__()
    
    """
    check for students waiting in queue
    """
    def is_student_waiting():
        if len(HelpSystem.waiting_list) > 0:
            return True
        else:
            return False
        
    """
    add a student to the queue
    """
    def add_to_waiting_list(Student): 
        next_in_line = Student.prompt() 
        HelpSystem.waiting_list.append(Student.display())
         
    def help_next_student(self):
        if HelpSystem.is_student_waiting():
            student_helped = HelpSystem.waiting_list.popleft()
            print("\nNow helping {}".format(student_helped))
        else:
            print("\nNo one to help") 
 
 
"""
create the student queue, prompt for user entry,
  add or remove student from queue or quit
"""
def main():
    help_queue = HelpSystem(Student())
    choice = "0"    
    while choice != "3":
            choice = input("\nOptions: \n1. Add a new student\n2. Help next student\n3. Quit\nEnter selection: ")
            if choice == "1":
                help_queue.add_to_waiting_list()
            elif choice == "2":
                    help_queue.help_next_student()
            elif choice == "3":
                print("Goodbye")
                break        
            
  
if __name__ == '__main__':
    main()      
        

        
        
        
        
