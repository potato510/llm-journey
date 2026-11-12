import oop

print("=== 练习2 ===")

class SavingAccount(day5.BankAccount):

    def __init__(self, owner, balance=0 , interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"{super().__str__()}(利率 {self.interest_rate})"

    def add_interest(self):
        self._balance =  self._balance * (1 + self.interest_rate)






if __name__ == "__main__":
    save = SavingAccount("李四",0.03,1000)
    save.add_interest()

    print(save)


