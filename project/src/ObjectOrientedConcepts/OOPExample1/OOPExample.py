from project.src.ObjectOrientedConcepts.OOPExample1.Test import *  #Imports everything from Test.py

def main():

    obj1 = Test()
    obj1.function1()

    obj2 = Test2()
    obj2.function1()
    obj2.function2()
    obj2.function3()

    obj3 = Test3("Tim")
    obj3.function1("Tim")
    obj3.function2("Hello", "Mr.", "Tim")

    pass


if __name__ == '__main__':
    main()


'''

Object Oriented Programming


Note
- We can apply object oriented programming concepts ...to a limited degree
- We do not have to implement __init__ , it is called automatically when we create a new object
- But calling __init__ is good programming practice

Self
- Notice the self is there by DEFAULT
- We do not need to add self but is present BY DEFAULT
- Even if no argument is present, we still have "self" present by default
- similar to pointer in C++



'''