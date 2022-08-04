# ชื่อ, เงินเดือน
class Employee: #การสร้าง class ตัวแรกแนะนำตัวใหญ่
    #สร้าง method
    def detail(self,empname,empsalary):
        self.name = empname
        self.salary = empsalary

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))

#สร้างวัตถุ
obj1 = Employee()
obj1.detail("Loog",100)
obj2= Employee()
obj2.detail("Bon",200)

obj1.showData()
obj2.showData()
