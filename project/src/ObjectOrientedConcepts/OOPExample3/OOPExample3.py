from project.src.ObjectOrientedConcepts.OOPExample3.PersonClass import *
from project.src.ObjectOrientedConcepts.OOPExample3.EmployeeClass import *

def main():

    person1 = Person("Tim", 12345)
    print("Name: ", person1.getName(), "        Id: ", person1.getId())

    person2 = Employee("John", 50)
    print("\nName: ", person2.getName(), "        Id: ", person2.getId())
    print("IsEmployee: ", person2.isEmployee())


    # How to check if a class is a subclass of another ?
    print("\nCheck if Class is subclass of another using 'subclass''")
    print("Is Person Subclass of Employee: ", issubclass(Person, Employee))
    print("Is Employee Subclass of Person: ", issubclass(Employee, Person))

    print("\nCheck if Class is subclass of another using 'isInstance''")
    print("Is person1 is of type Person: ", isinstance(person1, Person))
    print("Is person1 is of type Employee: ", isinstance(person1, Employee))

    print("Is person2 is of type Person: ", isinstance(person2, Person))
    print("Is person2 is of type Employee: ", isinstance(person2, Employee))

    pass


if __name__ == '__main__':
    main()


'''
Note
- Python Supports multiple inheritance unlike Java or C++
- We can fetch hidden private methods using a get function which returns the private member ...similar to Java
- We can use subClass to check if a class is a subclass of another
- We can use isInstance to check if an object is an instance of a particular class

'''