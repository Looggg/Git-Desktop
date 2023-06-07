# โครงสร้างควบคุม (Control Structure)
# แบบลำดับ(แบบปกติ จากบนลงล่าง), เลือก, ทำซ้ำ

# แบบเลือก if

#input
name=input("ป้อนชื่อ ")
age=int(input("ป้อนอายุ "))

# age==15 #ตัวดำเนินการเปรียบเทียบมีชนิดข้อมูลเป็น boolean
#  if boolean expression: #expression(เงื่อนไขการทำงาน เป็นบลูลีน)
#      statement
# if เงื่อนไขเป็นจริง : จึงจะทำงาน

if age>=15:
    print("นาย"+name)
# แบบเลือก if...else
if age>=15:
    print("วัยรุ่น")
elif age>=20: #elif จะไม่เชคกรณีต่อๆไปถ้าเมื่อกรณีแรกเป็นจริง
    print("วัยผู้ใหญ่")
elif age>=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")
