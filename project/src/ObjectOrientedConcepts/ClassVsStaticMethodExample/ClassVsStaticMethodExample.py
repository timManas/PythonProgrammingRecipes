from project.src.ObjectOrientedConcepts.ClassVsStaticMethodExample.Person import *

def main():

    person1 = Person("Tim.M", 31)
    person2 = Person.fromBirthYear("John.M", 2008)

    print("Is Person1 an Adult: ", Person.isAdult(person1, 31))
    print("Is Person2 an Adult: ", Person.isAdult(person2, 13))


if __name__ == '__main__':
    main()


'''
Class Method

What ?
- Recieves "cls" as an implicit 1st argument
- Bound to the class and not the OBJECT of the class
- Have access to the State of the class 
- Pointer points to the class and not the object instance
- Can modify the state of the class ...which would be applicable to ALL  the instances of all classes 

Static Method

What ? 
- Method which is bound to class and NOT the object
- Cannot access or modify Class state


Difference between both 
- Class method takes in cls as 1st parameters while static methods do not need any specific parameters
- Class methods can modify the state of the class while static cannot
- Static methods are more utility classes
- We use @classmethod declarator to create a class method




'''