import random;
# num = random.randint(1,13)

def main():
    num = random.randint(1,13)
    restart = "y"
    player_score = 300
    while restart == 'y' and player_score != 0:
        print(f'The card is: {num}')
        guess = input('Higher or lower? [h/l] ')
        print(f'Next card was: {nnum(num)}')
        print(f'Your score is: {score(player_score, guess, num)}')
        restart = input('Play again? [y/n] ')
    print('Thank you for playing')

def nnum(num):
    num = random.randint(1,13)
    return num

def score(player_score, guess, num):
    if guess == 'h':
        guess = num + 1
        if guess >= num:
            player_score = player_score + 100
        else:
            player_score = player_score - 75
    elif guess == 'l':
        guess = num - 1
        if guess <= num:
            player_score = player_score + 100
        else:
            player_score = player_score - 75
    return player_score

main()