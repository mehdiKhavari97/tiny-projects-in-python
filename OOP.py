
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
    level = "University" #This is a class variable, if you change it, it will be changed for all the objects
    def __init__(self, fName = "John", lName = "Doe", age = 20):
        #This are instance variables
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


# making a class inside a class is possible

class Employee:
    def __init__(self, name = "John", age = 20, salary = 20000):
        self.name = name
        self.age = age
        self.salary = salary
        self.lpt = self.Laptop()

    def show(self):
        print(self.name, self.age, self.salary)
        self.lpt.show()



    class Laptop:
        def __init__(self, brand = "ASUS", cpu = "i5", ram = 16):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)


e1 = Employee("Mehdi", 24, 12000)
e1.show()