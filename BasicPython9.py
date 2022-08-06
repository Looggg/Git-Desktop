
class Employee: 
    minSalary = 100
    __maxSalary = 200

    def __init__(self,name,salary,department): 
        self.__name = name 
        self.__salary = salary 
        self._department = department
    
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name) 
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

#สร้าง class สึบทอดคุณสมบัติ
class Accounting(Employee):
    __departmentName = "แผนกบัญชี" #class variable
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department
        super()._showData()

class Programmer(Employee):
    __departmentName = "โปรแกรมเมอร์"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department


class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department

account = Accounting("loog",100)
account._showData()

programmer = Programmer("ooo",200)
programmer._showData()

sale = Sale("baba",300)
sale._showData()