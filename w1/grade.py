grade=int(input("输入你的成绩"))
if(grade<0 or grade>100):
    print("成绩无效")
else:
    if(grade<70):
        if(grade<60):
            print("E")
        else:
            print("D")
    else:
        if(grade<80):
            print("C")
        else:
            if(grade<90):
                print("B")
            else:
                print("A")

