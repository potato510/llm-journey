

# 增加联系人
def add_contact(contacts,name,phone,email,note):
    if contacts is None:
        print(f"通讯录为空，默认创建一个空通讯录")
        contacts = {}

    # 姓名正则校验
    if not name :
        raise ValueError("姓名不能为空")

    # 手机号正则校验
    if not phone.isdigit() or len(phone) != 11:
        raise ValueError("手机号需要是11位的数字")

    if name in contacts:
        print(f"通讯录中已经存在该姓名：{name}")
        return False
    else:
        contacts[name] = {'phone':phone,'email':email,'note':note}
        return True
# 删除联系人
def delete_contact(contacts,name):
    if contacts is None:
        print("通讯录为空，不能操作")
        return False
    
    names = list(contacts.keys());

    if name in names:
        del contacts[name]
        return True
    else:
        print(f"联系人 {name} 不存在，无法删除。")
        return False

# 查找联系人
def search_contact(contacts,keyword):
    if contacts is None:
        print("通讯录为空，不能操作")
        return {}
    
    if not isinstance(contacts,dict) :
        print(f"联系人列表为非字典结构，不可查询{contacts}")
        return {}   

    word = keyword.strip();

    return {name:info for name,info in contacts.items() if word in name or word in info['phone'] or word in info['email'] or word in info['note'] }

# 更改联系人信息
def update_contact(contacts,name,email,phone,note):
    if contacts is None:
        print("通讯录为空，不能操作")
        return False

    names = list(contacts.keys())
    if name in names:
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError("手机号格式不正确")
        if name is None:
            raise ValueError("联系人姓名不能为空")
        contacts[name]['phone'] = phone or contacts[name]['phone']
        contacts[name]['email'] = email or contacts[name]['email']
        contacts[name]['note'] = note or contacts[name]['note']
        return True
    else:
        print(f"该姓名不再通讯录中{name}，默认添加")
        return add_contact(contacts,name,phone,email,note)


# 遍历联系人列表
def list_contacts(contacts):
    if contacts is None:
        print("联系人列表为空")
        return 0

    panel = sorted(contacts.items(),key = lambda x : x[0])

    for name,info in panel:
        print(f"联系人：{name},手机号：{info['phone']},电子邮箱：{info['email']},备注：{info['note']}")
    return len(panel)
