from items import Items
from room import Room
from directions import room

inventory = {
    "treasure_chest": Items("Treasure Chest",
                            """You will not have to work for the rest of your life,
                            there are enough spoils in these coiffers to make King Midas jealous
                            but you cannot take this treasure without another item."""),
    "sword": Items("Sword",
                    """A longsword, engraved with the Excalibur"""),
    "book": Items("Book of Knowledge",
                 """This is the real treasure! As, an added bonus, you also get the treasure chest.
                 You have won the game!"""),
    "ball": Items("Crystal Ball",
                 """The treasure you seek is not the one you think."""),
    "light": Items("Star of Eärendil",
                  """This Star of Eärendil, our most beloved star.
                  May it be a light to you when all other lights go out."""),
    "poison": Items("Ricin",
                   """You have touched one of the most deadliest of poisons in the world,
                   sorry, but you are dead now. Goodbye..."""),
    "dragon egg": Items("Dragon Egg",
                       """You are the proud parent of a fierce and beautiful dragon.
                       Take care of this creature because it the only one of its kind"""),
    "magic wand": Items("Magic Wand",
                       """You have in your possession Merlin's wand.
                       Be careful where you point that thing! It is really powerful""")
}

room['foyer'].add_item(['sword', 'light'])
room['overlook'].add_item(['magic wand', 'ball'])
room['narrow'].add_item(['poison'])
room['treasure'].add_item(['dragon egg', 'treasure chest'])
room['secret'].add_item(['book'])