import numpy as np
"""
list & Array
-Array สมาชิกใน Array มีชนิดข้อมูลเหมือนกัน
-list สมาชิกชนิดต่างกันได้

-Array ขนาดที่แน่นอนเปลี่ยนแปลงขนาดไม่ได้
-list มีขนาดที่ยืดหยุ่นกว่า
"""

# .ndim แสดงข้อมูลสมาชิก
a = np.array([1, 2, 3])
print(a.ndim)
li = [1, 2, 3, 4]
b = np.array(li)
print(type(b))
print(b)

# การเข้าถึงสมาชิก
# a[dept][row][colum]
