class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator must not be zero.')
        self.numerator = numerator
        self.denominator = denominator
    
    @property
    def proper(self):
        return abs(self.numerator) < abs(self.denominator)

    @staticmethod
    def _greatest_common_divisor(a, b):
        while b != 0:
            h = a % b
            a = b
            b = h
        return a

    def reduce(self):
        gcd = Fraction._greatest_common_divisor(abs(self.numerator), abs(self.denominator))
        return Fraction(self.numerator/gcd, self.denominator/gcd)
