class Complex_number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'({self.a},{self.b})'

    def __add__(self, other):
        return f'({self.a + other.a},{self.b + other.b})'

    def __mul__(self, other):
        return f'({self.a * other.a - self.b * other.b},{self.a * other.a + self.b * other.b})'


num1 = Complex_number(2, 3)
num2 = Complex_number(2, 5)
num1 + num2

print(num1 + num2)
print(num1 * num2)
