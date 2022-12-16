from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0501.txt')
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
    newmap = list()
    numberofcolumns = int(numberofcolumns)
    for row in columns:
        length = len(row)
        if (length < numberofcolumns):
            for i in range(length, numberofcolumns):
                row.append(' ')
        newmap.append(row)
    finalmap = list()
    for i in range(len(newmap)):
        columns = list()
        for item in newmap[::-1]:
            if (item[i] != ' '):
                columns.append(item[i])
        finalmap.append(columns)
    return finalmap


datamap = createmap(data)
datamap.append(['D', 'S', 'C', 'N', 'L', 'P', 'H'])
print(datamap)
print(data)

for command in data:
    actions = command.split(' ')
    count = int(actions[1])
    columnfrom = int(actions[3])-1
    columnto = int(actions[5])-1
    print(f"moving {count} from column {columnfrom} to column {columnto}" )
    length = len(datamap)
    for move in range(count):
        cfrom = datamap[columnfrom]
        cto = datamap[columnto]
        if (len(cfrom) > 0):
            cto.append(cfrom[-1])
            cfrom.pop(-1)
        datamap[columnfrom] = cfrom
        datamap[columnto] = cto
    message = list()
    for column in datamap:
        if (len(column) > 0):
            message.append(column[-1])

print("".join(message))



