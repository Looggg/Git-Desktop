try:
    fw=open("Score.txt","a",encoding="utf-8")
    while True:
        studentid=input("ป้อนรหัสนักเรียน : ")
        if studentid == "exit":
            break
        score=input("ป้อนคะแนน : ")
        fw.writelines(studentid+"\t"+score+"\n")
    fw.close()
    fr=open("Score.txt","r",encoding="utf-8") # อ่านไฟล์
    fa=open("Grade.txt","a",encoding="utf-8")
    grade = None # เขียนค่าข้างนอก loop 
    for line in fr.readlines():    # --> line = fr.readlines() แสดงข้อมูล
        score = line[-4:].strip() #ลบช่องว่าง (คะแนนนักเรียน) #s01 12
        studentid = line[:-4].strip() # ชื่อนักเรียน
        # print("รหัส = ",studentid," คะแนน = ",score)
        score = int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<80:
            grade="B"
        elif score>=50 and score<=69:
            grade="C"
        else:
            grade="F"
        print("รหัส = ",studentid," คะแนน = ",score," Grade = ",grade)
        fa.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fa.close()
    fr.close()
except Exception as e:
    print(e)

