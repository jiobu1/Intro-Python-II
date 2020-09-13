from room import Room
from player import Player
from items import Item
from directions import room
from inventory import inventory

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
    selection = input("""
    Please pick a direction, action, or view your inventory:
    North(n) South(s) East(e) West(w)
    Search(search) the room
    View inventory(items)
    Quit(q).  """
    )

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

        elif selection == 'search':
            # if player.inventory == inventory['poison']:
            #     take_job = input('Do you take the job? (Y/N): ').upper()
            #     print(f"""Sorry {player.name}!
            #     Game over!
            #     Thank you for playing {player.name}!
            #     Play again soon...""")
            #     break

            # elif player.inventory == inventory['book']:
            #     player.book = True
            #     print(f"""Congratulations {player.name}!
            #     You won the game! You found the Book of Knowledge!
            #     Thank you for playing {player.name}!
            #     Play again soon...""")
            #     break

            # else:
                player.search()

        elif selection == 'items':
            player.check_inventory()

        else:
            print("You cannot perform this action. Please choose a valid action.")

    except TypeError:
        print("You cannot perform this action. Please choose a valid action.")
