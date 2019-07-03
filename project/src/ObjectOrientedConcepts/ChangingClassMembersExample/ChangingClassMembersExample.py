# from project.src.ObjectOrientedConcepts.ChangingClassMembersExample.CSStudent import *   # This works
from project.src.ObjectOrientedConcepts.ChangingClassMembersExample import CSStudent    # This doesent work ?

def main():

    student1 = CSStudent("Tim", 12345)
    student2 = CSStudent("John", 346)
    student3 = CSStudent("Romero", 233424234234234)

    #Print Student Stream
    print("Stream of Student1: ", student1.stream)
    print("Stream of Student2: ", student2.stream)
    print("Stream of Student3: ", student3.stream)

    # Changing the member of the Class by referring to the CLASS NAME directly
    CSStudent.stream = "Mathematics"

    #Print Student Stream
    print("\nStream of Student1: ", student1.stream)
    print("Stream of Student2: ", student2.stream)
    print("Stream of Student3: ", student3.stream)

    # Now we only want Student#3 to be back to BIOLOGY
    student3.stream = "BIOLOGY"

    #Print Student Stream
    print("\nStream of Student1: ", student1.stream)
    print("Stream of Student2: ", student2.stream)
    print("Stream of Student3: ", student3.stream)



    pass


if __name__ == '__main__':
    main()


'''
Theres going to be instances when we want to change the static members for ALLLLLLL the classes 

If we want to change the instance of all the object which REFER to that class
- We must use the CLASS NAME instead of the object name

But if we want to change individual objects
- Then we must use the individual object name member



'''