from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", None, None, None, None, None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", None, None, None, None, None),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", None, None, None, None, None),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", None, None, None, None, None),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None, None, None, None, None),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Anduin", room["outside"], None)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
directions = {
    "n": "North",
    "s": "South",
    "e": "East",
    "w": "West"
}


def handle_direction(cmd):
    attr = cmd + '_to'

    if hasattr(player.room, attr) == False:
        return "The current room does not have attributes."

    getAttr = getattr(player.room, attr)
    print(getAttr)
    if getAttr is None:
        print(f"There is nothing to the {directions[cmd]}.")
        pass
    else:
        print(f'reached the else block {player}')
        player.room = getAttr
        print(f"{player.name} has moved to {player.room.name}")
        return getAttr


while True:
    print(player.room.name)
    print(player.room.desc)
    cmd = input("Please input n/s/e/w: ")
    if cmd == "q":
        print("Thank you for playing!")
        break
    elif cmd == "n" or "s" or "e" or "w":
        attr = handle_direction(cmd)
    else:
        print("\nInvalid input, please try again.\n")
