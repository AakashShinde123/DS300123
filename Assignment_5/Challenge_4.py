class Account:

    def __init__(self,name = None,balance = 0):
        self.name = name
        self.balance = balance

        
    
class SavingsAccount(Account):

    def __init__(self,name,balance,intresrate):
        # write your code here
        super().__init__(name,balance)
        self.intrestrate = intresrate

    
a2 = SavingsAccount("Ashish",5000,5)
print(a2.name)
print(a2.balance)
print(a2.intrestrate)  
