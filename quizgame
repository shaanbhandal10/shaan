from tkinter.messagebox import YES
from PIL import Image #This is to show the images for the code
image1 = Image.open("pancakes.jpg")
image2 = Image.open("UBC.png")
image3 = Image.open("car.jpg")

print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes) or (no)")

if playing != "yes": #This is the loop so you can say yes or no to playing the game
    quit()
print("Okay! Let's play :)")
def gamequiz():#This is the function for the game
    answer = input("What is James's favourite NBA team(the 76ers) or (the raptors)? ").lower()
    if answer == "the 76ers": #This is the if statement for one of the questions for the game
        image1.show()
        print("correct! :)")
    else:
        print("inncorrect. :(")

    answer = input("What does UBC stand for?").lower()#The lower makes everything lowercase
    if answer == "university of british columbia":
        image2.show()
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
        image3.show()
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

keep_playing = input("Would you like to kepp playing (y) or (n)").lower()#This is to continue playing the game

while keep_playing == 'y':# this will let you play again
    gamequiz()
    keep_playing = input("Would you like to kepp playing (y) or (n)").lower()
    if keep_playing == 'n':#This lets you quit the game
        print("You have quit the game!")

