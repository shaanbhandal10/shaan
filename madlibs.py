#An example is:
#youtuber = "Garcha_meatbros" # some string variable
#print("subscribe to " + youtuber)

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")
partofabody = input("A part of the body: ")
place = input("A place: ")
ing_verb = input("A verb ending in ing: ")
noun = input("A noun: ")
number = int(input("A number: "))
def madlib1():
    f"Computer programming is so {adj}! It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! But when I'm not \
    programming, you can usually see me working out my {partofabody}. I usually work out at {place}, \
    to which I usually like {ing_verb} to. And when I'm not working out you could find me at the local \
    park walking my {noun}. Then to end of the day I usually go to sleep by using the counting sheep \
    method, and tonight I counted {number}. "
def madlib2():
    f"Seeing Arsh the goat Garcha play basketball is so {adj}! It just makes me wanna run up \
    some {number}s. The way that Arsh the goat Garcha {verb1}s is just so spectacular. Not to mention \
    his huge {partofabody} shows that he's dominant in the paint as well. The play style of Arsh the \
    goat Garcha reminds me of {famous_person}. Arsh plays as if he's playing in {place}. After seeing \
    Arsh the goat Garcha play it incourages me to do something active, so I start {ing_verb}. But the \
    only sad part of the night was while I was {ing_verb} I accidently hit a {noun} and tore my acl.\
    Then I thought to myslef good thing that didn't happen to Arsh the goat Garcha!"
def madlib3():
    f"The man the myth the legend himself {famous_person} is just so {adj} that the man the \
    man himself cured world hunger, because of his soccer skills. The legend himself known for being \
    the legend of{place}. Not only is he a soccer star, but he can also {verb1} like no one else. He \
    {verb1} so gracefully with the number {number} jersey. But what truely stands out his huge {partofabody}. \
    But not all soccer stars are like {famous_person}, sometimes they need a break and get a sub to drink some{noun}. \
    But then {famous_person} is ready to go onto the field to start {ing_verb}. After that he scores a hat trick \
    and calls it a day after the 3-0 dub."

storynumber = input("Which story would you like to play? (1, 2, 3, or q): ")

if storynumber == "1":
    madlib1()
elif storynumber == "2":
    madlib2()
elif storynumber == "3":
    madlib3()
elif storynumber == "q":
    print("You have succesfully quit.")
else:
    print("Invalid input. Click run and choose again.")



