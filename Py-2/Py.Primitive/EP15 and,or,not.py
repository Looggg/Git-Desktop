#การใช้ and or not ตามตาราง
# and
age=int(input("ป้อนอายุ ")) 
# if not age>=15 and age<20:
#    print("วัยรุ่น")
if age>=15 and age<20:  #and ต้องจริงทั้งคู่
    print("วัยรุ่น")       #or เป็นจริงอันเดียว
elif age>=20 and age <30: 
    print("วัยผู้ใหญ่")
elif age>=30 and age<60:
    print("วัยทำงาน")
elif age>=60:
    print("วัยชรา")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")

