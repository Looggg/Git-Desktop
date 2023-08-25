# list1 = list(range(1, 11))
# sum1 = 0
# for i in range(len(list1)):
#     if i % 2 != 0:
#         print(i)
#         sum1 += list1[i] ** 2
# print(sum1)

# list1 = list(range(1, 11))
# sum1 = 0
# for i in range(len(list1)):
#     if list1[i] % 2 != 0:
#         print(list1[i])
#         sum1 += list1[i] ** 2
# print(sum1)

# list1 = list(range(1, 11))
# sum1 = 0
# for i in range(len(list1)):
#     if i % 2 != 0:
#         print(i)
#         sum1 = sum1 + list1[i] ** 2
#     else :
#         print(i)
#         sum1 = sum1 + list1[i]
# print(sum1)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd_index_values = list1[1::2]  # ดึงสมาชิกที่มีดัชนีเป็นเลขคี่

# sum_of_odd_index_squares = sum([value ** 2 for value in odd_index_values])

# print("ผลบวกกำลังสองของสมาชิกที่ index ที่เป็นเลขคี่:", sum_of_odd_index_squares)

# x=int(input("xxx"))
# y=int(input("xxx"))
# sum1 = 0
# for i in range(x,y+1):
#     print("แม่ที่ :",i)
#     for o in range(1,13):
#         print(i,"*",o,"=",i*o)
#         c=i*o
#         sum1 += c
# print(sum1)

# x=int(input("xxx"))

# for a in range(1,x+1):
#     for b in range(2,a+1):
#         print(b,end="")
#     print("")
# while True:
#     start=int(input("ป้อนแม่สูตรคูณ = "))
#     stop=int(input("ป้อนแม่สูตรคูณ = "))
#     c = "yes"
#     for x in range(start,start+1):
#         print("แม่ = ",x)  
#         for y in range(1,13):
#             print(x," * ",y," = ",(x*y))
#     print("Do you want continue")
#     c=input("xxx")
    # if a == "yes":
    #     print("กลับไปทำอีกครั้ง")
    # elif a == "no":
    #     break
    # else:
    #     print("ป้อนไม่ถูกต้อง")    


# for n in range(2, 10):
#     for x in range(2, n): # (2, n-1)
#         if n % x == 0:
#              print(n, 'equals', x, '*', n//x)
#              break
#     print(n, 'is a prime number')


# password=input("xxx")
# re = 1
# while re <= 3:
#     if 6 <= len(password) <= 16:
#         small = False
#         big = False
#         num = False
#         char = False
#         special = ['@','#','$']
#         for i in password:
#             if 'a' <= i <= 'z':
#                 small = True
#             elif 'A' <= i <= 'Z':
#                 big = True
#             elif '0' <= i <= '9':
#                 num = True
#             elif i in special:
#                 char = True

#         if small and big and num and char:
#             print("เหมาะสม")
#             # break
#         else:
#             print("ไม่เหมาะ")
#     else:
#         print("รหัส......")

# x=input("xxx")
# for i in range(len(x)):
#     if i % 2 == 0 and i != 0:
#         print(x[i])

list1 = [] #
for i in range(1,11):
    x=int(input("xxx :"))
    list1.append(x)
even = 0
odd = 0
for a in list1:
    if a % 2 == 0:
        even = even+ 1
    else:
        odd = odd + 1
print("เลขคู่ :",even,"เลขคี่ :",odd)

