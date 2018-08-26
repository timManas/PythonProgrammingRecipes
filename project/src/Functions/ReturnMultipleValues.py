class TestObject:

    def __init__(self):
        self.str = "HelloWorld"
        self.x = 10
        self.y = 20
        self.z = 30
        pass

    pass

def usingObject():

    print("\nReturn multiple values using Object")
    testObj = TestObject()
    print("Str: ", testObj.str)
    print("X: ", testObj.x)
    print("Y: ", testObj.y)
    print("Z: ", testObj.z)
    pass


def usingTuple():
    print("\nReturn multiple values using Tuple")
    str = "Hello World"
    X = 10
    Y = 20
    Z = 30

    return str, X, Y, Z                         # Notice how we can return multiple values in the "Return" statement


def usingList():
    print("\nReturn mutliple values using List")
    str = "Hello World"
    X = 10
    Y = 20
    Z = 30

    return [str, X, Y, Z]


def usingDict():
    print("\nReturn multiple values using Dictionary")
    dict1 = dict()
    dict1["str"] = "Hello World"
    dict1["X"] = 10
    dict1["Y"] = 20
    dict1["Z"] = 30
    return dict1


def main():
    usingObject()
    print(usingTuple())
    print(usingList())
    print(usingDict())

if __name__ == '__main__':
    main()