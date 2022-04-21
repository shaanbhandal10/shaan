from PIL import Image
image1 = Image.open("bleach.webp")
def bigmac():
    print("You ate the bigmac and you are now not hungry and have survied and won the game!")
def icecream():
    print("The icecream machine is broken bozo, it's Mcdonald's what did you expect.")
def nothing():
    print("You have starved to death. :(")
def mcdonalds():
    choice = input("You now pull up to Mcdonald's and you have the option of eating a BIGMAC or an ICECREAM cone.").lower()
    if choice == "icecream":
        icecream()
    elif choice == "bigmac":
        bigmac()
    else:
        print("invalid option. L + ratio + youngboy better")

def eggs():
    image1.show()
    print("James does not like eggs so james secretly pours bleach in your eggs and you die")
def pancakes():
    choice = input("You have made the pancakes with james as james starts eating the pancakes with passion, but you just realized that James ate your pancakes as well. What do you do? (Get MCDONALDS) or (eat NOTHING)").lower()
    if choice == "mcdonalds":
        mcdonalds()
    elif choice == "nothing":
        nothing()
    else:
        print("invalid option. L + ratio + youngboy better")
def run():
    print("You have run to the cops and have gotten James in jail for breaking into your house")
def breakfast():
    choice = input("Now you and James appear to be in the kitchen cookin up PANCAKES or EGGS. What do you do?").lower()
    if choice == "pancakes":
        pancakes()
    elif choice == "eggs":
        eggs()
    else:
        print("invalid option. L + ratio + youngboy better")
def first_choice():
    choice = input("You wake up, you see james sitting right next to you on your bed. What do you do?(RUN and call for help) or (make BREAKFAST with James)").lower()
    if choice == "breakfast":
        breakfast()
    elif choice == "run":
        run()
    else:
        print("invalid option. L + ratio + youngboy better")


name = input("What is your name? ")

check = name.isalpha()
if check == True:
    print(" Welcome to the game " + name + " please enjoy the game and please write down the words that are capitalized to choose which story you would like to continue with.")
    play_game = input("Would you like to play the game (y) or (n)")
    if play_game == "y":
        first_choice()
    else:
        print("You have quit the game")
elif check != True:
    print("Please spin back")
    