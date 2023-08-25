
import datetime

result=datetime.datetime.now() # ดึงวัน / เวลาปัจจุบันมาใช้งาน
# print(result.year)
# print(result.month)

newdate=datetime.datetime(2023,7,21,15,30,12) # yyyy,m,d,h,m,s
# print(newdate)

# จัดรูปแบบการแสดงผล
print("start = ", result)
# x=result.strftime("%x")# m/d/y
# print(x)
print(result.strftime("%x")) # m/d/y สั้น
print(result.strftime("%X")) # เวลา time
print(result.strftime("%c")) # ครบ ละเอียดเลย

#เวลา
print(result.strftime("%H:%M:%S %p")) # %H แสดงชั่วโมง Mนาที Sวินาที pหน่วยเวลามี AM,PM
# 1 - 366 day
print(result.strftime("%j")) # 
# date
print(result.strftime("%a")) # แสดงชื่อวันแบบสั้น
print(result.strftime("%A")) # แสดงชื่อวันแบบเต็ม
print(result.strftime("%w")) # ลำดับวัน เริ่มที่0 = sunday
print(result.strftime("%d")) # วันที่
print(result.strftime("%b")) # เดือนแบบสั้น
print(result.strftime("%B")) # เดือนแบบเต็ม

# d/m/y 
print(result.strftime("%d %m %Y")) # mเล็ก เดือน Yใหญ่ปี


