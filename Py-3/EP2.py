#การเข้าถึงไฟล์ -> open("ชื่อไฟล์","โหมด","เข้ารหัส")    
# a-> สร้างไฟล์,แก้ไขข้อมูล,เพิ่มข้อมูล
# w-> เขียนข้อมูลทับที่มีอยู่
# r-> อ่าน
# เพิ่มไฟล์ txt
"""try:
    fr=open("score.txt","r",encoding="utf-8")
    print(fr.read())
except FileExistsError:
    print("ไม่เจอไฟล์")
"""
"""try:
    fw=open("score.txt","w",encoding="utf-8") #encoding="utf-8" ทำงานกับภาษาไทยได้
    fw.write("Hello World\n")
    fw.writelines("สวัสดีชาวโลก")
    fw.close()
except FileExistsError:
    print("ไม่เจอไฟล์")
"""

"""try:
    fr=open("score.txt","r",encoding="utf-8")
    line=fr.readlines()
    for x in line:
        print("=>",x)

    # fw=open("score.txt","a",encoding="utf-8")
    # fw.writelines("dsadasd1123\n")
    fr.close()
    # fw.close()
except FileExistsError :
    print("ไม่เจอไฟล์")"""

# try:
#     fw=open("score.txt","a",encoding="utf-8")
#     for i in range(5): 
#         name = input("ป้อนข้อความที่ต้องการ : ")
#         fw.writelines(name+'\n')
#     fw.close()

# except FileExistsError :
#     print("ไม่เจอไฟล์")    

# ลบไฟล์ txt
import os # ตัวจัดการไฟล์ โฟล์เดอร์
try:
    if os.path.exists("123.txt") : # หาตัวแหน่งไฟล์
        os.remove("123.txt")
        print("ลบเรียบร้อย")
    else :
        print("ไม่พบไฟล์")
except Exception as e:
    print(e)
