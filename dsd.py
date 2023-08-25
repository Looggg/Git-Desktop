import math

a = float(input("ป้อนค่า a: "))
if a > 0:
    b = float(input("ป้อนค่า b: "))
    c = float(input("ป้อนค่า c: "))
    y=b**2-4*a*c
    if y > 0:
        y1 = (-b + math.sqrt(y)) / (2*a)
        y2 = (-b - math.sqrt(y)) / (2*a)
        print("มีสองคำตอบ")
        print("คำตอบที่ 1: ",y1)
        print("คำตอบที่ 2: ",y2)
    elif y == 0:
        y = -b / (2*a)
        print("มีคำตอบเดียว")
        print(y)
    else:
        print("ไม่มีคำตอบ")
else:
    print("a ต้องไม่เท่ากับ 0")