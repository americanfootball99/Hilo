# HILO / Higher or Lower
# Created by: CSE210 1pm Team

# The format for random is random.randInt(*minimum value*, *maximum value*)
# That will spit out a random number in the range

import random;

def main():
    num = random.randint(1,13)
    restart = "y"
    player_score = 300
    while restart == 'y' and player_score != 0:
        print(f'The card is: {num}')
        guess = input('Higher or lower? [h/l] ')
        print(f'Next card was: {new_num(num)}')
        print(f'Your score is: {score(player_score, guess, num)}')
        restart = input('Play again? [y/n] ')
    print('Thank you for playing')

# This generates a new number each round
def new_num():
    ;
# This will calculate the player's score based on if they got it right or wrong
def score():
    ;