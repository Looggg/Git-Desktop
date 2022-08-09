#สร้าง Constructor

class Employee: #การสร้าง class ตัวแรกแนะนำตัวใหญ่

    def __init__(self,empname,empsalary): 
        #private Attribute
        self.__name = empname #Protected
        self.__salary = empsalary 
    
    #Private Attribute
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name)) #Protected
        print("เงินเดือน = {}".format(self.__salary))
    
    # setter method กำหนดค่าให้ object
    def setName(self,newname):
        self.__name = newname
        
    def setsalary(self,newsalary):
        self.__salary = newsalary

    # getter method ดึงค่าจาก Object
    def getName(self):
        return self.__name

obj1 = Employee("Loog",100)

print("พนักงานดีเด่น = {}".format(obj1.getName()) ) # ดึงค่าแสดง
# print(obj1.getName()) ดึงค่าแสดง
# obj1.setName("OOO")   กำหนดค่า
# obj1.setsalary(20000) กำหนดค่า
# obj1._showData()