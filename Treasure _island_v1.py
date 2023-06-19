print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

name = input("What is your name, traveler?\n")

choice = input("You find yourself at a fork in the road. The RIGHT path looks a little bumpy and hilly. The LEFT path looks nice and smoothe and paved. \nWhich path will you choose?\n")

if choice.lower() == "right":
    print(f"I'm sorry {name}, but on this path you have broken your ankles and fallen into a pit.\nGAME OVER!")
elif choice.lower() == "left":
    choice2 = input(f"Great job {name}! Your path is smooth as butter, and you soon find yourself at a dock. At the dock is a BOAT with a ferryman who will take you accross the bay for $5. You could also try to SWIM it, but it's not likely that you would make it.\nWhat will you do?\n")
    if choice2.lower() == "swim":
        print(f"Wow, {name}. Getting kinda cocky aren't we? Anyway, on your way to swim accross the entire bay you run out of energy and drown.\nGAME OVER!")
    elif choice2.lower() == "boat":
        choice3 = input(f"You, {name}, have once again made a good decision! The freeyman accepts your money and takes you accross the bay to the island.\nOn the island is a house with three doors: a RED door, a YELLOW door, and a BLUE door.\nWhich do you choose?\n")
        if choice3.lower() == "yellow":
            print(f"Contgrats, {name}! You have found the treasue! YOU WIN!!!")
        elif choice3.lower() == "blue":
            print(f"Sorry, {name}, but you have drowned slowly in a room full of water!\nGAME OVER!")
        elif choice3.lower() == "red":
            print(f"What a way to die, {name}. When you open the door a burst of flames comes and consumes your flesh, leaving only char and bone.\nGAME OVER!")
        else:
            print(f"That is not a valid input {name}, but since this game isn't programmed with recursion or functions, a gargle of goblins comes and mugs you, takes all of your money and equipment, and you starve and die.\nGAME OVER")
    else:
            print(f"That is not a valid input {name}, but since this game isn't programmed with recursion or functions, a gargle of goblins comes and mugs you, takes all of your money and equipment, and you starve and die.\nGAME OVER")
        
else:
    print(f"That is not a valid input {name}, but since this game isn't programmed with recursion or functions, a gargle of goblins comes and mugs you, takes all of your money and equipment, and you starve and die.\nGAME OVER")
    