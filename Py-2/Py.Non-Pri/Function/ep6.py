# Arbitrary Arguments (args)
# *agrs

def add(*Lugh):
    sum=0
    for i in range(len(Lugh)):
        sum+=Lugh[i]
    print(sum)

add(10,20,13,44,2)