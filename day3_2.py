# 【语法卡片】函数 / 字典 / 文件读写 / JSON → 见同目录 day3.py 顶部

print("=== 练习 3  ===")

scores = {"志刚": 90, "文博": 80, "双龙": 70, "柏迅": 60, "元红": 50}

def statistics(scores):
    if not scores:
        return None  # 如果字典为空，返回None,None 不代表任何意义，可以作为空参的兜底策略
    total_score = sum(scores.values()) 
    average_score = total_score / len(scores) # 平均分
    max_score = max(scores.values()) # 最高分
    min_score = min(scores.values()) # 最低分

    scores_list = sorted(scores.items(),key=lambda x: x[1], reverse=True)  # 按分数从高到低排序
    top_student = scores_list[0][0]  # 获取最高分学生姓名

   # 统计及格率
    passed = {name:score for name, score in scores_list if score >= 60}
    pass_rate = len(passed) / len(scores) if scores else 0

   # 统计及格人数
    pass_count = len(passed)

    return  {"average_score": average_score, "max_score": max_score, "min_score": min_score, "pass_rate": pass_rate, "pass_count": pass_count, "top_student": top_student}



result = statistics(scores)
print(f"该班级的平均分是：{result['average_score']}，最高分是：{result['max_score']}，最低分是：{result['min_score']}，及格率是：{result['pass_rate'] * 100:.2f}%，及格人数是：{result['pass_count']}人，最高分学生是：{result['top_student']}")
