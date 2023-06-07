#คุณสมบัติของการ return

def randomnumber(x):     
    if len(x)<3: #ตัวเลขน้อยกว่า 3 หลัก
        return 
    if x == "100":
        print("ถูกหวย")
        return(1000)
    else:
        print("ไม่ถูกหวย")
        return(0)

money=randomnumber("10") 
print("เงินรางวัล = ",money)