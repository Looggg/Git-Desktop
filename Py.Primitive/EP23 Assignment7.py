#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) : ") #45C

degree=int(temp[:-1]) #45
unit=temp[-1].upper()    #C

if unit=="C":
    #แปลงเป็นฟาเรน
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
    unit.replace("C", "F")
    print("แปลงตัวเลข = ",temp," เป็น",unit_result," = ",result,unit.replace("C", "F")) 
if unit=="F":
    #แปลงเป็นเซลเซียส
    result=(degree-32)*5/9
    unit_result="เซลเซียส"
    unit.replace("F", "C")
    print("แปลงตัวเลข = ",temp," เป็น",unit_result," = ",result,unit.replace("F", "C")) 



    
    