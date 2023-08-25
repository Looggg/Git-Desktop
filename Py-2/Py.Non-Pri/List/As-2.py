# หาค่า มาก น้อย

number=[]
while True:
    x=int(input("ป้อนตัวเลข"))
    if x<0:
        break
    number.append(x)

print(number)
print("ค่ามากสุด ",max(number))
print("ค่าน้อยสุด ",min(number))
print("ผลรวม ",sum(number))