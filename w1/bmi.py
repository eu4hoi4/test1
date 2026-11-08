h=int(input("请输入你的身高"))
w=int(input("请输入你的体重"))
bmi=w/(h*h)
if bmi<18.5:
    print("偏瘦")
elif bmi<24:
    print("正常")
elif bmi<28:
    print("偏胖")
else:
    print("肥胖")