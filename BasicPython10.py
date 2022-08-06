
class Employee: 
    minSalary = 100
    __maxSalary = 200

    def __init__(self,name,salary,department): 
        self.__name = name 
        self.__salary = salary 
        self._department = department
    
    #แสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name) 
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = "+self._department)

    #คำนวณรายได้ต่อปี
    def _getIncome(self):
        return self.__salary *12

#สร้าง class สึบทอดคุณสมบัติ
class Accounting(Employee):
    __departmentName = "แผนกบัญชี" #class variable
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department
        # super()._showData()

class Programmer(Employee):
    __departmentName = "โปรแกรมเมอร์"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department


class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department

account = Accounting("loog",100)
print("รายได้ต่อปี = {}".format(account._getIncome()))
programmer = Programmer("ooo",200)
print("รายได้ต่อปี = {}".format(programmer._getIncome()))
sale = Sale("baba",300)
print("รายได้ต่อปี = {}".format(sale._getIncome()))
print(br)
