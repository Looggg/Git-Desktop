# Recursive Function เรียกใช้ฟังก์ชั่นในตัวเอง
"""
หาจุดวนซ้ำ
หาจุดออกจาก function
ต้องมี parameter
"""

""" ตัวอย่างแบบง่าย ไม่มีการใช้ loop
def addNumber(number):
    if number==5:
        return
    print(number)
    number+=1
    addNumber(number)

addNumber(0)
"""    
# ฟังก์ชั่น เรียก ฟังก์ชั่นตัวเอง
def addNumber(number):
    if number==5:
        return print(number)
    print(number)
    number+=1
    addNumber(number)

def summation(number):
    if number==1:
        return number
    if number<1:
        print("ส่งเลขมากกว่า 1 มาไอ้โง่")
    else:
        return number+summation(number-1)

x=summation(5) # 5+4+3+2+1
print(x)  
    