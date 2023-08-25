# Union
"""x={"AA","BB","CC","DD"}
y={"aa","bb","cc","dd"}

all=x.union(y) เอา x รวมกับ y
print(all)
x.update(y) เอา y ใส่ใน x
print(all)"""

""" 
# copy
x={"AA","BB","CC","DD"}
y={"aa","bb","cc","dd"}
c=x.copy()
print(c)
"""

# differnece อะไรต่างกันบ้าง
"""x={"AA","BB","CC","DD","aa","bb"}
y={"aa","bb","cc","dd"}

c=x.difference(y)
x.difference_update(y)
print(c)
"""
"""
# Intersection อะไรเหมือนกัน
x={"AA","BB","CC","DD","aa","bb"}
y={"aa","bb","cc","dd"}

c=x.intersection(y)
x.intersection_update(y)
print(c)
"""
"""
# Subset
fish={"ปลาดุก","ปลาหมอ","ปลาวาฬ"}
x={"ปลาหมอ","ปลาซิว"}

print(x.issubset(fish)) # เช็คว่า x เป็น subset ของ fish ไหม 
print(fish.issuperset(x)) # เช็คว่า fish เป็น superset ของ x ไหม
# ตอบเป็น T, F
"""
"""
# min max
number={12,14,134,1253,665}
print(min(number))
print(max(number))

"""