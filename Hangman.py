# Displays the rules:

print('Rules of the game:')
print('1. Start guessing letters in the secret word.')
print('2. A letter will be filled in the blanks if the players guesses correctly.')
print('3. You have 8 lives')
print('4. You win if you guess the word correctly')
print('5. All the letters you guessed will be displayed below\n')

# Module/ Package import section
import random


# Function Section

def random_word():
    # generates and returns a random word
    wordlist = ['science', 'network', 'memory', 'establish', 'spring', 'theory', 'maintain', 'traditional',
                'control', 'structure', 'discover', 'production', 'evening', 'conference', 'evening',
                'trip', 'inside', 'worry', 'challenge', 'improve', 'beautiful', 'alcohol', 'average', 'claim',
                'dream', 'hangman', 'laugh', 'various', 'leg', 'environment', 'station', 'blue', 'pink', 'orange',
                'grape', 'honey', 'printer', 'python', 'computer', 'skill', 'sister', 'family', 'father', 'arrive',
                'message', 'disease', 'prepare', 'central', 'shoot', 'moment', 'before', 'focus', 'author', 'pot',
                'flight', 'hospital', 'thousand', 'condition', 'short', 'term', 'period', 'red', 'number', 'water']
    word = random.choice(wordlist)
    return word


def display(turns):
    # Displays the Hangman's status!
    if (turns == 8):
        print("\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 7):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 6):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 5):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 4):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 3):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|   /|\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 2):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|   /|\\\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 1):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|   /|\\\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|   / \n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")
    elif (turns == 0):
        print("\
                \t\t\t\t\t_____\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|    O\n\
                \t\t\t\t\t|   /|\\\n\
                \t\t\t\t\t|    |\n\
                \t\t\t\t\t|   / \\\n\
                \t\t\t\t\t|\n\
               \t\t\t\t\t\t----")


ch = 'yes'
while (ch == "yes" or ch == "Yes" or ch == "y" or ch == "Y" or ch == "YES" or ch == 's' or ch == 'S'):

    # Random_word function call
    word = random_word()
    n = len(word)
    lst1 = []
    used = []  # Stores the guesses made by the player
    turns = 8  # maximum wrong guesses made by player
    bp = 0     # breakpoint
    print('Guess this word:')

    # prints n '_'
    for i in word:
        print('_', end=' ')
    print('\n')

    # Is executed untill turns don't exhaust
    while turns > 0:
        w = input('\nEnter a Letter (or) the word: ')
        #breaks if the word and input are the same
        if w == word:
            break

        # If player re-enters the same letter more than twice
        if w in used:
            print('The letter is already guessed!')
            continue
        elif w not in word:
            turns -= 1

        # appends the entered letter to the used letters list
        used.append(w)
        for i in range(n):
            if word[i] == w:
                lst1.append(i)

        # displays the status of the word
        for k in range(n):
            if k in lst1:
                print(word[k], end=' ')
            else:
                print('_', end=' ')
        print()

        # Calls display function to display the status of hangman
        display(turns)

        # for each case display the used letters
        print('Letters Used so far: ', end='')
        for i in used:
            print(i, end=' ')
        print()

        print('Remaining tries:', turns)
        bp = len(lst1)
        if (bp == n):
            break
        print('\n-------------------------------------------------------------------------------------------------------------------------------------------------\n')
    if turns == 0:
        print('Play again, you lost!')
        print('Your word was:', word, end='\n')
    else:
        print('Congratulations! you won!!\n')
    ch = input('\nEnter "yes" to play again? ')
