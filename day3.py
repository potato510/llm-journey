# ═══════════════════════════════════════════════════════════════════
# Day3-4 语法卡片 · 函数 / 字典 / 集合 / 文件读写 / JSON
# ═══════════════════════════════════════════════════════════════════
# 函数
#   def calc(a, b):
#       return a + b, a - b            # 多返回值 → 元组，可解包：x, y = calc(1, 2)
#   def greet(name, greeting="你好"):  # 默认参数
#       return f"{greeting}，{name}"
#   规则：函数只 return 数据，打印交给调用方
#
# 异常（与函数契约配合）
#   raise ValueError("...")            # 函数里抛
#   try:
#       ...
#   except ValueError as e:            # 调用方接
#       print(e)
#
# 字典 / 集合 / 推导式
#   for name, score in scores.items():
#   {name: s for name, s in scores.items() if s >= 60}   # 字典推导式
#   set([1, 2, 2]) → {1, 2}                              # 去重
#   set(a) & set(b) / - / |                              # 交 / 差 / 并
#
# 文件读写（一定写 encoding="utf-8"，用 with 自动关闭）
#   with open("a.txt", "r", encoding="utf-8") as f:
#       content = f.read()      # 或 lines = f.readlines()
#   with open("a.txt", "w", encoding="utf-8") as f:
#       f.write("...")
#
# JSON（字典 ↔ 文件）
#   import json
#   json.dump(data, f, ensure_ascii=False, indent=2)   # 写，中文不转义
#   data = json.load(f)                                 # 读
#   异常：except (FileNotFoundError, json.JSONDecodeError)   # 文件不存在 / 内容损坏
# ═══════════════════════════════════════════════════════════════════
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
