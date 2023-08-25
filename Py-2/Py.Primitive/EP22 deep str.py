name=" Loog Bon11 Loog " # index => 0

# print(name[-2:]) # มีจุดเริ่มและจบ [-2:]นับจากหลัง, [:2]นับจากหน้า(0)

# print(len(name)) เชคจำนวน str 

# name=name.strip() ลบช่องว่าง ขวา-ซ้าย
# print(name)
# name=name.rstrip() ลบช่องว่าง ขวา
# name=name.lstrip() ลบช่องว่าง ซ้าย

#แปลง case ของ string
# print(name.upper()) แปลงเป็นพิมใหญ่ทั้งหมด
# print(name.lower()) แปลงเป็นพิมเล็กทั้งหมด
# print(name.capitalize()) ตัวแรกเป็นตัวพิมใหญ่

# การแทนที่
# print(name.replace("คำที่ต้องการเปลี่ยน", "เปลี่ยนให้เป็นตัวนี่", จำนวนที่ต้องการเปลี่ยน)) 
# print(name.replace("Loog", "5555", 1)) 

# เชคข้อความ -> bool
# x = "คำที่ต้องการหา" in ตัวแปร
# x = "Loog" in name
# if x:
#     name=name.replace("Loog", "ควย",1)
# print(name)

# การต่อ str (concatinate) +
# dd= "Loog"
# aa= "Bon"
# age= "18"
# full=dd+aa+age
# print(full+"\tควย") #\t เหมือนกด Tap

# จัดรูปแบบการแสดงผล
# dd= "Loog" #0
# aa= "Bon"  #1
# age= "18"  #2
# mon=123.12345 #3
# full="ชื่อต้น :{1}\tนามสกุล :{1}\tอายุ :{2}\tเงินเดือน :{3:.2f}" 
# หรือ "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}             {ตำแหน่งตัวแปร:.จำนวนทศนิยมที่ให้มี}
# print(full.format(aa, dd, age,mon)) # aa, dd สลับตำแหน่งกัน

#นับจำนวนคำในประโยค (count)
# fruit="ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
# print(fruit.count("ทุเรียน")) # เจอ 3 จุด

#เชคคำขึ้นต้น
# n="นายควยไร ใจเหี้ย"
# print(n.startswith("นาย")) #เชคเฉยๆ
# if n.startswith("คำขึ้นต้น")
# if n.startswith("นาย"):
#     print("เป็นชาย")
# else :
#     print("เป็นใครไม่รู้")

# เชคคำลงท้าย
# a="1150"
# print(a.endswith("0"))

