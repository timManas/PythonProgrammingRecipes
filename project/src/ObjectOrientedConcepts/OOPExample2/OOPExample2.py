from project.src.ObjectOrientedConcepts.OOPExample2.Test2 import *

def main():

    obj1 = Test2a()
    obj1.gender = "M"
    obj1.age = 31
    obj1.printIdentification()
    obj1.printAge()

    obj2 = Test2b(6951789, "World")
    # obj2.gender                       # Notice how we cant even set the internal properties age and gender
    # obj2.age
    obj2.printIdenticication();

    pass


if __name__ == '__main__':
    main()


'''
Private members 

What ? 
- We need to hide certain fields from the user and other components


How ? 
- We add the "__" in front of the variable ...ex ("__name")

Why ?
- To follow the SOLID Principle ...

Note
- Private methods are accessible outside their classes too, just Not easily accesible



'''