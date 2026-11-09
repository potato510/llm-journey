import random
print("=== 练习 4  ===")

num = random.randint(1, 100)
step = 1
conjecture = input("请输入一个数字：")
success = False
while success != True:
    if int(conjecture) > num:
        print("你输入的数字大了")
    elif int(conjecture) < num:
        print("你输入的数字小了")
    else:
        print("恭喜你，猜对了！")
        success = True
        break
    if step >=7:
        print(f"你已经猜了{step}次了，游戏结束！，正确的数字是：{num}")
        break
    step += 1
    conjecture = input("请重新输入一个数字：")
