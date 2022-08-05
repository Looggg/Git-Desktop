#สร้าง Constructor

class Employee: #การสร้าง class ตัวแรกแนะนำตัวใหญ่

    def __init__(self,empname,empsalary): 
        #private Attribute
        self._name = empname #Protected
        self.__salary = empsalary 
        # self._showData() เรียก print
    #Private Attribute
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self._name)) #Protected
        print("เงินเดือน = {}".format(self.__salary))
        
  
obj1 = Employee("Loog",100)
# obj1.__salary = 2000 ไม่สามารถใช้ได้เพราะเป็น private 
#  obj1._name = "โจโจ้"
#  obj1.name = "โจโจ้"
#  print(obj1._name)
# obj1._showData()

