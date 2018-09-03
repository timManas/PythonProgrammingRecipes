class Test2a:
    __id = 12345
    __name = "Tim"
    gender = ""
    age = ""

    def printIdentification(self):
        print("\nId: ", self.__id, "     Name: ", self.__name)

    def printAge(self):
        print("Age: ", self.age, "      Gender: ", self.gender)

    pass

class Test2b:
    __id = ""
    __name = ""
    __gender = ""
    __age = ""

    def __init__(self, x, y):
        self.__id = x
        self.__name = y

    def printIdenticication(self):
        print("\nId: ", self.__id, "      Name: ", self.__name)

    def printAge(self):
        print("Age: ", self.__age, "      Gender: ", self.__gender)