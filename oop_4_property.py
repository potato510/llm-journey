import oop


print("=== 练习3 ==")

class BankAccountExpand(day5.BankAccount):


     def __init__(self,owner,balance=0):
         super().__init__(owner,balance)
         self._phone = ""

         
     @property                          # 只读属性
     def balance(self):
        return self._balance

     
     @balance.setter
     def balance(self,value):
         if value < 0:
             raise ValueError("余额不能为负数")
         self._balance = value


     @property
     def phone(self):
         return self._phone

     @phone.setter
     def phone(self,value):
         if not value.isdigit() or  len(value) != 11:
             raise ValueError("手机号不合法")
         self._phone = value


     def __str__(self):
        return super().__str__()
             



if __name__ == "__main__":
 
 expand = BankAccountExpand("王五")

 expand.balance = 999

 try:
  expand.phone = "110"
 except ValueError:
    print("预期异常，放行")

 expand.balance = 990

 expand.phone = "18501725101"

 print(expand)