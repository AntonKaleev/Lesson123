room = int(input())
if room in (1,9,17,25):
    print(1, end=",")
if room in (2,10,18,26):
    print(2, end=",")
if room in (3,11,19,27):
    print(3, end=",")
if room in (4,12,20,28):
    print(4, end=",")
if room in (5,13,21,29):
    print(5, end=",")
if room in (6,14,22,30):
    print(6, end=",")
if room in (7,15,23,31):
    print(7, end=",")
if room in (8,16,24,32):
    print(8, end=",")

if 1<=room<=8:
    print(1)
if 9<=room<=16:
    print(2)
if 17<=room<=24:
    print(3)
if 25<=room<=32:
    print(4)
