# Write a class to hold player information, e.g. what room they are in
# currently.

from items import Item
from inventory import inventory

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.book = False
        self.inventory = []

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'

    def move(self, direction):
        if self.current_room.__call__(direction) == None:
            print(f"You cannot go in that direction, you are staying in {self.current_room.name}")
        else:
            self.current_room = self.current_room.__call__(direction)
            return  self.current_room

    def search(self):
        items_taken = 0
        if len(self.current_room.inventory) >= 1:
            for item in self.current_room.inventory:
                print(f'You found the {item.name}')
                take_item = input('Take item? (Y/N): ')
                # if take_item[0].lower() == 'y':
                #     if player.current_room.inventory == inventory['poison']:
                #         print(f'{item.description}\n')
                #         print(f"""Sorry {player.name}! Game over! Thank you for playing {player.name}! Play again soon...""")
                #         break
                #     elif player.current_room.inventoryfit == inventory['book']:
                #         print(f'{item.description}\n')
                #         print(f'You took the {item.name}. \n Check your inventory with \"items\"\n\n')
                #         print(f"""Sorry {player.name}! Game over! Thank you for playing {player.name}! Play again soon...""")
                #         break
                #     else:
                self.inventory.append(item)
                print(f'{item.description}\n')
                print(f'You took the {item.name}. \n Check your inventory with \"items\"\n\n')
                items_taken += 1

            for _ in range(0, items_taken):
                self.current_room.inventory.pop(0)
                
        else:
            print('After searching hard, you find nothing\n')

    def check_inventory(self):
        if len(self.inventory) >=1:
            #Able to print inventory list
            print(f"""Items: \n {' '.join(map(str, self.inventory))}""")
        else:
            print('you don\'t have any items yet')

if __name__ == '__main__':
    pass