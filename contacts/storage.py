import json
import os


def load_contacts(path):
 try:
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8') as file:
            return json.load(file)
    else : return {}
 except FileNotFoundError:
   return {}
 except json.JSONDecodeError:
   print(f"⚠️ {path} 内容损坏，已重置为空通讯录")
   return {}

def save_contacts(contacts,path):
 if contacts is None:
    print(f"通讯录为空：{contacts}")
    return False

 if not isinstance(contacts,dict):
   raise ValueError("通讯录不是字典结构，不支持保存")

 try:
     with open(path,'w',encoding='utf-8') as file:
        json.dump(contacts,file,ensure_ascii=False,indent=4)
        return True
 except FileNotFoundError :
    raise  FileNotFoundError("改文件不存在！")

 


 
