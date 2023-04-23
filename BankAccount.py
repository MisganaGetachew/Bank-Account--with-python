# classes excercise
class BankAccount:
    def __init__(self):
        self.Balance = 0
        self.transaction = {}
        # self.interestRate = interestRate
        self.tranCount = 0

    def deposit(self, amount):
        # self.amount = amount  # not important
        self.Balance += amount
        self.tranCount += 1
        self.transaction[f' transaction {self.tranCount} diposited ETB'] = amount
        return self.Balance

    def widthdraw(self, amount):
        # self.amount1 = amount  # not important
        self.Balance -= amount
        self.tranCount += 1
        self.transaction[f' transaction {self.tranCount} Withdrew ETB'] = amount
        return self.Balance

    def checkBalance(self):
        return self.Balance

    def transactions(self):
        return self.transaction


def register():
    accNumber = input("""
                    please Insert your Name: """)
    return accNumber


def choices():
    choice = int(input("""
                        what would you like TO DO?
                    1: To be registered    2: To deposit    
                    3: To withdraw         4: To see Transaction History
                    5: Check Balance       6: exit
                                :- """))
    return choice


def amount():
    amount = float(input("""
                    please insert Amount: """))
    return amount


print(""" 
            ------  WELCOME TO CBE - THE MOST TRUSTED BANK WORLD WIDE -------
                             
""")

while True:
    choiceMade = choices()
    if choiceMade == 1:
        accNum = register()
        accNum = BankAccount()
    elif choiceMade == 2:
        dipAmount = amount()
        accNum.deposit(dipAmount)
    elif choiceMade == 3:
        withdAmount = amount()
        accNum.widthdraw(withdAmount)
    elif choiceMade == 4:
        num = dict(accNum.transactions())
        for key, item in num.items():
            print(key, item)
    elif choiceMade == 5:
        # val = accNum.checkBalance()
        print(accNum.checkBalance())
    elif choiceMade == 6:
        break
