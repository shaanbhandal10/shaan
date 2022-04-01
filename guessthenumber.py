import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You have guessed {random_number}! ')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)? ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, the computer guessed your number!')

which_game = input("What game would you like to play? (user guess, computer guess or quit): ")

if which_game == "user guess":
    user_guess(10)
elif which_game == "computer guess":
    computer_guess(10)
elif which_game == "quit":
    print("You have succesfully quit the game! ")
else:
    print("Invalid option has been choosen. ")
