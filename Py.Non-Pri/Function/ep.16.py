# lambda function
"""
lambda arguments : expression
"""
#sum=lambda x,y : x+y
#print(sum(1,2))

def myPower(x):
    # x = ตัวเลข
    # a = เลขชี้กำลัง
    return lambda a : x**a

y=myPower(5)
result=y(3)

print(result)
