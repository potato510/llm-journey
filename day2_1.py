# 【语法卡片】if / for / while / break / continue → 见同目录 day2.py 顶部



print("=== 练习 2  ===");
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和是：{total}");  


for i in range(1, 101):
    if i % 3 == 0:
        print(f"{i}是3的倍数");

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
        print(f"{i}是偶数");
print(f"1到100的偶数和是：{total}");