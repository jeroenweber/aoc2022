from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0301.txt')
total = 0

next3sacks = True
numberofsacks = len(data)
sackcount = 0

while sackcount < numberofsacks:
    c = set(data[sackcount]) & set(data[sackcount+1]) & set(data[sackcount+2])
    sackcount += 3
    c = ord(list(c)[0])
    if (c >= 97):
        c -= 96
    else:
        c -= 38
    total += c

print(total)