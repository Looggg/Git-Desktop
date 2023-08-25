x = "yes"
while x == "yes":
    password = input("ป้อนชื่อ")
    # print("ครั้งที่ ", x)
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    if 6 <= len(password) <=16:    
        for char in password:
            if 'a' <= char <= 'z':
                count_lower += 1
            elif 'A' <= char <= 'Z':
                count_upper += 1
            elif '0' <= char <= '9':
                count_digit +=1
            elif char in ['$', '#', '@']:
                count_special +=1
        if count_lower>=1 and count_upper>=1 and count_digit>=1 and count_special>=1:
            x = "no"
        x+=1
    # print("ชื่อไม่เหมาะสม")
#SADsa21
print("ออกจากโปรแกรม")