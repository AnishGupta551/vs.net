# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is the minimum number to guess in between?')
user_min = int(input())
print('What is the maximum number to guess in between?')
user_max = int(input())


number = random.randint(user_min, user_max)
number_guesses = int(input('Enter the max number of guesses'))

print('Well, I am thinking of a number between '+str(user_min)+' and '+str(user_max)+'.')

while guessesTaken <= number_guesses:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
    
