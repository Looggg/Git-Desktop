# การสร้าง dict
# ชื่อตัวแปร = {key:value, key:value, ....} สร้างได้ 2 แบบ
"""colors={"red":"สีแดง"}
pets=dict(cat="แมว")

print(colors["red"])
print(pets.get("cat"))
print(pets["cat"])"""

# แก้ข้อมูล
"""colors={"red":"สีแดง"}
pets=dict(cat="แมว")

colors["red"]="สีเขียว"
print(colors["red"])"""

# เพิ่มข้อมูล ความสามารถ update เพิ่มข้อมูลและหาเจอข้อมูลที่ซ้ำจะแก้ไขให้
"""colors={"red":"สีแดง"}
pets=dict(cat="แมว")
colors.update({"blue":"น้ำเงิน", "orange":"ส้ม","red":"สีสมพู"})
print(colors)"""

# ดึงสมาชิกมาใช้
"""colors={"red":"สีแดง","blue":"น้ำเงิน", "orange":"ส้ม","red":"สีสมพู"}
for x in colors:
    print(x) # แสดงข้อมูลเป็น key
for x in colors.values():
    print(x) # แสดงเป็น values
for x,y in colors.items():
    print(x,y) # แสดงทั้งสอง"""

# ลบข้อมูล
""""colors={"red":"สีแดง","blue":"น้ำเงิน", "orange":"ส้ม","red":"สีสมพู"}
colors.pop("red")
colors.popitem() # ลบข้อมูลที่อยู่หลังสุดออก
colors.clear() # เคลียข้อมูล
del colors # ลบตัวแปร
#คัดลอก 
x=colors.copy()
print(x)"""

# ทำ dict ซ้อน dict 
market={
    "ร้าน A":{
        "name":"9A",
        "menu":["กระเพรา","มันไก่"],
        "zone":"หน้าตลาด"
    },
    "ร้าน B":{
        "name":"9B",
        "menu":["นมปั่น","ชาเย็น"],
        "zone":"หลังตลาด"
    },
    "ร้าน C":{
        "name":"9C",
        "menu":["มะม่วง","มังคุด"],
        "zone":"กลางตลาด"
    }
}
print(market["ร้าน C"]["menu"])
print("มังคุด" in market["ร้าน C"]["menu"])

if "มังคุด" in market["ร้าน C"]["menu"]:
    print("เป็น")
else:
    print("ไม่เป็น")
