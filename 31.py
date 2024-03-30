filename = "1.txt"
data=[(1, 20),(2, 30),(3, 40),(4, 35),(5, 22),(6, 10)]
data1 = map(str, data)
def write(filename, data1):

    f = open(filename, 'w')
    string = ''
    for i in data:
        string += str(i)
        string += ''
    f.write(string)
    f.close()

write(filename, data)
