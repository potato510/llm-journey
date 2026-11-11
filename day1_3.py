# 【语法卡片】变量 / 数字 / 字符串 / 列表 / 元组 → 见同目录 day1.py 顶部

cart = "apple", "banana", "orange","watermelon";

cart = list(cart);
cart.append("grape");
cart.insert(0, "pear");
cart.remove("banana");

print(f"购物车中的水果有：{cart}");
print(f"购物车中的水果数量为：{len(cart)}");
print(f"购物车中的第一个水果是：{cart[0]}");
print(f"购物车中的最后一个水果是：{cart[-1]}");
