#ฟังก์ชั่นเสริม

from inspect import Attribute


class Employee: #การสร้าง class ตัวแรกแนะนำตัวใหญ่

    def __init__(self,empname,empsalary): 
        self.name = empname
        self.salary = empsalary

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))

    def __del__(self):
        print("Call Destructor")
        
obj1 = Employee("Loog",100)
#obj1.salary = 500 เปลี่ยนเงินเดือนได้ โดยเข้าถึง salary หรือเปลี่ยนชื่อก็ได้
obj1.showData()
obj2 = Employee("Bon",200)
obj2.showData()
obj3 = Employee("Baba",300)
obj3.showData()

print(isinstance(obj1,Employee)) #เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามไหม
print(dir(obj1)) #แสดง Attribute และ Method
print(obj1.__class__) #แสดงชื่อ class ของ object 
