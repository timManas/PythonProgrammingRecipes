# Classes
class Parent:
    'Parent Class Example'
    sharedAttribute = "Romero"
    __hiddenAttribute = "Hidden"

    def __init__(self):
        print("Parent Class has been created")

    def parentMethod(self):
        print ("Parent Method Called")

    def setattr(self, attribute):
        Parent.parentAttribute = attribute              # Notice we still create our own attribute here

    def getParentAttr(self):
        print ("Getting Parent Attribute: ", self.parentAttribute)

class Child(Parent):
    'Parent Class Example'
    childAttribute = "Child Attribute"
    __childHiddenAttribute = "Hidden_Child"

    def __init__(self):
        print ("Child Class have been created")

    def childMethod(self):
        print ("Child Method Called")

    def setChildAttribute(self, attribute):
        Child.childAttribute = attribute


    def getChildAttr(self):
        print ("Getting Child Attribute: ", self.childAttribute)


# Methods
def inheritanceExample():

    parent1 = Parent()
    child1 = Child()
    child2 = Child()

    # Print Child1 Methods
    print ("\n-----Child Methods")
    child1.childMethod()
    child1.setChildAttribute("John")        # This is not private ...but STATIC since it is declared outside of constructor
    setattr(child1, "age", "20")            # REMEMBER THIS IS PRIVATE
    child1.name = "Child1-Tim"
    child1.age = "50"
    print ("Child1 name: ", child1.name)
    print ("Child1 age: ", child1.age)

    # Print Child2 Methods
    print ("\n-----Child Methods")
    child2.childMethod()
    child2.setChildAttribute("Michaela")    # This is not private ...but STATIC since it is declared outside of constructor
    setattr(child2, "id", "06951789")            # REMEMBER THIS IS PRIVATE
    child2.name = "Child2-John"
    child2.age = "100"
    print("Child2 name: ", child2.name)
    print("Child2 id: ", child2.id)
    print("Child2 age: ", child2.age)

    # Print Parent Methods
    print ("\n-----Parent Methods")
    parent1.parentMethod()
    parent1.setattr("Tim")
    print ("Print Parent Hidden Attribute: ", parent1._Parent__hiddenAttribute)




    print ("Child getting Parent attribute: ", child1.parentAttribute)        # How is this possible ?
    print ("\nChild LastName: " + child1.sharedAttribute)
    print ("Access Hidden Attributes: ", child1._Parent__hiddenAttribute)


# Main
if __name__ == '__main__':
    inheritanceExample()

'''

Classes

What ? 

Why ? 


Notes
- Remember Python does NOT use getter and setter methods 


'''