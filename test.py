
while True:
    password = input("ป้อนพาสเวิร์ด: ")
    x = False
    lower = 0
    upper = 0
    digit = 0
    special = 0
    
    if 6 <= len(password) <= 16:
        for i in password:
            if 'a' <= i <= 'z':
                lower += 1
            elif 'A' <= i <= 'Z':
                upper += 1
            elif '0' <= i <= '9':
                digit += 1
            elif i in ['$', '#', '@']:
                special += 1
        
        if lower >= 1 and upper >= 1 and digit >= 1 and special >= 1:
            x = True
    
    if x:
        print("พาสเวิร์ดถูกต้องและเหมาะสม")
        break
    else:
        print("พาสเวิร์ดไม่เหมาะสม")
