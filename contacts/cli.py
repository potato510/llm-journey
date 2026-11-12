from .service import add_contact,search_contact,delete_contact,update_contact,list_contacts
from .storage import load_contacts,save_contacts

def main():
    contacts = load_contacts("contacts.json")
    while True:
        print("\n1 添加 2删除 3修改 4 查询 5列表 0退出")
        choice = input("请输入你的选择").strip()

        if choice == '0':
            save_contacts(contacts=contacts,path="contacts.json")
            print("再见")
            break
        elif choice ==  '1':
            name = input("姓名：").strip()
            phone = input("手机号：").strip()
            email = input("电子邮箱：").strip()
            note = input("备注：").strip()
            try:
                add_contact(contacts=contacts,name=name,phone=phone,email=email,note=note)
            except ValueError as e:
                print(f"添加失败：{e}")

        elif choice == '2':
            name = input("姓名").strip()
            delete_contact(contacts=contacts,name=name)

        elif choice == '3':
            name = input("姓名：").strip()
            phone = input("手机号：").strip()
            email = input("电子邮箱：").strip()
            note = input("备注：").strip()
            try:
             update_contact(contacts=contacts,name=name,phone=phone,email=email,note=note)
            except ValueError as e:
                print(f"更改失败：{e}")

        elif choice == '4':
            keyword = input("姓名/手机号/电子邮箱/备注：").strip()
            result = search_contact(contacts=contacts,keyword=keyword)
            for name,info in result.items() :
                 print(f"{name}:{info['phone']}  {info['email']}  {info['note']}")
            print(f"共{len(result)} 条")   

        elif choice == '5':
            count = list_contacts(contacts=contacts)
            print(f"通讯录总共{count}位联系人")
        else:
            print("请输入0-5的数字")

