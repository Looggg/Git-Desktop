# Exception
while True:
    try:
        number1=int(input("ป้อนตัวเลขที่ 1 :"))
        number2=int(input("ป้อนตัวเลขที่ 2 :"))
        if number1 and number2 == None:
            break
        result=number1/number2
        print(result)
    except Exception as e: #ลดรูป
        print(e) 
    finally : # ทำงานหมดไม่สน error
        print("ทำงานต่อไปไม่สนว่า Error หรือไม่")
    