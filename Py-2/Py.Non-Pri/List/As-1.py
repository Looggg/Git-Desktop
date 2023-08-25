# เรียงลำดับข้อมูล (เป็นจำนวนบวก)

number=[]
while True:
    x=int(input("ป้อนตัวเลข"))
    if x<0:
        break
    number.append(x)
    
print("ก่อนเรียง ",number)
number.sort()
print("หลังเรียง ",number)
number.reverse()
print("เรียง มากไปน้อย ",number)
print("จบโปรแกรม")
