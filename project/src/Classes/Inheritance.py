# Classes
class Parent:
    'Parent Class Example'
    sharedAttribute = "Romero"
    __hiddenAttribute = "Hidden"
    parentAttribute = "parentAttribute"

    def __init__(self):
        print("Parent Class has been created")

    def parentMethod(self):
        print ("Parent Method Called")

    def setattr(self, attribute):
        Parent.parentAttribute = attribute              # Notice we still create our own attribute here

    def getParentAttr(self):
        print ("Getting Parent Attribute: ", self.parentAttribute)

    def getParentHiddenAttribute(self):
        print("Getting Hidden Parent Attribute: ", self.__hiddenAttribute)

class Child(Parent):                # Here we Inherit from Parent ...using the ()
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

    def getHiddenChildAttr(self):
        print("Getting Hidden Child Attribute: ", self.__childHiddenAttribute)


# Methods
def inheritanceExample():

    parent1 = Parent()
    child1 = Child()
    child2 = Child()

    # Print Child1 Methods
    print ("\n-----Child Methods")

    # Ex #1: Child calling Child Method
    child1.childMethod()

    # Ex#2: Child setting Attribute of Child Object
    child1.setChildAttribute("John")        # This is not private ...but STATIC since it is declared outside of constructor

    # Ex #3: Child adding additional attributes to object
    setattr(child1, "age", "20")
    setattr(child1, "__id", "1234")

    # Ex #4: Child changing attributes of itself
    child1.name = "Child1-Tim"
    child1.age = "50"
    print ("Child1 name: ", child1.name)
    print ("Child1 age: ", child1.age)

    # print ("Child1 __childHiddenAttribute: ", child1.__childHiddenAttribute)   # This WILL NOT work

    # Ex #5: Child access Hidden Element
    hiddentChildAtrr = child1.getHiddenChildAttr()
    print (hiddentChildAtrr)      # Why is this none ? Because "print() does NOT RETURN anything .. hence none

    # Ex #6: Child access PUBLIC attribute of Parent Object
    print("Inheriting fromt Parent: ", child1.parentAttribute)      # Notice child is able to access the parent public attribute
    print ("Child getting Parent attribute: ", child1.parentAttribute)        # How is this possible ? Because of Magic ... nah its because child inherits parents properties and methods
    print ("\nChild LastName: " + child1.sharedAttribute)


    # Ex: #7: Child access PRIVATE attribute of Parent Object
    print("Fetching parent Hidden attribute from child ")
    child1.getParentHiddenAttribute()

    # Ex #7b: Child accessing Prirvate attrivute of Parent object
    print ("Another way of Child accessing Hidden Attributes from Parent: ", child1._Parent__hiddenAttribute)


    # Example #8: Parent Element Print Parent Methods
    print ("\n-----Parent Methods")
    parent1.parentMethod()
    parent1.setattr("Tim")
    print ("Print Parent Hidden Attribute: ", parent1._Parent__hiddenAttribute)



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