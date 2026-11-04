# 0 tuhjad alad
# 1 alad kuhu saab liikuda
# 2 alustamisruut
# 3 lopetamisruut
# ules alla votab 2 blokki ruumi
# korvale votab 1/2 vaheldumisi ruumi

board = {
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 3, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
}

def solveTheLevel():
    # vaatab kuhu saab liikuda, liigub
    # kirj massiivi enda liikumise kohta
    # ss kutsub uuesti sama solvethelevel
    # edasi tagasi seni kuni jouab lahenduseni
    # kui ei saa liikuda - liigub tagasi sammu vorra ja proovib jargmise voimaliku kaigu
    for(x in boards):
        for(y in boards[x]):
    # kutsu uuesti solvethelebel

def moveUp():
    # liigub ules

            

def moveDown():
    # liigub alla

def moveLeft():

def moveRight():