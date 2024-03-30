def my_filter():
    list_number = list(map(int, input().split()))
    a = []
    for item in list_number:
        a.append(item*10)
    print(a)
my_filter()