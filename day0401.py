from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0401.txt')
total = 0

set1 = {3}
set2 = {4,5,6}

for line in data:
    set1 = set()
    set2 = set()
    line = line.split(',')
    set1line1 = line[0].split('-')
    set1b = int(set1line1[0])
    set1e = int(set1line1[1])+1
    for i in range(set1b,set1e):
        set1.add(i)
    set2line2 = line[1].split('-')
    set2b= int(set2line2[0])
    set2e = int(set2line2[1])+1
    for i in range(set2b,set2e):
        set2.add(i)
    if set1.issubset(set2) or set2.issubset(set1):
        total += 1

print(total)
