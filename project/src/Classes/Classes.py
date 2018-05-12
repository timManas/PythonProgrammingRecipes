# Classes
class Employee:
    'Optional class documentation string'               # This line can be accessed by ClassName.__doc__
    empCount = 0                                        # Value can be shared from inside or outside the class. Can be accessed by Employee.empCount

    def __init__(self):                                 # Default Constructor
        self.name = "null"
        self.salary = "$0"
        Employee.empCount += 1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.id = ""
        Employee.empCount += 1

    def displayEmployeeCount(self):
        print ("Employee: ", self.name, "      Salary: " , self.salary, "    id: ", self.id)


# Methods
def classExample():

    # Create an Instance of a class
    #employee1 = Employee()                      # Why does this fail ?
    employee2 = Employee("Tim", "$70,000")
    employee3 = Employee("John", "$80,000")
    employee4 = Employee("Romero", "$90,000")


    # Access the Attributes
    employee2.displayEmployeeCount()
    employee3.displayEmployeeCount()
    employee4.displayEmployeeCount()


    # How to check if Attribute Exist
    print ("\nDoes attribute 'age' exists? ", hasattr(employee2, "age"))
    print ("Does attribute 'id' exists? ", hasattr(employee2, "id"))
    print ("Does attribute 'salary' exists?", hasattr(employee2, "salary"))

    # Get attribute if Attribute Exits
    print ("\nGet Attribute 'id' from Employee2: ", getattr(employee2, "id"))
    print ("Get Attribute 'salary' from Employee2: ", getattr(employee2, "salary"))
    #print "Get Attribute 'age' from Employee2: ", getattr(employee2, "age")     # This will cause a Error


    # Set attribute
    print ("\nSetting Attribute")
    setattr(employee3, 'id', "06951789")
    setattr(employee4, 'name',"George Soros")
    employee3.displayEmployeeCount()
    employee4.displayEmployeeCount()

    # Delete attribute
    print ("\nDeleting Attribute")
    delattr(employee2, 'name')
    # employee2.displayEmployeeCount()            # This is will cause an Error since we deleted the Attribute

    # Built in Attributes
    print ("\nEmployee.__doc__: ", employee2.__doc__)
    print ("Employee.__module__: ", employee2.__module__)

    # Class Inheritance


    # Overriding methods



    pass


if __name__ == '__main__':
    classExample()




'''

Classes

What ? 


How ? 



Notes
- We dont need to define all the member variables within the class. 
- We can declare the members within the constructor
- Anything declared outside the constructor is a static variable




'''