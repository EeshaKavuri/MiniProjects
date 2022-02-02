
from PIL import Image
import random
end = 100

'''
def show_board():
    img = Image.open('Screenshot\(105\).jpg')
    img.show()
'''

def check_ladder(points):
    if points==8:
        print('Ladder')
        return 26
    elif points==21:
        print('Ladder')
        return 82
    elif points==43:
        print('Ladder')
        return 77
    elif points==50:
        print('Ladder')
        return 91
    elif points==62:
        print('Ladder')
        return 96
    elif points==66:
        print('Ladder')
        return 87
    elif points==80:
        print('Ladder')
        return 100
    else:
        #Not a ladder
        return points 

def check_snake(points):
    if points==44:
        print('Snake')
        return 22
    elif points==46:
        print('Snake')
        return 5
    elif points==52:
        print('Snake')
        return 11
    elif points==55:
        print('Snake')
        return 7
    elif points==59:
        print('Snake')
        return 17
    elif points==64:
        print('Snake')
        return 36
    elif points==69:
        print('Snake')
        return 33
    elif points==73:
        print('Snake')
        return 1
    elif points==83:
        print('Snake')
        return 19
    elif points==92:
        print('Snake')
        return 51
    elif points==95:
        print('Snake')
        return 24
    elif points==98:
        print('Snake')
        return 28
    else:
        #not a snake
        return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1_name = input('Player 1, Please enter your name: ')
    p2_name = input('Player 2, Please enter yout name: ')
    pp1, pp2, turn =0, 0, 0
    while True:
        if turn%2==0:
            #player 1 turn
            pp = pp1
            p_name = p1_name
        else:
            #player 2 turn
            pp = pp2
            p_name = p2_name
        print(p_name,'your turn')
        dice = random.randint(1,6)
        print('Dice showed:',dice)
        pp += dice
        pp = check_ladder(pp)
        pp = check_snake(pp)
        #check if the player goes beyond the board
        if pp>end:
            pp = end
        print(p_name,'Your score:',pp)
        if reached_end(pp):
            print(p_name,'won')
            break
        c = int(input('Press 1 to continue, 0 to quit: '))
        if c==0:
            print(p1_name,'scored',pp1)
            print(p2_name,'scored',pp2)
            print('Quitting the game, Thanks for playing!')
        print()
            
#show_board()
play()
