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
    # def _getIncome(self):
    #     return self.__salary *12

    # Overlordind method ชื่อเหมือนกันกับอีกตัวใน class แต่ พารามิเตอร์ต่างกัน
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary *12)+bonus+overtime

    #แปรง object -> String
    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(self.__name, self._department, self.__salary))

#สร้าง class สึบทอดคุณสมบัติ
class Accounting(Employee):
    __departmentName = "แผนกบัญชี" #class variable
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department
        self.__age = age 

    def _showData(self):
        super()._showData()
        print("อายุ = "+str(self.__age))
        print("###############")

    def __str__(self):
        return(super().__str__()+" , อายุ = {}".format(self.__age))

class Programmer(Employee):
    __departmentName = "โปรแกรมเมอร์"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print("###############")

    def __str__(self):
        return(super().__str__()+", ประสบการณ์ = {} , ทักษะ = {}".format(self.__exp,self.__skill))


class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName) #สังเกต self ใส่แค่ตรง department
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = "+self.__area)
        print("###############")

    def __str__(self):
        return(super().__str__()+" , พื้นที่รับผิดชอบ = {}".format(self.__area))


account = Accounting("loog",100,30)
programmer = Programmer("ooo",200,2,"โง่")
sale = Sale("baba",300,"ตาก")


print("รายได้ต่อปี = "+str(account._getIncome())) #ไม่ใส่โบนัท แต่ตรง bonusของmethod ต้องเติม =0 
print("รายได้ต่อปี = "+str(account._getIncome(500))) #ใส่โบนัท 500
print("รายได้ต่อปี = "+str(account._getIncome(0,200))) #ใส่โอที 200

# print(account.__str__())
# print(programmer.__str__())
# print(sale.__str__())
