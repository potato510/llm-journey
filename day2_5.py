# 【语法卡片】if / for / while / break / continue → 见同目录 day2.py 顶部

print("=== 练习 6  ===")

rows = int(input("请输入行数："))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()