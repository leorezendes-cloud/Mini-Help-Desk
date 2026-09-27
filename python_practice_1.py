#!/usr/bin/env python3

print(f'====================================')
print(f'====================================')
print(f'          Guessing Game')
print(f'====================================')
print(f'====================================')


print(f'''I am thinking of a number 
You have 3 attempts per round
Guess the number 3 times in a row and you win
....you win BIG TIME!!''')

import random

while 
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
                print('Too low bro, Try Again')
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('too high my friend, Try Again')
            elif guess == secret_number:
                print('Congets Bro, Next Round....FIGHT!')
                round += 1
                break
            if attempts == 3:
                print('Game Over!! You ran out of attempts, Sorry!')  
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
                print('Too low bro, Try Again')
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('too high my friend, Try Again')
            elif guess == secret_number:
                print('Congets Bro, Next Round....FIGHT!')
                round += 1
                break
            if attempts == 3:
                print('Game Over!! You ran out of attempts, Sorry!')
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
                print('Too low bro, Try Again')
            elif guess > secret_number:
                max_allowed = guess - 1
                attempts += 1
                print('too high my friend, Try Again')
            elif guess == secret_number:
                print('Congets Bro, You Win BIG TIME!!')
                round += 1
                break
        if attempts == 3:
            print('Game Over!! You ran out of attempts, Sorry!')
            break
