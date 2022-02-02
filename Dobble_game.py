'''

Created on TUES Oct 10 14:14:27
@author: eesha.kavuri

'''
#Dobble game:
#any two lists have only 1 and only 1 letter in common not more or less

import string
import random
symbols = list(string.ascii_letters)
card1, card2 = [0]*5, [0]*5
#pos1 and pos2 are same symbol positions in card1 and card 2
pos1, pos2 = random.randint(0,4), random.randint(0,4)
samesymbol = random.choice(symbols)
card1[pos1] = samesymbol
card2[pos2] = samesymbol
symbols.remove(samesymbol)
card1[pos2] = random.choice(symbols)
symbols.remove(card1[pos2])
card2[pos1] = random.choice(symbols)
symbols.remove(card2[pos1])
i = 0
while i<5:
    if i!=pos1 and i!=pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i+=1
print(card1)
print(card2)
ch = input('Spot the SAME symbol: ')
if ch==samesymbol:
    print('Right')
else:
    print('Wrong, Correct symbol:',samesymbol) 
