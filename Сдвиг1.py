l=int(input("Введи массив"))
d=list(range(l))
print(d)


s=int(input('Введи цивру - '))


def sdvig(d,s):
    if s>0:
        for i in range(1,s):
            f=d.pop()
            d.insert(0,f)
            print(d)

    elif s<0:
        for j in range(s,-1):
            k=d.pop(0)
            d.append(k)
            print(d)

sdvig(d,s)

