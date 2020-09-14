# Implement a class to hold item information. This should have name and
# description attributes.

class Item:

    def __init__(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image

    def __str__(self):
        return f'{self.name}.\n{self.description}'

