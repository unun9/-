k1 = 'k1'
k2 = 'k2'
k3 = 'k3'
k4 = 'k4'
k5 = 'k5'
k6 = 'k6'
k7 = 'k7'
k8 = 'k8'
k9 = 'k9'
k10 = '|'
k11 = "X "
k12 = "O "

sa = "---|----|---"
print(sa)
print(k1, k10, k2, k10, k3)
print(sa)
print(k4, k10, k5, k10, k6)
print(sa)
print(k7, k10, k8, k10, k9)
print(sa)
spisok1 = {k1, k2, k3}
spisok2 = {k1, k5, k9}
spisok3 = {k1, k4, k7}
spisok4 = {k2, k5, k8}
spisok5 = {k3, k5, k7}
spisok6 = {k3, k6, k9}
spisok7 = {k4, k5, k6}
spisok8 = {k7, k8, k9}
prin = {sa, "\n", k1, k10, k2, k10, k3, "\n", sa, "\n", k1, k10, k2, k10, k3, "\n", sa, "\n", k7, k10, k8, k10, k9,
        "\n", sa}
while spisok1 != k11 or k12 or spisok2 != k11 or k12:
    nol = input("Куда поставить - O")
    if nol == k1:
        k12, k1 = k1, k12
        sa = "---|----|---"
        print(sa)
        print(k1, k10, k2, k10, k3)
        print(sa)
        print(k1, k10, k2, k10, k3)
        print(sa)
        print(k7, k10, k8, k10, k9)
        print(sa)

    elif nol == k2:
        print()
