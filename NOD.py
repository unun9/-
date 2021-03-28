# Омурзаков Кудайберди
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, chisl, znam):
        self.chisl = chisl
        self.znam = znam

    def __str__(self):
        return str(self.chisl) + "/" + str(self.znam)

    def __add__(self, otherfraction):

        newchisl = self.chisl * otherfraction.znam + self.znam * otherfraction.chisl
        newznam = self.znam * otherfraction.znam
        common = gcd(newchisl, newznam)

        return Fraction(newchisl // common, newznam // common)

    def __add__(self, otherfraction):

        newchisl = self.chisl * otherfraction.znam - self.znam * otherfraction.chisl
        newznam = self.znam * otherfraction.znam
        common = gcd(newchisl, newznam)

        return Fraction(newchisl // common, newznam // common)

    def multiply_fractions(self, othermultiply):
        newchisl2 = self.chisl * othermultiply.znam
        newznam2 = othermultiply.chisl * self.znam
        common = gcd(newchisl2, newznam2)

        return Fraction(newchisl2 // common, newznam2 // common)


    def __eq__(self, other):
        firstnum = self.chisl * other.znam
        secondnum = other.chisl * self.znam

        return firstnum == secondnum




x = Fraction(1, 2)
y = Fraction(1, 4)
print(x + y)
print(x == y)
a = Fraction(1, 2)
b = Fraction(1, 4)
print(a.multiply_fractions(b))