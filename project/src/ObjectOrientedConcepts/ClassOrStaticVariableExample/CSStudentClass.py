class CSStudent:

    stream = "CSE"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.__hiddenName = name + "_Hidden"

    def printCred(self):
        print("Name: ", self.name, "       Roll: ", self.roll)

    def printHiddentName(self):
        print("Hidden Name: ", self.__hiddenName)


    pass