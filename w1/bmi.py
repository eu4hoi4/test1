h=float(input("身高（米，例如 1.75）："))
w=float(input("体重（kg）："))
bmi=w/(h*h)
print(f"你的bmi是{bmi:.2f}")
if bmi<18.5:
    print("偏瘦")
elif bmi<24:
    print("正常")
elif bmi<28:
    print("偏胖")
else:
    print("肥胖")