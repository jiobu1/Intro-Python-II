from items import Item
from directions import room

inventory = {
    "treasure chest": Item("Treasure Chest \n",
    """This is the Treasure Chest. You will not have to work for the rest of your life, there are enough spoils in these coiffers to make King Midas jealous
    but you cannot take this treasure without another item."""),

    "sword": Item("Sword \n",
    """This is a Sword. It is a longsword, engraved with the Excalibur."""),

    "book": Item("Book of Knowledge \n",
    """This is the real treasure! The Book of Knowledge, holds all the secrets of the world. As, an added bonus, you also get the treasure chest. \n You have won the game!"""),

    "ball": Item("Crystal Ball \n",
     """The treasure you seek is not the one you think."""),

    "light": Item("Star of Eärendil \n",
     """This Star of Eärendil, our most beloved star. \n May it be a light to you when all other lights go out."""),

    "poison": Item("Ricin \n",
    """You have touched Ricin, one of the most deadliest of poisons in the world, sorry, but you are dead now. Goodbye..."""),

    "dragon egg": Item("Dragon Egg \n",
    """You have found the Dragon Egg. You are the proud parent of a fierce and beautiful dragon. \n Take care of this creature because it the only one of its kind"""),

    "magic wand": Item("Magic Wand \n",
    """You have in your possession Merlin's wand. \n Be careful where you point that thing! It is really powerful""")
}

#Add items
room['foyer'].inventory = [inventory['sword'], inventory['light']]
room['overlook'].inventory = [inventory['magic wand'], inventory['ball']]
room['narrow'].inventory = [inventory['poison']]
room['treasure'].inventory = [inventory['dragon egg'], inventory['treasure chest']]
room['secret'].inventory = [inventory['book']]

if __name__ == "__main__":
    print(inventory.keys())
    print(inventory.values())