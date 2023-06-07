start , stop = 1,5
sum ,avg =0,0
while(start<=stop):
    num=int(input("ป้อนตัวเลข = "))
    sum+=num # บวกเลขที่ป้อนแต่ล่ะรอบ
    start+=1
    
avg=sum/stop
print("ผลรวม = ", sum)
print("ค่าเฉลี่ย = ", avg)
    