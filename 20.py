x = float(input())
n=-1
a=0.000001
rezult=1
summa=0
while abs(rezult)>a:
    n += 1
    rezult = (((-1) ** (n)) * x ** (n+1) )/ (n+1)
    summa += rezult
print(round(summa,8))