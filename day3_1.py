# 【语法卡片】函数 / 字典 / 文件读写 / JSON → 见同目录 day3.py 顶部

print("=== 练习 2 ===")

scores_a = {"志刚": 90, "文博": 80, "双龙": 70, "柏迅": 60, "元红": 50}

# def get_passed_students(scores):
#     passed_students = {}
#     for name, score in scores.items():
#         if score >= 60:
#             passed_students[name] = score
#     return passed_students

# pass_ = get_passed_students(scores)
# print("及格的学生有：")
# for name, score in pass_.items():
#     print(f"{name}：{score}分") 


# def get_failed_students(scores):
#     return {name: score for name, score in scores.items() if score < 60}

# fail_ = get_failed_students(scores)
# print("不及格的学生有：")
# for name, score in fail_.items():
#     print(f"{name}：{score}分")



for name, score in scores_a.items():
    if score >= 60:
        print(f"{name}：{score}分，及格")
    else:
        print(f"{name}：{score}分，不及格")


scores_b = {"冰川": 87, "孟铃": 80, "刘红": 60, "柏迅": 60, "王红": 40}




# scores_taobal = {**scores_a, **scores_b}


# intersection = set(scores_a.keys()) & set(scores_b.keys())
# difference_set = set(scores_a.keys()) ^ set(scores_b.keys())


scores_a_name = {name for name in scores_a.keys() }
scores_b_name = {name for name in scores_b.keys() }

scores_taobal_name = set(scores_a_name | scores_b_name)

intersection = ()
difference_set = ()

for name in scores_taobal_name:
    print(f"学生姓名：{name}")
    score_a = name in scores_a_name
    score_b = name in scores_b_name
    print(f"是否在A班中：{score_a}，是否在B班中：{score_b}")
    if score_a and score_b:
        intersection += (name,)
    elif score_a and not score_b:
        difference_set += (name,)



for name in intersection:
    print(f"{name}在A班和B班中都存在")

for name in difference_set:
    print(f"{name}只在A班中存在")

        








        

