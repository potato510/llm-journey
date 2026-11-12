from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""
    note: str = ""

    def __str__(self):
        return f"姓名：{self.name}，手机号：{self.phone},电子邮箱：{self.email},备注：{self.note}"

    def __eq__(self, value):
        return self.name == value.name and self.phone == value.phone



if __name__ == "__main__":

    print("=== 练习4 ===")
    sun = Contact("孙权样","110","15334250103@163.com")
    print(sun)

    print("=== 练习5 ===")

    sun_ = Contact("孙权样","110")

    print(sun == sun_)

