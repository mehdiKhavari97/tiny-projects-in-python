class PyCharm():
    def execute(self):
        print("Compile")
        print("Run")

class MyEditor():
    def execute(self):
        print("Spell check")
        print("Compile")
        print("Run")
        print("Debug")

class Laptop():
    def code(self, ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)