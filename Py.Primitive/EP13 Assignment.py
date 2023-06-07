#คำนวณ BMI

# input
weight=int(input("ป้อนน้ำหนัก (kg): "))
height=int(input("ป้อนส่วนสูง (cm): "))

#process
#cm => m
height=height/100
#calculate
bmi=weight/height*height

#output
print("BMI =",bmi)