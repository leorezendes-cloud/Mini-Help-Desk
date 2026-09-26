#!/usr/bin/env python3

import random
secret_number = random.randint(1, 10)
guess = 0
attempts = 0
min_allowed = 1
max_allowed = 10

while guess !=  secret_number and attempts < 3:
    guess = int(input('Guess a number between 1 and 10: '))
    
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
            print('too hight my friend, Trey Again')
    elif guess == secret_number:
        print('Congets Bro, You did it!')
        break
if attempts == 3:
    print('Game Over!! You ran out of attempts, Sorry!')