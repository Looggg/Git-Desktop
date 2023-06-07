# หาเลข คู่ คี่

number=[]
odd=[] #เลขคี่
even=[] #เลขคู่

while True:
    x=int(input("ป้อนตัวเลข"))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else :
        odd.append(x)   
    number.append(x)

odd.sort()
even.sort()
print("เลขทั้งหมด ",number)
print("เลขคี่ ",odd)
print("เลขคู่",even)