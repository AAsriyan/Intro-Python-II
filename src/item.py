class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def onTake(self):
        print(f"\nYou have picked up {self.name}\n")

    def onDrop(self):
        print(f"\nYou have dropped {self.name}\n")
