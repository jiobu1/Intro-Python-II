# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} is at the {self.current_room}'

    def move(self, direction):
        if self.current_room.__call__(direction) == None:
            print(f"You cannot go in that direction, you are staying in {self.current_room.name}")
        else:
            self.current_room = self.current_room.__call__(direction)
            return  self.current_room

    def pickup(self, item):
        self.inventory.append(item)
        print(f"{self.name}, {item.name} is added to your inventory!")

    def drop(self, item):
        self.inventory.remove(item)
        print(f"{self.name}, {item.name} has been removed from your inventory!")

    def inventory_list(self):
        pass

if __name__ == '__main__':
    pass