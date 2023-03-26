class Account:
    def __init__(self):
        self.setBalance(10)

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

obj = Account()
obj.setBalance(30)
print(obj.getBalance())
obj.setBalance(20)
print(obj.getBalance())