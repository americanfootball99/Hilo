# HILO / Higher or Lower
# Created by: Logan Simmons

import random;

def main():
    restart = "y"
    player_score = 300
    num = 0
    while restart == 'y' and player_score >= 0:
        num1 = nnum(num)
        num2 = nnum(num)
        print(f'The card is: {num1}')
        guess = input('Higher or lower? [h/l] ')
        print(f'Next card was: {num2}')
        player_score = score(player_score, guess, num1, num2)
        print(f'Your score is: {player_score}')
        restart = input('Play again? [y/n] ')
    print('Thank you for playing')

def nnum(num):
    num = random.randint(1,13)
    return num

def score(player_score, guess, num1, num2):
    if guess == 'h':
        if num1 >= num2:
            player_score = player_score + 100
        else:
            player_score = player_score - 75
    elif guess == 'l':
        if num1 <= num2:
            player_score = player_score + 100
        else:
            player_score = player_score - 75

    else:
        print("Incorrect Input")

    if player_score <= 0:
        print("You Lose!")

    return player_score

if __name__ == "__main__":
    main()