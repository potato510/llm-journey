# 【语法卡片】函数 / 字典 / 文件读写 / JSON → 见同目录 day3.py 顶部

import json
print("=== 练习 6  ===")

# with open("scores.json", "w") as file:
#     file.write('{"志刚": 90, "文博": 80, "双龙": 70, "柏迅": 60, "元红": 50}')

def save_scores(scores, filename):
    try:
        with open(filename, "w", encoding='utf-8') as file:
            json.dump(scores, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print("文件操作失败，请检查文件路径是否正确！")

save_scores({"冰川": 87, "孟铃": 80, "刘红": 60, "柏迅": 60, "王红": 40}, "scores.json")
save_scores({"志刚": 90, "文博": 80, "双龙": 70, "柏迅": 60, "元红": 50}, "scores.json")

def load_scores(filename):
    try:
        with open(filename, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"文件操作失败，请检查文件路径是否正确！{filename}")
        return {}


j = load_scores("scores.json")
print(f"读取的成绩数据：{j}")   