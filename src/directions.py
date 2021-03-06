from room import Room
from items import Item

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness.
Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",
                    """The narrow passage bends here from west to north.
The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                    """You've found the long-lost treasure chamber!
Search the room to find what riches await!  The only exit is to the south."""),

    'secret':  Room("Secret Chamber",
                    """You have entered a secret chamber, who knows what you will find in here.""")
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['overlook'].n_to = room['secret']
room['secret'].s_to = room['overlook']
