from items import Item
from directions import room

inventory = {
    "treasure chest": Item("Treasure Chest",
    f"""This is the Treasure Chest. You will not have to work for the rest of your life,
there are enough spoils in these coiffers to make King Midas jealous but you cannot
take this treasure without another item.""",
    """xxx"""
    # """
    #                          ____...------------...____
    #                     _.-"` /o/__ ____ __ __  __ \o\_`"-._
    #                     .'     / /                    \ \     '.
    #                     |=====/o/======================\o\=====|
    #                     |____/_/________..____..________\_\____|
    #                     /   _/ \_     <_o#\__/#o_>     _/ \_   \
    #                     \_________       \####/       _________/
    #                     |===\!/========================\!/===|
    #                     |   |=|          .---.         |=|   |
    #                     |===|o|=========/     \========|o|===|
    #                     |   | |         \() ()/        | |   |
    #                     |===|o|======{'-.) A (.-'}=====|o|===|
    #                     | __/ \__     '-.\uuu/.-'    __/ \__ |
    #                     |====          .'.'^'.'.         ====|
    #                     |  _\o/   __  {.' __  '.} _   _\o/  _|
    #                     ''' -  '''''''''''''''''''''''''  -'''
    # """
    ),

    "sword": Item("Sword",
    f"""This special Sword. It is a longsword, engraved with the name Excalibur!""",
    """
                                                        &&
                                                        &&
     ______________________________________,___________&&&&              &
    /__________________________________________________&@@@@@@@@@@@@@@@@&&}
    \______________________________________ ___________&@@@@@@@@@@@@@@@@&&}
                                        `              &&&&              &
                                                        &&
                                                        &&

    """),

    "book": Item("Book of Knowledge",
    f"""This is the real treasure! The Book of Knowledge, holds all the secrets of the world.
As, an added bonus, you also get the treasure chest. You have won the game!""",
    """
              __...--~~~~~-._   _.-~~~~~--...__
            //               `V'               \\
           //                 |                 \\
          //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
         //__.....----~~~~._\ | /_.~~~~----.....__\\
        ====================\\|//====================
                            `---`

    """),

    "ball": Item("Crystal Ball",
    f"""The treasure you seek is not the one you think.""",
    """
         _...._
       .`      `.
      / ***      :
     : **         :
     :            :
      \          /
       `-.,,,,.-'
      (          )
       `-......-`
    """),

    "light": Item("Star of Eärendil",
    f"""This Star of Eärendil, our most beloved star. May it be a light to you
when all other lights go out.""",
    """
               .
          ---./|\.---
          '._/ | \_.'
        _.-'_'.|.'_'-._
         '-._.'|'._.-'
          .' \ | / '.
          ---'\|/'---
               '
    """),

    "poison": Item("Ricin",
    f"""You have touched Ricin, one of the most deadliest of poisons in the world, sorry,
but you are dead now. Goodbye...""",
    """
     mmm
     )-(
    (   )
    |   |
    |   |
    |___|
    """),

    "dragon egg": Item("Dragon Egg",
    f"""You have found the Dragon Egg. You are the proud parent of a fierce and beautiful dragon.
Take care of this creature because it the only one of its kind""",
    """
        .----.
     .'  \__ '.
    |   __|  _ :
    V\/(0I0\/ |/
       \ : /  '
       (oYo)
       /` `\__
     _|  _ Vuu: ,
    |uV\/ \| \_/|
    :      /\   :
      \   -'    /
      '-.___.-'  <>
     =        <;)
     """),

    "magic wand": Item("Magic Wand",
    f"""You have in your possession Merlin's wand.
Be careful where you point that thing! It is really powerful.""",
    """
    ------------ *
    """)
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