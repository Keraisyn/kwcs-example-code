# Text-Based Adventure Game
# Author: Matthews Ma

# How to create the game (Follow the examples below for more information):
# - Create a new "room" or "area" using the def command
# - Ask user where they want to go or what action they want to do. Save this in a variable.
# - Use if-statements to find the next "room" or "area".
# - Send the player to that place.


# You can use variables to keep track of things the user does.
coins = 0

def room():
    print("You are in your room. Where do you want to go?")
    print("You need 2 coins to win!")

    # Check forest() for a detailed explanation of this.
    global coins
    if coins >= 2:
        win()

    print("Option 1: school")
    print("Option 2: forest")

    option = int(input())

    if option == 1:
        school()
    elif option == 2:
        forest()


def school():
    print("You are in the school.")
    print("Option 1: forest")

    option = int(input())

    if option == 1:
        forest()


def forest():
    # You must declare any variables used as global. The reason for this is a bit complicated.
    global coins

    print("You are in the forest.")

    # Add a coin to the coins variable. Make sure you declare it as global!
    print("You found a coin!")
    coins = coins + 1

    print("Option 1: room")

    option = int(input())

    if option == 1:
        room()


def win():
    print("You win!!")


# Start at the room.
room()
