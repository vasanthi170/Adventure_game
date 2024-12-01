name = input('Hello user! Enter your name: ')
print(f'Hello {name}, welcome to the game...!')

wanna_play = input('Do you want to play? (yes/no): ').lower()

if wanna_play == 'yes' or wanna_play == 'y':
    weapon = input('Choose your weapon (stick/sword): ').lower()
    print('Choose your direction carefully...')
    direction = input('Which direction? (left/right): ').lower()
    
    if direction == 'left':
        print('You chose the wrong direction... There is danger!')
        print('Game Over!')
    elif direction == 'right':
        print('There is a bridge in front of you.')
        choice = input('How do you want to cross it? (swim/cross/boat): ').lower()
        
        if choice == 'swim' and weapon == 'stick':
            print('You were eaten by an alligator... Game Over!')
        elif choice == 'swim' and weapon == 'sword':
            print('you choice is wrong.. but still u survived!')
        elif choice == 'boat' and weapon == 'stick':
            print('You safely crossed the river with the stick.')
            print('Congratulations! You survived!')
        elif choice == 'cross' and weapon == 'sword':
            print('You fought off the dangers and crossed the bridge. Well done!')
        else:
            print('You made an unwise choice. Game Over!')
    else:

        print('Invalid direction. Game Over!')
else:
    print('We are not playing. Goodbye!')
