
#fruit={"dsa",11,3.22,True}
"""
# การเพิ่มข้อมูลตัวเดียว
fruit={"dsa",11,3.22,True}
fruit.add("21")
# เพิ่มสมาชิกหลายตัว
a=["asd",23,1.23]
fruit.update(a)
print(fruit)
"""
"""
# Loop
fruit={"dsa",11,3.22,True}
for x in fruit:
   print("ข้อมูล => ",x)
"""

# แสดงจำนวนสมาชิก print(len(fruit))
"""
# ลบข้อมูล
fruit={"dsa",11,3.22,True}
fruit.discard("dsa") #ลบแบบ ถึงจะมีหรือไม่มีก็ไม่ขึ้น errors แนะนำใช้ตัวนี่
fruit.remove("dsa") #ลบแบบ ถ้าไม่มีสมาชิกจะขึ้น error
fruit.clear() ล้างสมาชิก
del fruit ลบตัวแปร
"""



