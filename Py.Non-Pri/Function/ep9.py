# Function return ค่า

def randomnumber(x): # Parameter ตัวรับค่าที่ส่งเข้ามาจาก Argument    
    if x == "100":
        print("ถูกหวย")
        return(1000)
    else:
        print("ไม่ถูกหวย")
        return(0)

money=randomnumber("100") # Arguments ตัวที่ส่งข้อมูลไป
x=300 #สมมุติซื้อหวยเป็นหนี้ 300
result=money-x
print("เงินางวัล = ",money)
print("คงเหลือ = ",result)