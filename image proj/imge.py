
from PIL import Image, ImageFilter
import os

size200 = (200,200)
size500 = (500,500)

for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)

        i.thumbnail(size500)
        i.save('500/{}_500{}'.format(fn,fext))

        i.thumbnail(size200)
        i.save('200/{}_200{}'.format(fn,fext))

astro = Image.open("astro.jpg")
astro.rotate(180).show()

bigmac = Image.open("bigmac.jpg")
bigmac.convert(mode = 'L').show("bigmac.jpg")

car = Image.open("car.jpg")
car.rotate(270).show("car.jpg")

cat = Image.open("cat.jpg")
cat.filter(ImageFilter.GaussianBlur(10)).show("cat.jpg")

dog = Image.open("dog.jpg")
dog.convert(mode = 'L').show("dog.jpg")

Moon = Image.open("Moon.jpg")
Moon.rotate(25).show("Moon.jpg")

pancakes = Image.open("pancakes.jpg")
pancakes.filter(ImageFilter.GaussianBlur(20)).show("pancakes.jpg")

panda = Image.open("panda.jpg")
panda.convert(mode = 'L').show("panda.jpg")

raps = Image.open("raps.jpg")
raps.rotate(90).show(r'pics\ImageM.py\raps.jpg')

wave = Image.open("wave.jpg")
wave.show("wave.jpg")

j_list = ['astro', 'bigmac', 'car','cat', 'dog', 'moon','pancakes', 'panda', 'raps', 'wave']
a_list = ['rotate', 'resize', 'png', 'blur', 'black and white']
def displaylist(x):
    for i in x:
        print(i)
    print('')
def run():
    while True:
        print ("Images: ")
        displaylist(j_list)
        choice = input("Which image should we change?: ").lower()
        if choice in j_list:
            userImage = Image.open(f"{choice}.jpg")
            userImage.show()
            if user_confirm() == True:
                break
            else:
                print("Invalid Input\n")
        alterimage()

def user_confirm():
    choice = input ("Should we edit this image? (yes) or (no): ").lower()
    if choice == "yes":
        return True
    elif choice == 'no':
        print("")
        run()
    else:
        print('invalid input')

def alterimage():
    while True:
        print ("Alter options: ")
        displaylist(a_list)
        choice = input('Select alter mode: ').lower()
        if choice in a_list:
            if user_confirm() == True:
                if choice == a_list[0]:
                    choice.rotate()
                if choice == a_list[1]:
                    choice.resize()
                if choice == a_list[2]:
                    choice.png()
                if choice == a_list[3]:
                    choice.blur()
                if choice == a_list[4]:
                    choice.blacknwhite()



                                   