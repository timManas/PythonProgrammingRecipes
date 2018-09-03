from datetime import date

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def isAdult(self, page):
        return self.age > 18

    pass
