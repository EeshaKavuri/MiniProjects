import random
doors = [0]*3
goatdoors = [0]*2
swap = 0
dont_swap = 0
#xth door will comprise of BMW
j = 0
while j<10:
    x = random.randint(0,2)
    doors[x] = 'BMW'
    for i in range(3):
        if i==x:
            continue
        else:
            doors[i] = 'Goat'
            goatdoors.append(i)
    choice = int(input('Enter your choice: '))
    #open a door that comprise of goat
    door_open = random.choice(goatdoors)
    while door_open==choice:
        door_open = random.choice(goatdoors)
    ch = input('Do you want to swap? (y/n): ')
    if ch=='y':
        if doors[choice]=='Goat':
            print('Player wins')
            swap += 1
        else:
            print('Player lost')
    else:
        if doors[choice]=='Goat':
            print('player lost')

        else:
            print('Player wins')
            dont_swap+=1
    j+=1

print(swap)
print(dont_swap)
