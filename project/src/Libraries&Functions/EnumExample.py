import enum

def main():

    # Print enum member using String
    print("Print enum member using String")
    print("Enum member: ", Animal.dog)
    print("Enum member: ", Animal.cat)


    # Print enum member using repr
    print("\nPrint enum member using repr")
    print("Enum member: ", repr(Animal.dog))
    print("Enum member: ", repr(Animal.lion))

    # Print the type of enum member  using type()
    print("\nPrint the type of enum member  using type()")
    print("Enum member: ", type(Animal.dog))
    print("Enum member: ", type(Animal.lion))

    # Print the name of the enum member using "name" keyword
    print("\nPrint the name of the enum member using 'name' keyword")
    print("Enum member: ", Animal.dog.name)
    print("Enum member: ", Animal.cat.name)

    # Iterate through an enum
    print("\nIterate through an enum")
    for Anim in Animal:
        print("Enum Member: ", Anim)

    # Use Enum to create a Dictionary or Set
    print("\nCreate a dict using an Enum")
    dict1 = {}
    dict1[Animal.dog.name] = "DOOOG"
    dict1[Animal.cat.name] = "CAAAT"
    print("enum to Dict: ", dict1)

    # Access enum memebers by value
    print("\nAccess enum memebers by value")
    print("Access the 1st Enum member: ", Animal(1))
    print("Access the 2nd Enum member: ", Animal(2))
    print("Access the 3rd Enum member: ", Animal(3))
    # print("Access the 3rd Enum member: ", Animal(4))      # Should cause Error

    # Access enum members by name
    print("\nAccess enum members by name")
    print("Access the 1st Enum member: ", Animal["dog"])
    print("Access the 2nd Enum member: ", Animal["cat"])
    print("Access the 3rd Enum member: ", Animal["lion"])
    #print("Access the 3rd Enum member: ", Animal["fish"])      # Should cause Error

    # Assign a var an Enum Member
    enumMember = Animal.cat

    print("Display Enum Key / value pair")
    # Display the name
    print("\nDisplay name: ", enumMember.name)

    # Display the value
    print("Display value: ", enumMember.value)


    # Compare num members by Identity
    print("\nCompare num members by Identity")
    if enumMember is Animal.dog:
        print("Correct: Enum member is a dog")
    else:
        print("Error: Not a dog")

    # Compare num members by Equality
    print("\nCompare enum members by Equality")
    if enumMember.value <= 1:
        print("Value is Smaller", enumMember.value)
    else:
        print("Value is Bigger: ", enumMember.value)


    pass

class Animal(enum.Enum):

    dog = 1
    cat = 2
    lion = 3


    pass


if __name__ == '__main__':
    main()


'''
Enumerators

Properties of Enum
1. Can be displayed as String or repr
2. Can be checked for their type using type()
3. You can use the "name" keyword to display the name of the enum member
4. Enums are iterable
5. Supports hashing


What ? 
- Are simply just values ..unline variables which have a varName and varValue... Enums are just members

How ?
- You can create Enums using classes

'''