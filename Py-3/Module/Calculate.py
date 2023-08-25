# ให้บริการข้อมูลค่าคงที่ / คำนวณตัวเลข
PI = 3.14
def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวก = ", total)

def subtraction(num1, num2):
    print("ผลลบ = ", (num1-num2))

def power(num1,m):
    print("ผลการยกกำลัง = ", num1**m)
