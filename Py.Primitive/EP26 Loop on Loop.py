# loop ซ้อน loop

# i=1
# while i<=3 : #เมื่อเป็นจริง
#     j=1 # ตัวนับ
#     while j<=5:
#         print("รอบที่ = ",i,"ตำแหน่งที่ = ", j) 
#         j+=1
    
#     i+=1
    
for i in range(1,4):
    print("รอบที่ = ",i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ",j)