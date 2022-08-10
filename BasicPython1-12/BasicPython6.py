#สร้าง Constructor

class Employee: #การสร้าง class ตัวแรกแนะนำตัวใหญ่

    def __init__(self,empname,empsalary): 
        #private Attribute
        self.__name = empname #Protected
        self.__salary = empsalary 
    
    #Private Attribute
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.getName())) #Protected
        print("เงินเดือน =",format(self.getsalary()))
        # print("เงินเดือน = "+self.getName())
    
    # getter method
    def getName(self):
        return self.__name

    def getsalary(self):
        return self.__salary

obj1 = Employee("Loog",100)
obj1._showData()
# print("พนักงานดีเด่น = {}".format(obj1.getName()))