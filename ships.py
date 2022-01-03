class Ship():
    """
    name, size, 
    """

    def __init__(self, size):
        self.size = size
        self.name = self.checkName()

    def checkName(self):
        if self.size == 2:
            return "destroyer"
        if self.size == 3:
            return "maria"
        if self.size == 4:
            return "submarine"


shipOne = Ship(3)
shipTwo = Ship(2)

print('string')