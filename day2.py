# ═══════════════════════════════════════════════════════════════════
# Day2 语法卡片 · 流程控制（if / for / while）
# ═══════════════════════════════════════════════════════════════════
# if / elif / else
#   if score >= 90:
#       ...
#   elif score >= 80:
#       ...
#   else:
#       ...
#   逻辑：and / or / not        比较：== != > >= < <=
#
# for（遍历序列或 range）
#   for i in range(1, 101):        # 1~100（不含 101）
#   for x in [1, 2, 3]:
#   for i, (k, v) in enumerate(d.items()):
#   break / continue               # 跳出循环 / 跳过本次
#
# while
#   while 条件:
#       ...
#       if 结束条件: break          # ⚠ 必须有退出条件或 break，否则死循环
#
# 取余判断倍数
#   i % 3 == 0                     # 3 的倍数
#   i % 15 == 0                    # 同时是 3 和 5 的倍数（FizzBuzz 先判它）
#
# 打印不换行
#   print(f"{j}×{i}={i*j}", end="\t")   # end 默认 "\n"
# ═══════════════════════════════════════════════════════════════════


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