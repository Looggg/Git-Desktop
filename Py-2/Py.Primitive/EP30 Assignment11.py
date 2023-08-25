#หาค่ามากสุด น้อยสุด

max ,min = 0,0

while True :
    number=int(input("ป้อนตัวเลข :"))
    if number<0 :
        break
    if number>max :
        max=number
    if number<min :
        min=number