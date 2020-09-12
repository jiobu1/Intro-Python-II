from room.room import Room
from player import Player
from room.directions import room
from items.inventory import inventory

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print('Welcome')
player_name = input("What is your name: ")
player = Player(name = player_name, current_room = room['outside'])

print(f'Welcome {player.name}! You are currently in the room {player.current_room}')

while True:

    #Player has to choose direction
    #Selection has to be an input
    selection = input("""Choose a direction: North(n), South(s), East(e), West(w), or Quit(q) """)

    try:
        #Have to cast input as a string
        selection = str(selection.strip().lower())

        if selection == 'q':
            # If the user enters "q", quit the game.
            print(f"Thank you for playing {player.name}")
            break

        elif selection in ('n','s','e','w'):
            if player.move(selection) != None:
                # * Prints the current room name
                print(f"{player.name}, you are now entering the {player.current_room}")
            else:
                # If the user enters a cardinal direction, attempt to move to the room there.
                # Print an error message if the movement isn't allowed.
                s = "You cannot go in this direction"

        elif selection == 'p':
            #random.choice
            # if else of what whill happen when they get different items
            #if they win - message
            #if they lose - message
            pass

        elif selection == 'd':
            # drop item
            # remove item from players inventory
            # add to regular inventory
            pass

        else:
            print("Please choose a valid direction.")

    except TypeError:
        print("Please choose n, s, e, w.")


# * Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.
"""
To Do:
inventory available in room
player's inventory
randomly assign item
if they win - message
if they lose - message
"""