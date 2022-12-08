from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0301.txt')
total = 0

for line in data:
    halflength = len(line)//2
    c1 = line[0:halflength]
    c2 = line[halflength:]
    common = set(c1)&set(c2)
    c = ord(list(common)[0])
    if (c >= 97):
        c -= 96
    else:
        c -=38
    total += c

print(total)