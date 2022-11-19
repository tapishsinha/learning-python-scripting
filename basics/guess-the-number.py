import random

print('Let us play the guessing game')
print('You have 5 tries to guess what number I am thinking')

number=random.randint(1, 20)

for i in range (1,6):
    print('Take your guess from 1 to 20')
    guess=int(input())

    if guess > number:
        print('Your guess is too high')

    elif guess < number:
        print('Your guess is too low')

    else:
        break

if guess == number:
        print('You guessed it right')

else:
    print('My number was '+str(number))