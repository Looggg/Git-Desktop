import math

def solve_quadratic_equation(a, b, c):
    # คำนวณค่า delta
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # มีสองคำตอบจริง
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        # มีคำตอบเดียว
        x = -b / (2*a)
        return x,
    else:
        # ไม่มีคำตอบจริง
        return ()

a = float(input("ป้อนค่า a: "))
b = float(input("ป้อนค่า b: "))
c = float(input("ป้อนค่า c: "))

solutions = solve_quadratic_equation(a, b, c)

if len(solutions) == 0:
    print("ไม่มีคำตอบจริง")
elif len(solutions) == 1:
    print("มีคำตอบเดียว:", solutions[0])
else:
    print("มีสองคำตอบ:", solutions[0], "และ", solutions[1])
