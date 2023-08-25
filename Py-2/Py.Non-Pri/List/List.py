# เข้าถึงข้อมูล print(num[1])
# เข้าถึงข้อมูลแบบกำหนดช่วง print(num[1:3])
# แก้ไขข้อมูล num[2]=...

# แสดงผลด้วย Loop -> for .[x]. in num:
#                       print(.[x].)

# ตรวจสอบข้อมูล if 20 in num:
#                 print("เป็น")
#             else:
#                 print("ไม่เป็น")

# นับจำนวนสมาชิก(len(num))

# Ex ประยุกlen&for loopการวนลูปบอกชื่อสมากชิกใน list
# for i in range(len(num)):
#     print(num[i])
# หรือ
# for item in num:
#     print(num)

# การเพิ่มข้อมูล append, insert
# num.append("กหฟกฟ") เป็นการต่อท้าย
# num.insert(1,"sdasd") กำหนดช่วงได้

# การลบข้อมูล remove, pop, del, clear
# num.remove("2") เลือกตัวที่อยากลบ
# num.pop() ลบสมาชิกตัวล่าสุด,ท้ายสุดออก
# del num[1] เคลียร์หน่วยความจำ ลบตัวแปร num ออก
# num.clear() ลบข้อมูลใน num ออกแต่ไม่ลบ num

# num=[1,2,3,4,5,5,5]

# คัดลอกข้อมูล
# x=[]
# x=num.copy()

# รวมข้อมูล ใช้ +

# แสดงจำนวนสมาชิก (count) 
# x=num.count(5)

# extend เหมือนกัน + กันเลย