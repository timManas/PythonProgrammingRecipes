import copy


def printAllList(list1, list2, list3):

    print("List1: ", list1)
    print("List2: ", list2)
    print("List3: ", list3)
    pass


def main():

    list1 = [2, 3, 5, [3, 5, 9], 3, 7]
    list2 = list1
    list3 = copy.deepcopy(list1)

    print("Original list")
    printAllList(list1, list2, list3)

    # Modify List3
    print("\nModified List3 only")
    list3[3][0] = 100
    printAllList(list1, list2, list3)

    #Modify List2
    print("\nModified List2")
    list2[2] = 50
    printAllList(list1, list2, list3)
    print("Notice List2 is only a Shallow copy, hence When list2 is modified list1 is also affected")

    # Modify List1
    print("\nModified List2")
    list2[0] = 90
    printAllList(list1, list2, list3)
    print("Any changes in List1, appears in list 2 since List2 is a shallow copy")

    pass


if __name__ == '__main__':
    main()


'''
Deep Copy ? 

What ? 
- Allows the developer to create a deep copy of an object
- This deep copy object has a compeletely new object with completely new references


Shallow Copy ? 

What ? 
- Changes to one reference, gets affected in the original copy 

Why ? 
- The second object is just a reference to the original object (LIST1) 

How ?
- Import copy
- Then use copy.deepcopy() to create a deep copy object ...Very simple

'''