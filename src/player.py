# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.no_book = True
        self.alive = True
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
                print(f'You found the {item.name}\n')
                take_item = input('Take item? (Y/N): \n ---> ')
                if take_item[0].lower() == 'y':
                    if item.name == "Ricin \n":
                        print("""You have touched Ricin, one of the most deadliest of poisons in the world, sorry, but you are dead now. Goodbye...""")
                        self.alive = False
                    elif item.name == "Treasure Chest \n":
                        print(f"""This is the Treasure Chest. You will not have to work for the rest of your life, there are enough spoils in these coiffers to make King Midas jealous 
                        but you cannot take this treasure without another item.""")
                        items_taken += 0
                    elif item.name == "Book of Knowledge \n":
                        print("""This is the real treasure! The Book of Knowledge, holds all the secrets of the world. As, an added bonus, you also get the treasure chest. \n You have won the game!
                        Hope you play again soon!""")
                        self.inventory.append(item)
                        items_taken += 1
                        self.no_book = False
                    else:
                        print(f'{item.description}\n')
                        self.inventory.append(item)
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