from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = [Item("rock", "A large rock")]
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        returnString = f"---------------\n\n{self.name}\n\n{self.desc} \n\nItems in room: {[item.name for item in self.items]}\n\n---------------"
        returnString += f"\n\n[{self.getRoomExitString()}]\n\n"
        return returnString

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        if direction == "s":
            return self.s_to
        if direction == "e":
            return self.e_to
        if direction == "w":
            return self.w_to
        return None

    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)

    def addItemToRoom(self, name, desc):
        item = Item(name, desc)
        self.items.append(item)
        print(f"\n{name} has been added to {self.name}\n")
