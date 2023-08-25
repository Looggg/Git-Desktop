# Bank Program

# Data
account = {"นายA":5000, "นายB":0}

def getBlance():
    print("ยอดเงินคงเหลือในบัญชี :",account)

def deposit(money):
    print("ฝากเงินเข้าบัญชี A :",money)
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่าไหร่")
    account["นายA"]+=money

def withdraw(money):
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่าไหร่")
    if money>account["นายA"]:
        raise Exception("ยอดเงินในบัญชีไม่พอ")
    print("ถอนเงินจากบัญชี A :",money)
    account["นายA"]-=money

def tranfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ต้องป้อนค่าเป็นตัวเลขจำนวนเต็มเท่านั้น")
    if money<=0:
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่าไหร่")
    if money>account["นายA"]:
        raise Exception("ยอดเงินในบัญชีไม่พอ")
    print("ทำการโอนเงินไปที่บัญชี B :",money)
    account["นายB"]+=int(money)
    account["นายA"]-=int(money)

try:
    getBlance()
    tranfer(234)
    getBlance()
except Exception as e:
    print(e)
