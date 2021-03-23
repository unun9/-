
class Fraction:
    def __init__(self, n1, n2):
        if n2 == 0:
            raise ValueError("osdff --0")
        self.n1 = n1
        self.n2 = n2

    def add(self, other):
        num_1 = self.n1 * other.n2 + self.n2 * other.n1
        num_2 = self.n2 * other.n2
        return num_1, num_2

    def sub(self, other):
        min1 = self.n1 - other.n1
        min2 = self.n2 - other.n2
        return min1, min2

    def mul(self, other):
        um1 = self.n1 * other.n1
        um2 = self.n2 * other.n2
        return um1, um2

    def truediv(self, other):
        del1 = self.n1 / other.n1
        del2 = self.n2 / other.n2
        return del1, del2


fraction1 = Fraction(5, 4)
fraction2 = Fraction(2, 1)
print(fraction1.mul(fraction2))
