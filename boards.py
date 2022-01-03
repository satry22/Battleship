from ships import shipOne

class Board():
    """
    Owner, ships, size, coordinates
    """

    def __init__(self, owner):
        self.owner = owner

test = Board('Sara')
print(test.owner)
print(shipOne.name)
