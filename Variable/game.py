import random

RanNum = random.randint(1,100)
CustNum = input("猜猜数字是多少：")
New_CustNum = int(CustNum)
if New_CustNum > RanNum:
    print("给的数字太大啦。")
elif New_CustNum < RanNum:
    print("给的数字太小啦。")
else:
    print("猜对啦！")
count = 1
while New_CustNum != RanNum:
    CustNum = input("猜猜数字是多少：")
    New_CustNum = int(CustNum)
    if New_CustNum > RanNum:
        print("给的数字太大啦。")
    elif New_CustNum < RanNum:
        print("给的数字太小啦。")
    else:
        print("猜对啦！")
    count += 1
    if count == 5:
        print("机会已用完")
        break
