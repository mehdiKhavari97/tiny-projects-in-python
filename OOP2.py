class A():
    def __init__(self):
        print("A init")

    def f1(self):
        print("f1-A")

    def f2(self):
        print("f2")

class B():
    def __init__(self):
        print("B init")

    def f1(self):
        print("f1-B")

    def f2(self):
        print("f2")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")


o1 = C()
o1.f1()