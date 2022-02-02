'''

Created on TUES Oct 10 14:14:27
@author: eesha.kavuri

'''
import random, pandas
def choose():
    words = ['rainbow', 'computer', 'science' ,'programming','mathematics',
             'player','condition','reverse', 'water', 'board']
    pick = random.choice(words)
    return pick
     
def jumble(word):
    jumbled = ''.join(random.sample(word,len(word)))
    return jumbled

def thank(p1n, p2n, pp1, pp2):
    data = {'name':[p1n,p2n],
            'points':[pp1,pp2]
           }
    print(pandas.DataFrame(data, index=[1,2]))
    
def play():
    p1name = input('Player 1, Please enter your name:')
    p2name = input('Player 2, Please enter your name:')
    pp1, pp2, turns = 0, 0, 0
    while(True):
        picked_word = choose()
        question = jumble(picked_word)
        print(question)
        #player 1
        if turns%2 == 0:
            print(p1name, ', Your turn:')
            ans = input('What is on my mind?')
            if ans==picked_word:
                pp1+=1
                print('Your score is: ',pp1)
            else:
                print('Better luck next time, I thought: ',picked_word)
        #player 2
        else:
            print(p2name, ', Your turn:')
            ans = input('What is on my mind?')
            if ans==picked_word:
                pp2+=1
                print('Your score is: ',pp2)
            else:
                print('Better luck next time, I thought: ',picked_word)
        #To exit or continue
        c = int(input('Press 1 to continue and 0 to quit: '))
        if c==0:
            thank(p1name, p2name, pp1, pp2)
            break
        turns+=1
        
play()
