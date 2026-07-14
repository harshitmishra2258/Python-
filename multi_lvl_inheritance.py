class Employee:
    start_time=10
    end_time=5
class Adminstaff(Employee):
    def __init__(self,role):
        self.role=role
    
class Acountant(Adminstaff):
    def __init__(self, role,accounts):
        super().__init__(role)
        self.accounts =accounts

A1=Acountant("CA","bank")
print(A1.accounts)
