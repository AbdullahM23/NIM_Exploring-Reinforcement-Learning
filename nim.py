import random
Moves = {
'3,2,2': [3,3,3,3,3,3,3],
'3,2,1': [3,3,3,3,3,3,0],
'3,2,0': [3,3,3,3,3,0,0],
'3,1,2': [3,3,3,3,0,3,3],
'3,1,1': [3,3,3,3,0,3,0],
'3,1,0': [3,3,3,3,0,0,0],
'3,0,2': [3,3,3,0,0,3,3],
'3,0,1': [3,3,3,0,0,3,0],
'3,0,0': [3,3,3,0,0,0,0],
'2,2,2': [3,3,0,3,3,3,3],
'2,2,1': [3,3,0,3,3,3,0],
'2,2,0': [3,3,0,3,3,0,0],
'2,1,2': [3,3,0,3,0,3,3],
'2,1,1': [3,3,0,3,0,3,0],
'2,1,0': [3,3,0,3,0,0,0],
'2,0,2': [3,3,0,0,0,3,3],
'2,0,1': [3,3,0,0,0,3,0],
'2,0,0': [3,3,0,0,0,0,0],
'1,2,2': [3,0,0,3,3,3,3],
'1,2,1': [3,0,0,3,3,3,0],
'1,2,0': [3,0,0,3,3,0,0],
'1,1,2': [3,0,0,3,0,3,3],
'1,1,1': [3,0,0,3,0,3,0],
'1,1,0': [3,0,0,3,0,0,0],
'1,0,2': [3,0,0,0,0,3,3],
'1,0,1': [3,0,0,0,0,3,0],
'1,0,0': [3,0,0,0,0,0,0],
'0,2,2': [0,0,0,3,3,3,3],
'0,2,1': [0,0,0,3,3,3,0],
'0,2,0': [0,0,0,3,3,0,0],
'0,1,2': [0,0,0,3,0,3,3],
'0,1,1': [0,0,0,3,0,3,0],
'0,1,0': [0,0,0,3,0,0,0],
'0,0,2': [0,0,0,0,0,3,3],
'0,0,1': [0,0,0,0,0,3,0]
}

def PickRandomPlay(state):
    total = 0
    for i in Moves[state]:
        total += i
    if total == 0: #if no available choices to play, it surrenders by returninig -1
        return -1
    r = random.randint(1, total)
    total = 0
    for i in range(len(Moves[state])):
        total += Moves[state][i]
        if total >= r:
            return i+1

def MakePlay(num):
    if num == 1 and playGround[0] >= 1:
        playGround[0] -= 1
        return True
    elif num == 2 and playGround[0] >= 2:
        playGround[0] -= 2
        return True
    elif num == 3 and playGround[0] >= 3:
        playGround[0] -= 3
        return True
    elif num == 4 and playGround[1] >= 1:
        playGround[1] -= 1
        return True
    elif num == 5 and playGround[1] >= 2:
        playGround[1] -= 2
        return True
    elif num == 6 and playGround[2] >= 1:
        playGround[2] -= 1
        return True
    elif num == 7 and playGround[2] >= 2:
        playGround[2] -= 2
        return True
    return False

def Learn(record,result): #result is a bool: True=won and False=lost
    moves = record.split('/')
    if result:
        for i in range(len(moves)-1):
            Moves[moves[i].split(':')[0]][int(moves[i].split(':')[1])-1] += 2
    else:
        for i in range(len(moves)-1):
            Moves[moves[i].split(':')[0]][int(moves[i].split(':')[1])-1] -= 1

def LoadMoves(filename):
    if filename == '':
        filename = 'mem.txt'
    if '.txt' not in filename:
        filename += '.txt'
    file = open(filename,'r')
    for line in file:
        if line == '':
            break
        index = line.split(':')[0]
        data = line.split(':')[1].replace('[','').replace(']','').split(',')
        for i in range(len(Moves[index])):
            Moves[index][i] = int(data[i])
    file.close()

def SaveMoves(filename):
    file = open(filename,'w')
    for i in Moves:
        file.write(i+':'+str(Moves[i])+'\n')
    file.close()

print('Do you want to load a move set?(Input Y for yes or anything else for no)',end=' ')
if input() == 'Y':
    LoadMoves(input('Enter the name of the file to load from(if nothing is input it will default to mem.txt): '))
playGround = [3,2,2]
playsMade = ''
#print(Moves)
#print('\n\n\n\n\n')
playing = True
while playing:
    n = int(PickRandomPlay(str(playGround[0])+','+str(playGround[1])+','+str(playGround[2])))
    if n == -1: #this means that it had no choices to choose from aka it lost
        Learn(playsMade,False)
        print('Player won, :(')
        playGround = [3,2,2]
        playsMade = ''
        continue
    playsMade = playsMade + str(playGround[0])+','+str(playGround[1])+','+str(playGround[2]) + ':' + str(n) + '/'
    MakePlay(n)
    if playGround == [0,0,0]:
        Learn(playsMade,False)
        print('Player won, :(')
        playGround = [3,2,2]
        playsMade = ''
        continue
    validInput = False
    while not validInput:
        print(playGround)
        Input = int(input('Play: '))
        if Input == -1:
            playing = False
            break
        validInput = MakePlay(Input)
        if(not validInput):
            print('Invalid input')
            print('---------')
    print(playGround)
    print('---------')
    if playGround == [0,0,0]:
        Learn(playsMade,True)
        print('I won, ;P')
        playGround = [3,2,2]
        playsMade = ''
        continue
if(input("Enter Y to save the current move set: ") == "Y"):
    print('Saving new move set...')
    SaveMoves('mem.txt')
#print(Moves)
#print('\n\n\n\n\n')
input('Done!')