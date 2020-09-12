'''Question 1: 
For this challenge,create a bank account class that has two attributes 
*ownerName 
*Balance 
And two methods 
*deposit 
*withdraw  
As an added requirement,withdrawals may not exceed the available balance. 
Instantiate your class,make several deposits and withdrawals,and test to make sure the account 
cant be overdrawn. '''

print("Question 1: ")
class bank_Account():
    def __init__(self, ownerName, balance):
        self.ownerName = ownerName
        self.balance = balance
        print("Name -", self.ownerName)
        print("Balance -", self.balance)

    def deposit(self): 
        amount = float(input("Enter amount to be deposited: ")) 
        self.balance += amount 
        print("Amount Deposited:", amount)

    def withdraw(self): 
        amount1 = float(input("Enter amount to be withdrawn: ")) 
        if self.balance >= amount1: 
            self.balance -= amount1 
            print("You Withdrew:", amount1) 
        else: 
            print("Insufficient balance") 

        print("Net Available Balance =", self.balance)

details = bank_Account("Sandeep", 0)
details.deposit()
details.withdraw()

'''Question 2:
For this challenge,create a cone class that has two attributes: 
*R=Radius 
*h=Height 
And two methods: 
*Volume = Π * r2 * (h/3) 
*Surface area : base : Π * r2 , side : Π * r * √(r2 + h2) 
Make only one class with functions,as in where required import Math. 
'''
print("Question 2: ")
import math as m

class cone():
    def __init__ (self,R,h):
        self.radius = R
        self.height = h

    def volume(self):
        vol = m.pi*(self.radius**2)*(self.height/3) # pi * r**2 * (h/3)
        print("Volume of the cone is: ",vol)

    def surfaceArea(self):
        base = m.pi*self.radius**2 # pi*r**2
        side = m.pi*self.radius*m.sqrt((self.radius**2)+(self.height**2)) # pi * r * sqrt(r**2 + h**2)
        print("Base of the cone is: ",base)
        print("Side of the cone is: ",side)

s = cone(5,12)
s.volume()
s.surfaceArea()
