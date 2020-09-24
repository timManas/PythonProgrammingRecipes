

class Singleton:
    __instance = None
    var = ""

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            __instance = Singleton()

        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance == None:
            Singleton.__instance = self  # Commenting causing an error. Functions cannot see setVar
        else:
            raise Exception("This class is a Singleton")


    def setVar(self, value):
        Singleton.var = value


def main():

    # Creating a Singleton using ()
    singleton1 = Singleton()
    singleton1.setVar("Modified #1")
    print("Singleton1: ", singleton1)
    print("Singleton1 Var: ", singleton1.var)

    # Creating a Singleton using getInstance()
    singleton2 = Singleton.getInstance()
    singleton2.setVar("Modified #2")
    print("\nSingleton2: ", singleton2)
    print("Singleton2 Var: ", singleton2.var)

    singleton3 = Singleton.getInstance()
    singleton3.setVar("Modified #3")
    print("\nSingleton3: ", singleton3)
    print("Singleton3 Var: ", singleton3.var)


if __name__ == '__main__':
    main()


'''
Singleton

What ? 
Only once instance of the class

How do i know its the same instance ?
1. Its referring to the same space in memory
2. var keeps changing despite having different instances

Note
- Notice we have getInstance actually creates the new instance
- init creates the self reference. Without this, app would fail
- We also have a static method called getInstance ...using @staticmethod




'''