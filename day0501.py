from readfromfile import readfromfile
from queue import Queue

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0501test.txt')
message = ''

qm = Queue()

def createmap(data):
    index = 0
    total = len(data)
    line = data[index]
    while line != '':
        print(line)
        data.pop(0)
        line = data[index]
    #remove empty line
    data.pop(0)

createmap(data)
print(data)

