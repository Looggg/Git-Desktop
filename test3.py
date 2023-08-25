while True:
    password = input("ป้อนพาสเวิร์ด")
    if 6<=len(password)<=16:
        small = False
        big =False
        num = False
        char = False
        special = ['@','#','$']
        for i in password:
            if 'a' <= i <= 'z':
                small = True
            elif 'A' <= i <= 'Z':
                big = True
            elif '0' <= i <= '9':
                num = True
            elif i in special:
                char = True
        if small and big and num and char:
            print("รหัสเหมาะสม")
            break
        else :
            print("รหัสไม่เหมาะสมลองอีกครั้ง")
    else:
        print("รหัสไม่เหมาะสมลองอีกครั้ง")
