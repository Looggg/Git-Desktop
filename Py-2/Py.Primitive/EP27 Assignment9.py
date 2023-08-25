# แม่สูตรคูณ

start=int(input("ป้อนแม่สูตรคูณ = "))
stop=int(input("ป้อนแม่สูตรคูณ = "))

for x in range(start,start+1):
    print("แม่ = ",x)  
    for y in range(1,13):
        print(x," * ",y," = ",(x*y))
            