import math

result=math.sqrt(64) # ฟังก์ชั่นรูท
score=math.floor(80.4) # ปัดเศษลง
score=math.ceil(80.4)  # ปัดขึ้น

# ค่าทางตรีโกณมิติ
convert = math.radians(90) # degrees -> radians
x=math.sin(convert) # เอาค่าที่เปลี่ยนมาใส่ใน sin
print(x)

#หาระยะระหว่างจุดสองจุด
point1=[5,4]
point2=[5,13]
d=math.dist(point1,point2) #คำนวณระยะทางจากจุด 1 -> 2
print(d)

#ลอการิทึม
l1=math.log10(32)
print(l1)

