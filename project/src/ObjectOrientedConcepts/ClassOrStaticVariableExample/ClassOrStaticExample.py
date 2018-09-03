from project.src.ObjectOrientedConcepts.ClassOrStaticVariableExample.CSStudentClass import *

def main():

    ob1 = CSStudent("TimothyManas", 12345)

    # Print the Members
    ob1.printCred()

    # Print the hidden Members
    ob1.printHiddentName()

    # Prints Static variable
    print("Print Static Value: ", CSStudent.stream)

    pass


if __name__ == '__main__':
    main()


'''

Static

What ?
- Python doesent have a keyword static


Class variables = Variables which are assigned a value 
Instance variables = Variables which are assigned a value inside class methods 

How ? 
- In order to get a variable to become static, you must declare a varialbe INSIDE a class definition but OUTSIDE a method are class or static variables
ex. Variable "stream" ...inside class but outside method 

'''