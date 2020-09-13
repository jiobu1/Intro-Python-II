from room import Room
from player import Player
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
                      Please pick a direction, action, or view your intventory:
                      North(n) South(s) East(e) West(w)
                      Take item(take [name]) Drop item(drop [name])
                      View inventory(i)
                      Quit(q)."""
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

        elif selection[0] == 'take':
            for item in player.current_room.inventory:
                if selection[1] in item.name:
                    player.pickup(item)
                    player.current_room.remove_item(item)
                    print(f"""\nYou find yourself at the {player.current_room}
                        There is {player.current_room.room_items()} on the ground.""")

            else:
                print(f'{selection[1]} not in room.')
                print(f"""\nYou find yourself at the {player.current_room}
                       There is {player.current_room.items_in_room()} on the ground.""")

        elif selection[0] == 'drop':
            for item in player.inventory:
                if selection[1] in item.name:
                    player.drop_item(item)
                    player.current_room.add_item(item)
                    print(f"""\nYou find yourself at the {player.current_room}
                        There is {player.current_room.items_in_room()} on the ground.""")

                else:
                    print(f'{selection[1]} not in inventory')
                    print(f"""You find yourself at the {player.current_room}
                        There is {player.current_room.items_in_room()} on the ground.""")

        elif action == 'check':
            player.check_inventory()

        elif player.inventory.name == item['book']:
            player.foundBook = True
            if item['book'] in player.inventory:
                print(f"""Congratulations {player.name}!
                       You won the game! You found the goose!
                       Thank you for playing {player.name}!
                       Play again soon...""")
                break

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