# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, direction = None):
        self.name = name
        self.description = description
        self.direction = direction
        # self.items = items
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.inventory = []

    def __call__(self, direction):
        # print(f"Room.__call__ called! direction={direction}")
        self.direction_method = {
            "n": self.n_to,
            "s": self.s_to,
            "w": self.w_to,
            "e": self.e_to
        }
        return self.direction_method[direction]

    def __str__(self):
        return f'{self.name}.\n{self.description}'

    def pickup(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def room_items(self):
        if len(self.inventory) >=1:
            print(f"""Items: {', '.join(self.inventory.name)}""")
        else:
            print('There are no items in this room')

if __name__ == '__main__':
    pass