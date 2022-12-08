from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0101.txt')
top3 = [0,0,0]
max = 0
sum = 0
for cal in data:
    if cal == '':
        if sum > max:
            max = sum
        sum = 0
    else:
        sum += eval(cal)

print(max)
