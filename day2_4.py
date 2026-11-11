# 【语法卡片】if / for / while / break / continue → 见同目录 day2.py 顶部

print("=== 练习 5  ===")

# for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz");
#         if i % 3 == 0:
#             print("Fizz");
#         elif i % 5 == 0:
#             print("Buzz");
#         else:
#             print(i);

i = 1;
count3 = 1
count5 = 1
while i <= 100:
    if count3  == 3 and count5 == 5:
        print("FizzBuzz")
        count3 = 0
        count5 = 0
    elif count3 == 3:
        print("Fizz")
        count3 = 0
    elif count5 == 5:
        print("Buzz")
        count5 = 0
    else:
        print(i)
    i += 1
    count3 += 1
    count5 += 1
