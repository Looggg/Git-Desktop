# คำนวณ BMI
weight=int(input("ป้อนน้ำหนัก (kg):"))
height=int(input("ป้อนส่วนสูง :"))/100

bmi = weight/(height**2)

result="ไม่ทราบค่าที่ชัดเจน"
if bmi<18.0:
    result="ต่ำกว่าเกณ"
elif bmi>=18.5 and bmi <=22.9:
    result="สมส่วน"
elif bmi>=23.0 and bmi <=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi <=29.9:
    result="โรคอ้วน ระดับ 1"
elif bmi>30:
    result="โรคอ้วนสัสๆ"
else :
    result="ไม่ทราบค่าที่ชัดเจน"


print(bmi)
print(result)

