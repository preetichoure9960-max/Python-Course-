class bankaccount:
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance
    def deposite(self):
        self.deposite=36000
        print("the money has deposited")
    def withdraw(self):
        self.withdraw=6000
        print("the money has withdrawal")
    def bankdetails(self):
        print(f"accountnumber:{self.accountnumber}")
        print(f"balance:{self.balance}")
bank1=bankaccount(250486709845,1000)
bank2=bankaccount(23456784, 2000)

bank1.bankdetails()
bank1.deposite()
bank1.withdraw()
bank2.bankdetails()
bank2.deposite()
bank2.withdraw()



class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year 
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
    def Cardetails(self, number):
        self.Cardetails = number
        print("the car number ")
    def describe_car(self):
        print(f"This car is a {self.year} {self.brand} {self.model} with {self.mileage} miles.")
Car1=Car(2007,"toyota", "hyundai")
Car1.Cardetails(Car)
Car1.drive(300)
Car1.describe_car()