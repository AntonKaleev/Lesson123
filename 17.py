x = input()
a = list(x)

bukva = a[0]
chislo = int(a[1])

if bukva == "a":
    c=1
elif bukva == "b":
    c=2
elif bukva == "c":
    c=3
elif bukva == "d":
    c=4
elif bukva == "e":
    c=5
elif bukva == "f":
    c=6
elif bukva == "g":
    c=7
elif bukva == "h":
    c=8
if (c+chislo)%2 == 0:
    print("black")
else:
    print("white")