# Classes
class Parent:
    'Parent Class Example'
    sharedAttribute = "Romero"
    __hiddenAttribute = "Hidden"

    def __init__(self):
        print "Parent Class has been created"

    def parentMethod(self):
        print "Parent Method Called"

    def setattr(self, attribute):
        Parent.parentAttribute = attribute              # Notice we still create our own attribute here

    def getAttr(self):
        print "Getting Parent Attribute: ", self.parentAttribute

class Child(Parent):
    'Parent Class Example'
    childAttribute = "Child Attribute"
    __childHiddenAttribute = "Hidden_Child"

    def __init__(self):
        print "Child Class have been created"

    def childMethod(self):
        print "Child Method Called"

    def setattr(self, attribute):
        Child.childAttribute = attribute

    def getAttr(self):
        print "Getting Child Attribute: ", self.childAttribute


# Methods
def inheritanceExample():

    parent1 = Parent()
    child1 = Child()
    child2 = Child()

    # Print Child1 Methods
    print "\n-----Child Methods"
    child1.childMethod()
    child1.setattr("John")
    child1.getAttr()

    # Print Child2 Methods
    print "\n-----Child Methods"
    child2.childMethod()
    child2.setattr("Michaela")
    child2.getAttr()


    # Print Parent Methods
    print "\n-----Parent Methods"
    parent1.parentMethod()
    parent1.setattr("Tim")
    parent1.getAttr()
    print "Print Parent Hidden Attribute: ", parent1._Parent__hiddenAttribute




    print "Child getting Parent attribute: ", child1.parentAttribute        # How is this possible ?
    print "\nChild LastName: " + child1.sharedAttribute
    print "Access Hidden Attributes: ", child1._Parent__hiddenAttribute


# Main
if __name__ == '__main__':
    inheritanceExample()