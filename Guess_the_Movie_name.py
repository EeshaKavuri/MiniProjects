'''
Created on TUES Oct 10 14:14:27
@author: eesha.kavuri
'''
import random, pandas
movies = ['dead pool','conguring', 'cindella', 'spiderman', 'titanic']

def create_question(movie):
    n = len(movie)
    letters = list(movie)
    temp = []
    for i in range(n):
        if letters[i] == ' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn = ''.join(str(x) for x in temp)
    return qn

def is_present(letter, movie):
    c = movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn, movie, letter):
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n):
        if ref[i] == ' ' or ref[i] == letter:
            temp.append(ref[i])
        else:
            if qn_list[i] =='*':
                temp.append('*')
            else:
                temp.append(ref[i])
        qn_new = ''.join(str(x) for x in temp)
        return qn_new

def play():
    p1name = input('Player 1!please enter your name: ')
    p2name = input('Player 2!please enter your name: ')
    pp1, pp2, turn = 0, 0, 0
    willing = True
    while willing:
        if turn%2==0:
            print(p1name,',Your turn: ')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter,picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie name or 2 to unlock another letter:')
                    if d==1:
                        ans = input('Your answer:')
                        if ans == picked_movie:
                            pp1+=1
                            print('Correct')
                            not_said = False
                            print(p1name,'Your score : ',pp1)
                        else:
                            print('Wrong answer, Try again!')
                else:
                    print(letter,' not found')
        else:
            print(p1name,',Your turn: ')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input('Your letter: ')
                if is_present(letter,picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print(modified_qn)
                    d = input('Press 1 to guess the movie name or 2 to unlock another letter:')
                    if d==1:
                        ans = input('Your answer:')
                        if ans == picked_movie:
                            pp1+=1
                            print('Correct')
                            not_said = False
                            print(p1name,'Your score : ',pp1)
                        else:
                            print('Wrong answer, Try again!')
                else:
                    print(letter,' not found')
        c = input('Press 1 to continue or 0 to quit')
        if c==0:
                data = {'name':[p1n,p2n],
                        'points':[pp1,pp2]
                       }
                print(pandas.DataFrame(data, index=[1,2]))
                print('Thanks from playing')
                print('Have a nice day')
                willing = False
        turn += 1
play()
