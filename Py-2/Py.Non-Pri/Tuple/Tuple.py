# ไม่สามารถแก้ไขข้อมูลได้
"""
การนิยาม , Constructor
tup=()
"""

"""
การเข้าถึงข้อมูลแบบกำหนดช่วง Slice
tup=(12,42,3.442,"dsawf")
print(tup[-4:])
print(tup[:-1])
"""

"""
การแก้ไขข้อมูล
tup=(12,42,3.442,"dsawf")
lis=list(tup) # เปลี่ยน tuple เป็น list
lis[0]="loog"

tup=tuple(lis)
"""

"""
การ Loop
tup=(12,42,3.442,"dsawf")
for item in tup:
    print("สมาชิก ", item)
"""

"""
ตรวจสอบข้อมูล
tup=(12,42,3.442,"dsawf")
if "loog" in tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")
"""

"""
นับจำนวนสมาชิก
tup=(12,42,3.442,"dsawf")
print(len(tup))
"""
"""
len() ทำงานร่วม Loop for
tup=(12,42,3.442,"dsawf")
for item in range(len(tup)):
    print(tup[item])
"""
"""
#การสร้างและเพิ่มข้อมูล (Join)
name=("Loog","Bon")
new=("Lugh",) แบบ 1
neww="Bonn" แบบ 2
name=name+new+(neww,) 
print(name)
"""

"""#ทำงานร่วมกับ list
tup=(12,42,3.442,"dsawf")
city=["กทม","ชล","อุบล"]

tup=tup+tuple(city)
print(tup)"""

"""
#การลบข้อมูล del, การลบแบบ list
tup=(12,42,3.442,"dsawf")
lis=list(tup)
lis.pop() # เอาตัวท้ายสุดออก
lis.remove(42)
tup=tuple(lis)
print(tup)
"""

"""
#ค้นหาและนับจำนวนสมาชิก count , index
tup=(12,42,4,4,3.442,"dsawf")
x=tup.count(4) # ค้นหาว่า 4 มีอยุ่กี่ตัว
y=tup.index(3.442) # ค้นหาว่า อยุ่ที่ตัวแหน่งไหน
print(x)
print(y)
"""



# การ sort ข้อมูล
tup=(12,42,3.442,4,1,2,6,5,11,224,532)
lis=list(tup)
print("ก่อนเรียง = ", lis)
lis.sort()
tup=tuple(lis)
print("หลังเรียง = ", tup)




