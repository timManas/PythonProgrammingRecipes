import collections

def main():

    # Instantiate a namedTuple
    Student = collections.namedtuple("Student", ["name", "age", "DOB"])     # Notice this is like the blue print for all student formats
    Worker = collections.namedtuple("Worker", ["name", "age", "ID"])
    print("Student NameTuple: ", Student)
    print("Student NameTuple: ", Worker)

    # Add values
    student1 = Student("Tim", "31", "1987")
    print("student1 NT: ", student1)

    # Access element using Index
    print("\nAccess Element by Index")
    print("Student1 Name: ", student1[0])
    print("Student1 DOB: ", student1[2])

    # Access elements using Key
    print("\nAccess Elements by Key")
    print("Student1 Name: ", student1.name)
    print("Student1 Age:", student1.age)
    print("Student1 DOB: ", student1.DOB)

    # Access element using getattr()
    print("\nAccess Elements by getAttr()")
    print("Student1 Name: ", getattr(student1, "name"))
    print("Student1 Age:", getattr(student1, "age"))
    print("Student1 DOB: ", getattr(student1, "DOB"))

    # Convert iterable (ex. list) to a named Tuple
    list1 = ["Vance", "100", "3442"]
    print("\nConvert list to NP using make(): ", Student._make(list1))

    # Convert namedTuple to an Ordered Dict()
    print("Convert NT to orderedDict: ", student1._asdict())

    # Convert dictionary to NT
    dict1 = {'name': "James", 'age': 19, 'DOB': '1391997'}
    print("Convert Dictionary to NT: ", Student(**dict1))           # Note: The ** converts dictionary to a tuple

    # Return all fields
    print("Return all fields: ", student1._fields)


    pass


if __name__ == '__main__':
    main()


'''
NameTuple 

REMEMBER ... THIS IS STILL A TUPLE ... NOT A DICTIONARY ... 
You can access the values like a dictionary but ultimately it is still ONE TUPLE WITH KEY/VALUE PAIRS as Elements


What ?  
- Light weight, easy to create objects
- Allows access to elements either by index or by key
- So you can fetch elements   like a list using the index or  like a map using key


How ?
- You need to instantiate it .... You need to create the blue print for it 
- Add Elements to it 

Note
- Similar to a Dictionary, you need to add key/value pairs to this object
- YOU SHOULD USE NAME TUPLES instead of Tuples anywhere object notation will make your code more readable

'''