class Test:

    def function1(self):
        print("Hello world")




class Test2:

    def __init__(self):
        print("\nInitializing ... calling __init")
        print("Called Constructor")
        print("We can do whatever we want here")


    def function1(self):
        print("\nHello Tim")

    def function2(self):
        print("Hello Goodlookin")

    def function3(self):
        print("Hello Sunshine")




class Test3:

    def __init__(self, x):
        print("\nCreating Test3 Object")
        print("Calling Constructor")
        print("Receiving value of x in constructor: ", x)


    def function1(self, x):
        print("\n Hello ", x)

    def function2(self, x, y, z):
        print("\n x: ", x, "    y: ", y, "      z: ", z)

    pass
