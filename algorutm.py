# 0 tuhjad alad
# 1 alad kuhu saab liikuda
# 2 alustamisruut
# 3 lopetamisruut
# ules alla votab 2 blokki ruumi
# korvale votab 1/2 vaheldumisi ruumi

board = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 3, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
]

isStanding = True
solution = []
currentCoordinates

lastRotation = ''

def solveTheLevel():
    # vaatab kuhu saab liikuda, liigub
    # kirj massiivi enda liikumise kohta
    # ss kutsub uuesti sama solvethelevel
    # edasi tagasi seni kuni jouab lahenduseni
    # kui ei saa liikuda - liigub tagasi sammu vorra ja proovib jargmise voimaliku kaigu
    

    # kutsu uuesti solvethelebel

def fallDown(x, y):    
    ##tšekk kui järgmine x,y == 0



def getStartingCoordinates():
    # saab alustamiskoordinaadid
    for x in board:
        for y in board:
            if board[x][y] == 2:
                return board[x][y]


def canMoveUp(x, y):
    # liigub ules
    if isStanding:
        if board[x-1][y] == 1 and board[x-2][y] == 1:
            board[x][y] = board[x-1][y]
            return True
    else:
        if board[x-1][y] == 1 and board[x-1][y+1] == 1:   
            board[x][y] == board[x-1][y]
                          

def canMoveDown(x, y):
    # liigub alla
    if isStanding:
        if board[x+1][y] == 1 and board[x+2][y] == 1:
            board[x][y] = board[x+1][y]
            return True
    else:
        if board[x+1][y] == 1 and board[x+1][y-1] == 1:   
            board[x][y] == board[x+1][y]

def canMoveLeft(x, y):
    # liigub alla
    if isStanding:
        if board[x][y-1] == 1 and board[x][y-2] == 1:
            board[x][y] = board[x][y-1]
            return True
    else:
        if board[x][y-1] == 1 and board[x+1][y-1] == 1:   
            board[x][y] = board[x][y-1]

def canMoveRight(x, y):
    if isStanding:
        if board[x][y+1] == 1 and board[x][y+2] == 1:
            board[x][y] = board[x][y-1]
            return True
    else:
        if board[x][y+1] == 1 and board[x-1][y+1] == 1:   
            board[x][y] = board[x][y+1]

def move(x, y, rotation, lastRotation):
    doubleX = if x+2 == 1 | x -2 == 1
    doubleY = if y+2 == 1 | x - 2 == 1
    if not isStanding & doubleX:
        y +1
        y-1

    if not isStanding & doubleY:
        y + 1
        y - 1

    if rotation == 'LEFT':
        if isStanding:
            board[x][y] = board[x-1][y]
            isStanding = False
        else:
            board[x][y] = board[x-2][y]
            isStanding = True

    if rotation == 'RIGHT':
        if isStanding:
            board[x][y] = board[x+1][y]
            isStanding = False
        else:
            board[x][y] = board[x+2][y]
            isStanding = True

    if rotation == 'UP':
        if isStanding:
            board[x][y] = board[x][y+1]
            isStanding = False
        else:
            board[x][y] = board[x][y+2] 
            isStanding = True
    if rotation == 'DOWN':
        if isStanding:
            board[x][y] = board[x][y-1]
            isStanding = False
        else:
            board[x][y] = board[x][y-2] 
            isStanding = True
           