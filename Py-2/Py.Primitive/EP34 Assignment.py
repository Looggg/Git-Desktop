#ทายลูกเต๋า

import random

myrandom=random.randrange(1,7)
k=1
print(myrandom)
correct=False
while True:
    number=int(input("ป้อนคำตอบ :"))
    if number<0 or number>6 or k==3:
        break
    correct=(number==myrandom) # true / false
    
    if not correct :
        if(number>myrandom):
            print("น้อยกว่านี้")
        if(number<myrandom):
            print("มากกว่านี้")
    if correct :
        print("")
        print("รับรางวัลไปเลย ควย")
        if number:
            break
    k+=1
    
print("")
if not correct :
    print("เสียใจด้วยไอ่โง่")
    print("คำตอบคือ :",myrandom)
    