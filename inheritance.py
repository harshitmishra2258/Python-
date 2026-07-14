class Employee:
    start_time=10
    end_time=5

class Teacher(Employee):
    def __init__(self,subject):
        self.subject=subject

t1=Teacher("Maths")
print(t1.subject)
print(t1.start_time)