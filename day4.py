import json
import os
print("=== 练习 1 ===")

contacts1 = {
    "张三": {"phone": "13800138000", "email": "zhang@x.com", "note": ""},
    "李四": {"phone": "13900139000", "email": "", "note": "同事"},
}


def load_contacts(path="contacts.json"):
    try:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {}

    except (FileNotFoundError,json.JSONDecodeError):
        return {}        

def save_contacts(contacts, path="contacts.json"):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(contacts, f, ensure_ascii=False, indent=4)
            return True
    except (FileNotFoundError):
        print("文件操作失败，请检查文件路径是否正确！")
        return False

def add_contact(contacts,name, phone, email = "", note = ""):
    if contacts is None:
        print("联系人列表为空，无法添加联系人。")
        return False

    if not phone.isdigit() or len(phone) != 11:
       raise ValueError("手机号格式不正确，应该是11位数字")

    
    if name in contacts:
        print(f"联系人 {name} 已存在，无法添加。")
        return False
    else:
        contacts[name] = {"phone": phone, "email": email, "note": note}
        return True

def delete_contact(contacts, name):
    if contacts is None:
        print("联系人列表为空，无法删除联系人。")
        return False
    if name in contacts:
        del contacts[name]
        return True
    else:
        print(f"联系人 {name} 不存在，无法删除。")
        return False


def search_contacts(contacts,keyword):

    result = {}
    if contacts is None:
        print("联系人列表为空，无法查找联系人。")
        return result

    if type(contacts) is not dict:
        print(f"联系人列表为非字典结构，不可查询{contacts}")
        return result

    return { name:data for name,data in contacts.items() if keyword in name or keyword in data['phone'] or keyword in data['email'] or keyword in data['note']}


def list_contacts(contacts):
    if not contacts:
        print("空集合不需要列出来")
        return 0
        
    panel = sorted(contacts.items(),key=lambda x: x[0]);

    for key,value in panel:
        
        print(f"联系人{key},手机号{value['phone']},邮箱{value['email']},备注{value['note']}")

    return len(panel)






c = load_contacts("contacts.json")

add_contact(c,"张三","13800138000")

add_contact(c,"李四","13900139000","li@x.com")

add_contact(c,"张三","13700137000")

try:

    add_contact(c, "王五", "abc")
except ValueError as e: 
    print(f"预期内异常：{e}")  

save_contacts(c)

c2 = load_contacts()

print(f"c2 数据详情{c2}")

count = list_contacts(c2)

print(f"联系人记录共有{count}条")

print(search_contacts(c2,"张"))

print(search_contacts(c2,"赵六"))