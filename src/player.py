# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.currentRoom = room
        self.items = []

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(self.currentRoom)
        else:
            print("\nYou cannot move in that direction.\n")

    def addItemToPlayer(self, inputItem):
        roomItems = self.currentRoom.items
        for item in roomItems:
            if item.name == inputItem:
                self.items.append(item)
                roomItems.remove(item)
                item.onTake()
                return None
        print(f"\n{inputItem} is not in {self.currentRoom.name}\n")

    def dropItemFromPlayer(self, inputItem):
        roomItems = self.currentRoom.items
        for item in self.items:
            if item.name == inputItem:
                self.items.remove(item)
                roomItems.append(item)
                item.onDrop()
                return None
        print(f"\n{inputItem} is not in {self.name}'s inventory\n")
