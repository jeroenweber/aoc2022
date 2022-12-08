from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0101.txt')
top3 = [0,0,0]

def ranking(val):
    if (val > top3[0]):
        top3[2] = top3[1]
        top3[1] = top3[0]
        top3[0] = val
    elif (val > top3[1]):
        top3[2] = top3[1]
        top3[1] = val
    elif (val > top3[2]):
        top3[2] = val

max = 0
sum = 0
for cal in data:
    if cal == '':
        ranking(sum)
        sum = 0
    else:
        sum += eval(cal)

print(top3[0]+top3[1]+top3[2])

