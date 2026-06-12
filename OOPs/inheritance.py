class Person:
    def __init__(self, name , age):
        self.name=name
        self.age=age
        
    def displaydetailsofperson(self):
         print("Name:", self.name)
         print("Age:", self.age)
class CEO(Person):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age)
        self.employee_id=employee_id
        self.salary=salary
        self.department=department
        
    def displayCEO(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
        print("Department:", self.department)
class Manager(CEO):
    def __init__(self,name, age, employee_id, salary, department,remark):
        super().__init__(name, age, employee_id, salary, department)
        self.remark = remark
        
    def displayManager(self):
        print("Remark:", self.remark)
        
    def give_bonus(self, bonus):
        self.salary += bonus
        print("Bonus added! New Salary:", self.salary)    
        
m1 = Manager("Preeti", 30, 101, 50000, "IT", "Excellent")
m1.displaydetailsofperson()
m1.displayCEO()
m1.displayManager()
m1.give_bonus(5000)



class Electriccar:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def displaycar(self):
         print("Name:", self.name)
         print("Model:", self.model)
class Car(Electriccar):
    def __init__(self, name, model, year, battery_capacity):
        self.year= year
        self.battery_capacity=battery_capacity
        self.charge_level = 0
        
    def displaycar(self):
        print("Year:",self.year)
        print("battery capacity:", self.battery_capacity)
        
    def charge(self):
        self.charge_level = 100

    def describe_battery(self):
        print(f"This car has a {self.battery_capacity} kWh battery with {self.charge_level}% charge.")


electric_car = Car('Tesla', 'Model 3', 2020, 75)
electric_car.displaycar()
electric_car.describe_battery()
electric_car.charge()
electric_car.describe_battery()