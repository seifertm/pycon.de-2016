class Complex():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, number):
        return Complex(self.real + number.real, self.imaginary + number.imaginary)
    
    def __sub__(self, number):
        return Complex(self.real - number.real, self.imaginary - number.imaginary)

    def __mul__(self, number):
        return Complex(self.real * number.real - self.imaginary * number.imaginary,
                       self.real * number.imaginary + self.imaginary * number.real)

    def conjugate(self):
        return Complex(self.real, -self.imaginary)
