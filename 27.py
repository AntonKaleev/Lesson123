list_number = list(map(int, input().split()))

def volume():
    if len(list_number) == 3:
        a = list_number[0]
        b = list_number[1]
        c = list_number[2]
        print(a*b*c)
    else:
        a = list_number[0]
        b = list_number[1]
        print(a*b)

volume()