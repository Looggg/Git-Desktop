# if ซ้อน if
age=int(input("ป้อนอายุ :"))

if age<=15:
    if age==15:
        pass #pass คือข้ามไปก่อน
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    else :
        print("ประถม")
else :
    print("มอปลาย")
    
print("จบโปรแกรม")