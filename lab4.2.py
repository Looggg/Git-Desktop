order = input("ป้อนเมนูไข่ที่ต้องการ (ไข่ต้ม, ไข่ดาว, ไข่เจียว) :")

if order in ["ไข่ต้ม", "ไข่ดาว", "ไข่เจียว"]:
    amount = int(input("ป้อนจำนวนไข่ที่ต้องการ :"))
    if amount > 0:
        if order == "ไข่ต้ม":
            price = amount*5
            print(price, "บาท")
        elif order == "ไข่ดาว":
            price = amount*7
            print(price, "บาท")
        elif order == "ไข่เจียว":
            price = amount*10
            print(price, "บาท")
        else :
            print("ร้านเรามีเมนู ไข่ต้ม ไข่ดาว และไข่เจียว")
    else:
        print("ใส่จำนวนเต็มบวกเท่านั้น")
else :
    print("ร้านเรามีเมนู ไข่ต้ม ไข่ดาว และไข่เจียว")