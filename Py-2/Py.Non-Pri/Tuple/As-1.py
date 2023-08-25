# นำค่าใน tuple ใส่ใน ตัวแปร

tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
d=a+b
print(d)

# สลับ tuple
x=(50,10)
y=(2,4)
print(x)
print(y)
x,y=y,x
print(x)
print(y)

# tuple => String
character=('L','o','o','g')
print(character)
name="".join(character) 
print(name)

# reverse tuple
t=(100,22,355,112,54,95,200)
print("ก่อน reversed = ", t)
u=tuple(reversed(t))
i=reversed(t)
print(u)
print(list(i)) #หรือ  print(tuple(i))
