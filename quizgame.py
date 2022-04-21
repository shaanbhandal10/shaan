from tkinter.messagebox import YES


print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes) or (no)")

if playing != "yes":
    quit()
print("Okay! Let's play :)")
def gamequiz():
    answer = input("What is James's favourite NBA team(the 76ers) or (the raptors)? ").lower()
    if answer == "the 76ers":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("What does UBC stand for?").lower()
    if answer == "university of british columbia":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("Are the Raptors gonna win the NBA championship (yes) or (no)? ").lower()
    if answer == "yes":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("What's 9 + 10? ").lower()
    if answer == "21":
        print("correct! :)")
    else:
        print("You stupid. :(")

    answer = input("Did Ozem deserve the best drip award in KP (yes) or (no)? ").lower()
    if answer == "yes":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("Is Akash the worst driver in KP (yes) or (no)? ").lower()
    if answer == "yes":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("What game did Kawal play on his youtube channel? ").lower()
    if answer == "agario":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("What school won the winter tip off in 2021? ").lower()
    if answer == "kwantlen park":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("Was Arsh Garcha selected to be an all star this year (yes) or (no)? ").lower()
    if answer == "yes":
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("Is Tottenham the best team in the premier leauge (yes) or (no)? ").lower()
    if answer == "yes":
        print("correct! :)")
    else:
        print("inncorrect. :(()")

gamequiz()

keep_playing = input("Would you like to kepp playing (y) or (n)").lower()

while keep_playing == 'y':
    gamequiz()
    keep_playing = input("Would you like to kepp playing (y) or (n)").lower()
    if keep_playing == 'n':
        print("You have quit the game!")

