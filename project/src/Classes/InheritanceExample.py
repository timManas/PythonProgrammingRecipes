
class Parent:
    parentAttribute = "ParentAttribute"
    sharedAttribute = "Parent Shared Attribute"
    __hiddenParentAttribute = "Hidden Parent Attribute"

    def __init__(self):
        print("Parent Class has been Created")

    def __init__(self, value):
        self.parentAttribute = value

    def setParentAttribute(self, value):
        self.parentAttribute = value

    def setParentSharedAttribute(self, value):
        self.sharedAttribute = value

    def setParentHiddenAttribute(self, value):
        self.__hiddenParentAttribute = value

    def getParentAttribute(self):
        return self.parentAttribute

    def getParentSharedAttribute(self):
        return self.sharedAttribute

    def getParentHiddenAttribute(self):
        return self.__hiddenParentAttribute


class Child(Parent):
    childAttribute = "ChildAttribute"
    sharedChildAttribute = "Child Shared Attribute"
    __hiddenChildAttribute = "Hidden Child Attribute"

    def __init__(self):
        print("Child Class has been Created")

    def __init__(self, value):
        self.childAttribute = value

    def setChildAttribute(self, value):
        self.childAttribute = value

    def setChildSharedAttribute(self, value):
        self.sharedChildAttribute = value

    def setChildHiddenAttribute(self, value):
        self.__hiddenChildAttribute = value

    def getChildAttribute(self):
        return self.childAttribute

    def getChildSharedAttribute(self):
        return self.sharedChildAttribute

    def getChildHiddenAttribute(self):
        return  self.__hiddenChildAttribute


def main():
    print("Inheritance Exmaple")

    # Test #1 - This will Set the Parent Attribute
    parent1 = Parent("Parent1")
    parent2 = Parent("Parent2")
    print("Parent 1 attribute: ", parent1.getParentAttribute())
    print("Parent 2 attribute: ", parent2.getParentAttribute())

    # Test #2 - Change in Parent 1 will NOT affect Parent 2 Shared Attribute
    print("\nTest2 - Change in 1 Parent Obj will NOT affect the other Parent")
    parent1.setParentAttribute("Parent1 - A")
    print("Parent1 Attribute: ", parent1.getParentAttribute())
    print("Parent2 Attribute: ", parent2.getParentAttribute())

    # Test #3 - Share Characteristics for Parents should still be the same
    print("\nTest #3 - Shared Attributes for parents should still be the same")
    print("Parent1 Shared Attribute: ", parent1.getParentSharedAttribute())
    print("Parent2 Shared Attribute: ", parent2.getParentSharedAttribute())

    # Test #4 - Change Hidden Attribute Parent in 1 will NOT affect the other
    print("\nTest #4 - Changing Hidden Attribute for one will NOT affect the other")
    parent1.setParentHiddenAttribute("Hidden Parent Attribute - A")
    print("Parent1 Hidden Attribute: ", parent1.getParentHiddenAttribute())
    print("Parent2 Hidden Attribute: ", parent2.getParentHiddenAttribute())


    print("\nCreate Child Objects")
    child1 = Child("Child1")
    child2 = Child("Child2")
    print("Child 1 attribute: ", child1.getChildAttribute())
    print("Child 2 attribute: ", child2.getChildAttribute())

    # Test #5 - Change in Child1 will not affect Child2 Shared Attribute
    print("\nTest #5 - Change in child1 cannot affect Child2")
    child1.setChildAttribute("Child1 - A")
    print("Child1 Attribute: ", child1.getChildAttribute())
    print("Child2 Attribute: ", child2.getChildAttribute())

    # Test #6 - Child can access Parent Attributes
    print("\nTest #6 - Child can access Parent Attributes")
    print("Child1 can access Parent Attribute: ", child1.getParentAttribute())
    print("Child2 can access Parent Attribute: ", child2.getParentAttribute())

    # Test #7 - Child can access Hidden Attributes
    print("\nTest #7 - Child can access Parent Hidden Attributes")
    print("Child1 access Hidden Parent Attribute: ", child1.getParentHiddenAttribute())
    print("Child2 access Hidden Parent Attribute: ", child2.getParentHiddenAttribute())

    # Test #8 - Change in Child Parent Attribute will not affect the other
    print("\nTest # 8 - Change in Parent Attribute will not affect the other")
    child1.setParentAttribute("Parent attribute Modified in Child")
    print("Child1 Parent Attribute: ", child1.getParentAttribute())
    print("Child2 Parent Attribute: ", child2.getParentAttribute())

    print("Finished Example")

if __name__ == '__main__':
    main()


'''

Classes

What ? 

Why ? 


Notes
- Every method in Parent class is inherited on the Child Objects
- Remember Python does NOT use getter and setter methods 
- PYTHON does not really support Private members. It is up to the programmer to set these values carefully


'''