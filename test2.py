while True:
    password = input("กรุณาใส่พาสเวิร์ด: ")

    if len(password) < 6 or len(password) > 16:
        print("พาสเวิร์ดไม่เหมาะสม")
    elif not any(c.isalpha() for c in password):
        print("พาสเวิร์ดไม่เหมาะสม")
    elif not any(c.isdigit() for c in password):
        print("พาสเวิร์ดไม่เหมาะสม")
    elif not any(c in "$#@@" for c in password):
        print("พาสเวิร์ดไม่เหมาะสม")
    else:
        print("พาสเวิร์ดเหมาะสม")
        break