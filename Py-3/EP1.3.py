# สร้าง Exception ด้วย Raise
# เขียนภายใน try
while True:
    try:
        number1=int(input("ป้อนตัวเลขที่ 1 :"))
        number2=int(input("ป้อนตัวเลขที่ 2 :"))
        if number1 == 0 and number2 == 0:
            break
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้") #ส่งค่าไป except เลย
        result=number1/number2
        print(result)
    except Exception as e: #ลดรูป
        print(e) 
    finally : # ทำงานหมดไม่สน error
        print("ทำงานต่อไปไม่สนว่า Error หรือไม่")