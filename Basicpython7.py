#สร้าง Constructor

class Employee: 
    # class variable
    _minSalary = 100
    _maxSalary = 200

    def __init__(self,empname,empsalary): 
        # instance variable
        self._name = empname
        self._salary = empsalary 
    
    
    def _showData(self):
        print("ชื่อพนักงาน = "+self._name) 
        print("เงินเดือน =",format(self._salary))
     
    

obj1 = Employee("Loog",100)
# print("เงินเดือนต่ำสุด = "+str(Employee._minSalary))
# print(Employee._minSalary)