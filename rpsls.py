import random
counter = 0
def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors, 'l' for lizzard,'sp' for spock: ")
    computer = random.choice (['r', 'p', 's','l','sp'])
    if user == computer:
        return 'It is a tie'
    if is_win(user, computer):
        global counter
        counter += 1
        return 'Great job, you won!'

    return 'You took the L'
    

def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r') or (player == 'l' and opponent =='sp') \
        or (player == 'l' and opponent == 'p') or (player == 'sp' and opponent == 's') \
        or (player == 'sp' and opponent == 'r') or (player == 'r' and opponent == 'l') \
        or (player == 'p' and opponent == 'sp') or (player == 's' and opponent == 'l'):
        return True
playon = input("Would you like to continue playing? (Yes (y) or No (n): ")

while playon == 'y':
    print(play())
    playon = input("Would you like to continue playing? (Yes (y) or No (n): ")
    if playon == 'n':
        print("you have quit the game")
        print("you have won " + str(counter) + " rounds")
        

