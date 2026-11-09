cnt=0
while(cnt<5):
    a = int(input("请输入一个数"))
    if(a<42):
        print("小了")
        cnt=cnt+1
    elif(a>42):
        print("大了")
        cnt=cnt+1
    else:
        cnt=cnt+1
        print(f"猜中了。你用了{cnt}次机会")
        break