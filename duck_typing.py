class Employee:
    def get_designation(self):
        print("Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Teacher")

t1=Teacher()
t1.get_designation()

e1=Employee()
e1.get_designation()