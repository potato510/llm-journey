

print("=== 练习 1  ===")
score = int(input("请输入你的成绩："))
if score > 100 or score < 0:
    print("输入的成绩不在有效范围内")
elif score >= 90:
    print("你的成绩是A")
elif score >= 80:
    print("你的成绩是B")
elif score >= 70:
    print("你的成绩是C")
elif score >= 60:
    print("你的成绩是D")
else:
    print("你的成绩是E")