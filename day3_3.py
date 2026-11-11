# 【语法卡片】函数 / 字典 / 文件读写 / JSON → 见同目录 day3.py 顶部

print("=== 练习 4  ===")

with open("sample.txt","w",encoding="utf-8") as f:
    f.write("The quick brown fox jumps over the lazy dog. The dog barks and the fox runs. A quick fox is a happy fox. The lazy dog sleeps." )

with open("sample.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(f"读取的内容：{content}")


# content = content.replace(".,!?;:\"'", " ").lower().split(" ")
content_list = content.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(";", "").replace(":", "").replace("\"", "").replace("\'", "").lower().split(" ")
print(f"单词列表：{content_list}") 

top_dict = {}

for word in content_list:
    if word in top_dict:
        top_dict[word] += 1
    else:
        top_dict[word] = 1


top_list = sorted(top_dict.items(), key=lambda x: x[1], reverse=True)[:10]
print(f"单词出现次数统计：{top_list}")
    

    


