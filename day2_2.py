# 【语法卡片】if / for / while / break / continue → 见同目录 day2.py 顶部

print("=== 练习 3  ===")

i = 1 
j = 1

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()
