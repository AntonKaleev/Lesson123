list_number = list(map(int, input().split()))
i = 0

while i < abs(list_number[len(list_number)-1]):
    i += 1
    for i in range(0, list_number[len(list_number)-1]):
        a = list_number[i] - list_number[i-1]
print(a)