
class Employee: 
    minSalary = 100
    __maxSalary = 200

    def __init__(self,empname,empsalary): 
        self._name = empname 
        self._salary = empsalary 
    
    
    def _showData(self):
        print("ชื่อพนักงาน ="+self._name) 
        print("เงินเดือน =",format(self._salary))
        
#สร้าง class สึบทอดคุณสมบัติ
class Accounting(Employee):
    def __init__(self):
        pass

class Programmer(Employee):
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self):
        pass

account = Accounting()
print(account.minSalary)
programmer = Programmer()
print(programmer.minSalary)
sale = Sale()
print(Sale._Employee__maxSalary)
