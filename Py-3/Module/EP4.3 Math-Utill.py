#แฮกรหัส ATM = 132
import random

ATM_PASSWORD = "132"
result = "" #เก็บผลลัพธ์

while result!=ATM_PASSWORD:
    result=""
    for lettet in range(len(ATM_PASSWORD)):
        list_number=random.choice("0123456789")
        result="".join(list_number)+str(result)
        print("SEARCH = ", result)
print("CRACK PASSWORD IS ", result)        
