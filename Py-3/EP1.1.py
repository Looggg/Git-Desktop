
try:
#    number1=int(input("ป้อนตัวเลข 1 :"))
#    number2=int(input("ป้อนตัวเลข 1 :"))
#    result=number1/number2
#    print(result)
    score=100+"50"
    print(score)
except ValueError: # ค่าผิดพลาด
    print("ป้อนตัวเลขเท่านั้น")
except ZeroDivisionError: # 
    print("ห้ามหารด้วย 0")
except TypeError:
    print("ชนิดข้อมูลไม่ตรงกัน")
else :
    print("จบโปรแกรม")    
        
# ลดรูป    
try:
    number1=int(input("ป้อนตัวเลข 1 :"))
    number2=int(input("ป้อนตัวเลข 1 :"))
    result=number1/number2
    print(result)
except Exception as e: #ลดรูป
    print(e) 
else: #เพิ่มได้
    print("จบโปรแกรม")
finally : # ทำงานหมดไม่สน error
    print("ทำงานต่อไปไม่สนว่า Error หรือไม่")
