from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0501test.txt')
numberofcolumns = 0
datamap = list()

def createmap(data):
    global numberofcolumns
    index = 0
    total = len(data)
    line = data[index]
    columns = list()
    col = list()
    count = []
    while line != '':
        pos = 0
        length = len(line)-1
        for c in line:
            if (pos == length):
                columns.append(col)
                col = list()
            if (pos%4 == 1):
                col.append(c)
            pos += 1
            if (c == '1'):
                count = line
                break
        data.pop(0)
        line = data[index]
    numberofcolumns = count[-1]
    data.pop(0)
    index = len(columns)-1
    #col = columns.pop(index)
    #print(col)
    # for line in columns:
    #     if
    return columns


datamap = createmap(data)
newmap = list()
numberofcolumns = int(numberofcolumns)
for row in datamap:
    length = len(row)
    if (length < numberofcolumns):
        for i in range(length,numberofcolumns):
            row.append(' ')
    newmap.append(row)

print(newmap)
print(data)



