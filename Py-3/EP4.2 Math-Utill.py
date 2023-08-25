import random
items=[1,2,3,4,5,"A","B","C","D"]
for i in range(10):
    #x=random.random() # 0.0 - 1.0
    x=random.uniform(5,10) # 5 <= x <10
    # y=random.randrange(1,10,2) 
    # y=random.randint(1,5) # 1 - 5
    y = random.choice(items) # random list
    y = random.choice([1,2,3,4,5,"A","B","C","D"]) # random list
    y = random.choice("1234ABCD") # random list
    random.shuffle(items) # สลับข้อมูลใน list
    # print(x)
    # print(y)
    print(items)

