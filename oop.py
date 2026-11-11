print("===   练习1  ===")

class BankAccount:
    bank_name = "招商银行"
    count = 0

    def __init__(self,owner,balance=0):
        self.owner = owner
        self._balance = balance
        BankAccount.count += 1

    def deposit(self,amount):
        self._balance += amount

    def __str__(self):
        return f"{self.owner} 的账户，余额 ¥{self._balance:.2f}"

    def show(self):
        print(self)    # 复用 __str__，格式只维护一处


    def withdraw(self,amount):
        if self._balance < amount:
            raise ValueError("余额不足")
        self._balance -= amount


if __name__ == "__main__":
    a = BankAccount("张三")
    a.bank_name = "工商银行"
    a.deposit(100); a.withdraw(30)
    print(a)                     # 张三 的账户，余额 ¥70.00
    try: a.withdraw(1000)
    except ValueError as e: print("预期内异常:", e)

    b = BankAccount("李四")
    print(f"a 的 bank_name：{a.bank_name} ,b 的 bank_name：{b.bank_name} BankAccount count值：{BankAccount.count}")

    
      