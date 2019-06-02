from abc import ABC, abstractmethod

class Parent (ABC):

    @abstractmethod
    def printMethod(self):
        print("print Abstract Method")

class Parent2(ABC):
    def printMethod(self):
        print("print Parent2 Abstract Method")

class Concrete1Class(Parent):

    def printMethod(self):
        print("print Concrete 1 Class")


class Concrete2Class(Parent):

    def printMethod(self):
        print("Print Concrete2 Class ")


def main():
    shape = Concrete1Class()
    shape.printMethod()

    shape2 = Concrete2Class()
    shape2.printMethod()

    # shape3 = Parent()       #Error ... You cannot instantiate abstract class with abstract methods
    # shape3.printMethod()    #Solution 1. Make class Not Abstract or 2. Remove Abstract methods

    shape4 = Parent2()
    shape4.printMethod()    # Why is this working ? Because we removed the @abstractMethod

    pass


if __name__ == '__main__':
    main()



'''
Abstract classes  includes Attributes in addition to methods

How ? 
- Attach an "@abstractmethod"  to the Abstrct method

'''