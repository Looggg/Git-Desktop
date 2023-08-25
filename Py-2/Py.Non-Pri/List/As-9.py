# การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["aa","aab", "cba", "bba","as", "asda"]
result=[]

for item in message:
    result.append(item.count("a"))
print(result)