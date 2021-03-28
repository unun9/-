# #Омурзаков Кудайберди
# class complex:
#     def __init__(self, n1,n2,):
#         self.n1 = n1
#         self.n2 = n2
#
#     def __str__(self):
#         return(self.n1)+(self.n2)
#
#     def __add__(self, other):
#         summ = self.n1 + other.n2
#         summ2 = self.n2 + other.n1
#         result = f"z1={other.n1} z={other.n2} {complex(summ//summ2)}"
#         return result
#
#     def __add__(self, otherminus):
#         minus1 = self.n1 - otherminus.n2
#         minus2 = self.n2 - otherminus.n1
#
#         return complex(minus1//minus2)
#
#
#     def multiply(self, othermultiply):
#         multi1 = self.n1 * othermultiply.n2
#         multi2 = othermultiply.n1 * self.n2
#         multiresult = complex(multi1//multi2)
#
#         return multiresult
#
#
#
#
#
# x = complex(3, 7)
# y = complex(1, 3)
# plus1 = (x.n1 + x.n2)
# plus2 = (y.n1 + y.n2)
# minus1 = (x.n1 - x.n2)
# minus2 = (y.n1 - y.n2)
# multi1 = (x.n1 * x.n2)
# multi2 = (y.n1 * y.n2)
#
# print(plus1, plus2)
# print(minus1, minus2)
# print(multi1, multi2)

from random import randint



a =[]
for i in range(10):
    a.append(randint(1, 100))

a.sort()
print(a)

value = int(input())

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID=", mid)