# Encapsulation Wrapping data & functions into single unit. 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance 

    def get_balance(self): # getter 
        return self.__balance
    
    def set_balance(self, newBalance): # setter 
        self.__balance = newBalance

acc1 = BankAccount("Akhilesh", 100_000_0000_000_00)
acc1.set_balance(20_000)

# print(acc1.name, acc1.get_balance())
print(acc1.name, acc1._BankAccount__balance)
