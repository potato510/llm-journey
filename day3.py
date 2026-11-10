print("=== 练习 1  ===")

def calc(a,b):
    return a + b, a - b, a * b, a / b, a % b, a ** b, a // b


i0, i1, i2, i3, i4, i5, i6 = calc(int(input("请输入第一个数字：")), int(input("请输入第二个数字：")))
print(f"两个数字的和是：{i0}");
print(f"两个数字的差是：{i1}");
print(f"两个数字的积是：{i2}");
print(f"两个数字的商是：{i3}");
print(f"两个数字的余数是：{i4}");
print(f"两个数字的幂是：{i5}");
print(f"两个数字的整除是：{i6}");


def greet(name, greeting="你好"):
    print(f"{greeting}，我叫：{name}");

greet(input("请输入姓名："), input("请输入问候语（默认为：你好）：") or "你好" );


def is_adult(age = 10):
    return age >= 18

is_adult_result = is_adult(int(input("请输入年龄（默认为：18）：") or 18))
if is_adult_result:
    print("你是成年人")
else:
    print("你是未成年人")
