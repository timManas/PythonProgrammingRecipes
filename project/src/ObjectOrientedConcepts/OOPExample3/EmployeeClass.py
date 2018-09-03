from project.src.ObjectOrientedConcepts.OOPExample3.PersonClass import Person


class Employee(Person):

    def isEmployee(self):
        return True

    def printAddress(self):
        print("Print Address: ", Person.address)

    pass