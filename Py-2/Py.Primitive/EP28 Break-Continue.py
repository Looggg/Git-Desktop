# Break/Continue

# i=1
# while i<=10:
#     print("รอบที่ = ",i)
#     if (i==5):
#         break # หยุดที่ตัวนี่
#     i+=1
# else:
#     print("จบโปรแกรม")    

# i=1
# while i<=10:
#     i+=1
#     if (i%3 != 0): #หารเหลือเศษ
#         continue # กระโดดข้าม
#     print("รอบที่ = ",i)
# else:
#     print("จบโปรแกรม")    

for i in range(1,11):
    if(i%2 == 0):
        continue
    print(i)
    
print("จบโปรแกรม")

for i in range(1,11):
    print(i)
    if(i==5):
        break
    
print("จบโปรแกรม")
