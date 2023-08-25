# ฟังก์ชั่น เรียกใช้ ฟังก์ชั่น

def equal(x,y,z):
    a=compareMax(x,y) # เอา x เปรียบเทียบ y เก็บใน a
    m=compareMax(a,z) # และเอา a เปรียบเทียบ z เก็บใน m
    return m # ส่งค่า m ออกมา
""" ลดรูปได้
def equal(x,y,z):
    compareMax(compareMax(x,y),z)
"""
 
def compareMax(x,y):
    if x>y:
        return x
    else:
        return y

max=equal(10,5,11)
print("ค่ามากสุด = ", max)
