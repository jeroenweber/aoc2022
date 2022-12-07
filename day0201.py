#Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# If both players choose the same shape, the round instead ends in a draw.

#A=rock, B=paper, C= scissors
#X=rock, Y=paper, Z=scissors

draw = 3
win = 6
lose = 0
bets = {'A': 1, 'B' : 2, 'C': 3, 'X' : 1, 'Y' : 2, 'Z' : 3}

from readfromfile import readfromfile

data = readfromfile('C:/Users/jeroen.weber/PycharmProjects/aoc2022g/day0201.txt')

def checkgame(playlist):
    points = 0
    base0 = bets[playlist[0]]
    base1 = bets[playlist[1]]
    if (playlist == ['A','Z']) or (playlist == ['B','X']) or (playlist == ['C','Y']):
        playlist[0] = 6
        playlist[1] = 0
    elif (playlist == ['A','Y']) or (playlist == ['B','Z']) or (playlist == ['C','X']):
        playlist[0] = 0
        playlist[1] = 6
    elif (playlist == ['A','X']) or (playlist == ['B','Y']) or (playlist == ['C','Z']):
        playlist[0] = playlist[1] = 3
    else:
        playlist[0] = playlist[1] = 0
    playlist[0] += base0
    playlist[1] += base1
    return playlist

total = 0
for line in data:
    total += checkgame(line.split())[1]

print(total)