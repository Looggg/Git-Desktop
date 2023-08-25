# Fibonacci number 
# 0, 1, 1, 2, 3, 5, 8, ....
# ฟังก์ชั่น เรียก ฟังก์ชั่นตัวเอง
def fibonacci(number):
    if number<=1 : # หา 2 ลำดับแรกก่อน
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
for i in range(10): # 0, 1, 1, 2, 3
    print(fibonacci(i))

        

