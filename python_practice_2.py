#!/usr/bin/env python3

import random


def play_game():


    print(f'   ====================================')
    print(f'   ====================================')
    print(f'   ====================================')
    print(f'   ====================================')
    print(f'   ====================================')
    print(f'              Guessing Game')
    print(f'   ====================================')
    print(f'   ====================================')

   



    print(f'''        I am thinking of a number 
      You have 3 attempts per round
    Guess the number 3 times in a row 
    and you win ...you win BIG TIME!!!''')

    import random



    round = 1
    secret_number = random.randint(1, 5)
    guess = 0
    attempts = 0
    min_allowed = 1
    max_allowed = 5


    while round == 1:
        
        while guess !=  secret_number and attempts < 3:
            guess = int(input('Round 1 - Guess a number between 1 and 5: '))
        
            if guess < min_allowed:
                attempts += 1
                print('Bro, i said too LOW!!, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess > max_allowed:
                attempts += 1
                print('You really are too high, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess < secret_number:
                min_allowed = guess + 1
                attempts += 1
                print("Too low bro, Try gettin' higher Try Again")
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('Too high my friend, Tranquillo Try Again')
            elif guess == secret_number:
                print('Congets Bro, Next Round....FIGHT!')
                round += 1
            break
        if attempts == 3:
            print('Game Over!! Kick rocks Kid.. outta tries..')  
            play_again = input('Wanna play again? (y/n): ')
            if play_again.lower() == 'y':
                round = 1
            break   


    secret_number = random.randint(1, 10)
    guess = 0
    attempts = 0
    min_allowed = 1
    max_allowed = 10

    while round == 2 and attempts < 3:
    
        while guess !=  secret_number and attempts < 3:
            guess = int(input('Round 2 - Guess a number between 1 and 10: '))
        
            if guess < min_allowed:
                attempts += 1
                print('Bro, i said too LOW!!, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess > max_allowed:
                attempts += 1
                print('You really are too high, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess < secret_number:
                min_allowed = guess + 1
                attempts += 1
                print("Too low bro, Try gettin' higher Try Again")
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('Too high my friend, Tranquillo Try Again')
            elif guess == secret_number:
                print('Congets Bro, Next Round....FIGHT!')
                round += 1
            break
        if attempts == 3:
            print('Game Over!! Kick rocks Kid.. outta tries..')  
            play_again = input('Wanna play again? (y/n): ')
            
              
            break

    secret_number = random.randint(1, 15)
    guess = 0
    attempts = 0
    min_allowed = 1
    max_allowed = 15

    while round == 3 and attempts < 3:
        
        while guess !=  secret_number and attempts < 3:
            guess = int(input('Round 3 - Guess a number between 1 and 15! HA!!: '))
        
            if guess < min_allowed:
                attempts += 1
                print('Bro, i said too LOW!!, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess > max_allowed:
                attempts += 1
                print('You really are too high, Try Again')
                print('This still counts as an Attempt, smh')
            elif guess < secret_number:
                min_allowed = guess + 1
                attempts += 1
                print("Too low bro, Try gettin' higher Try Again")
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('Too high my friend, Tranquillo Try Again')
            elif guess == secret_number:
                print('Congets Bro, You Win BIG TIME!!')
                play_again = input('Wanna play again? (y/n): ')
                
                    
            
        if attempts == 3:
            print('Game Over!! Kick rocks Kid.. outta tries..')
            play_again = input('Wanna play again? (y/n): ')


    return play_again
play_again = play_game()

while True :  
    if play_again == 'y':
       play_again = play_game()
    else:
        print('Nobody likes a quitter...Peace Out!!')
        break
