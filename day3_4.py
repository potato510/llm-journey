print("=== 练习 5  ===")



def filter_lines(src,dst,keyword):
    count = 0
    try:
        with open(src, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(dst, 'w', encoding='utf-8') as f:
            for line in lines:
                if keyword in line:
                    f.write(line)
                    count += 1
    except FileNotFoundError:
        print("文件操作失败，请检查文件路径是否正确！")
    return count

count = filter_lines("sample.txt", "fox_lines.txt", "fox")
print(f"共筛选出 {count} 行包含关键词 'fox' 的内容。")