# Implement a class to hold room information. This should have name and
# description attributes.

# n_to, s_to, e_to, w_to


class Room:
    def __init__(self, name, desc, items, n_to, s_to, e_to, w_to):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return f"From Room class: name is {self.name}, description is {self.desc}"

# , North: {self.n_to}, North: {self.n_to}, South: {self.s_to}, East: {self.e_to}, West: {self.w_to}"
