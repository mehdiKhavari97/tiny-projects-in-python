
class Computer:
    def config(self):
        print("i5, 16gb, 1TB")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()
com2.config()


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def config(self):
        print("Config is: ", self.brand, self.model)

car1 = Car("Benz", 2019)
car2 = Car("BMW", 2020)

car1.config()
car2.config()


class Student:
    def __init__(self, fName = "John", lName = "Doe", age = 20):
        self.fName = fName
        self.lName = lName
        self.age = age

    def update(self, newfName = "John", newlName = "Doe", newAge = 20):
        self.fName = newfName
        self.lName = newlName
        self.age = newAge

    def compareAge(self, other):
        if self.age == other.age:
            return True
        else:
            return False


s1 = Student("Ali", "Khoob", 21)
s2 = Student("Mehran", "Rajabi", 20)

if s1.compareAge(s2):
    print("They have the same age.")
else:
    print("They don't have the same age.")