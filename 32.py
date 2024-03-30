my_file = open("freqs.txt", "r")

data = my_file.read().split(";")

treshold = 11

number = []

for i in range(len(data)):
    number.append(data[i])

for i in number:
    if float(i) < treshold:
        print(i)



