#Every time you use an operator like + or -, a built-in class will be called.

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        return self.m1 + self.m2 + other.m1 + other.m2

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = student(15, 18)
s2 = student(10, 20)

print("s1 + s2 = ", s1 + s2)

print(s1)