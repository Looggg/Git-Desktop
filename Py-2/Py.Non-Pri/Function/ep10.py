# **kwargs ค่าเป็น dic -> ชื่อ parameter มีได้หลายชื่อ

# *args ค่าเป็น tuple -> ค่าใน parameter มีได้หลายค่า
def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

def displaydata(**item):
    print(item)

displaydata(fname="Lugh Bon",age="19",city="meatod")
displaydata(local="บ้านนอก",locall="บ้านใน",lod=11)
