import random
import time

def user_name():
    name = input('What is your name? ')
    return name
    
def displayIntro():
    print(user_name, ' is in a land full of dragons. In front of ', user_name, ',')
    print(user_name, ' sees two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with ', user_name, '. Another dragon')
    print('is greedy and hungry, and will eat ', user_name,' on sight.')
    print('The third dragon is tired and will breathe balls of fire')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3':
        print('Which cave will ', user_name, ' go into? (1, 2, or 3)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print(user_name, ' approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of ', user_name, '! He opens his jaws and...')
    print()
    time.sleep(2)
    

    if chosenCave == "1":
         print('Gives ', user_name, ' his treasure!')
    elif chosenCave == "2":
         print('Gobbles ', user_name, ' down in one bite!')
    else:
        print("Breathes out a fireball at ", user_name)

user_name = user_name()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('Do ', user_name, ' want to play again? (yes or no)')
    playAgain = input()