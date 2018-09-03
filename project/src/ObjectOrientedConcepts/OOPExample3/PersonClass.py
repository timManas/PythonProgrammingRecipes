class Person:

    __name = ""
    __id = ""
    __keyCode = "HelloWorld"
    address = "123 Rodeo Dr."

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id


pass