def setMain():
    print("::::::::: Set  ::::::::: ")

    # Members
    stringSet = {"Hello", "World", "Goodbye"}
    numericSet = {2, -5, 6, -8, 4, 2, -7}
    mixedTypeSet = {"Lets", "Rule", "This", "World", 2, "Night", True}
    # nestedSet = {{"a", "b", "c", "d"}, ("x", 8, "y", 9), [1, 2, 3, 4]}          # Cannot have variable type Sets

    # Print Set - The following will raise an ERROR !!!
    print("String Set: ", stringSet)
    # print("Print Element #2 in String Set: ", stringSet[1])     # This will not work since you set objects cannot be indexed

    # Traverse/Iterate over Sets
    print("\nIterating over a Set")
    for value in numericSet:
        print(value)

    # How to create a new Set
    modifiedStringSet = {}
    print("\nCreate New Set: ", modifiedStringSet)

    # Create a new Set with elements from another Set
    builtInModifiedStringSet = set(stringSet)
    print("\nCreate new Set from Set(): ", builtInModifiedStringSet)

    # Add
    addSingle = stringSet  # This DOES NOT  create a new Set
    addSingle.add("Hiya")      # .add() will add it random position on the set
    print("\nadd(): ", addSingle)

    # appendSet = stringSet[:]        # Error - This will not work
    # appendedSingle = stringSet.append("Hiya")            # Error - This will not Work since append will return None



    # Remove
    removeSet = set(stringSet)
    removeSet.remove("World")
    print("\nRemove('World'): ", removeSet)

    # Pop
    print("\nYou can pop from the Last or Any position if you include the '[i]'")
    popSet = set(mixedTypeSet)
    print("Pop(): ", popSet.pop())

    # Sorted
    sortedSet = sorted(numericSet)
    print("Numeric Sorted(): ", sortedSet)

    sortedSet = sorted(stringSet)
    print("Alphabetic Sorted(): ", sortedSet)

    # sortedSet = sorted(mixedTypeSet)      # Does not work since we can only compare similar types



    # Iterate Multiple Set at the same time...
    print("\nIterate Multiple Set ... Note: Index value is negated here")
    for values in zip(stringSet, mixedTypeSet):
        print(values)
    print("Notice how the Set only traverses until the shorter Set ends...Thats it =/ ")


    # Sets as Stacks
    print("\nSet as Stacks")
    stackSet = set(mixedTypeSet)
    stackSet.pop()
    stackSet.pop()
    stackSet.pop()
    print("StackSet(Pop x 3): ", stackSet)

    # Sets as Queues
    print("\nSet as Queues")
    from collections import deque
    queueSet = deque(mixedTypeSet)
    queueSet.append("OMG")
    queueSet.append("BECKY")
    queueSet.popleft()
    print("Queue(Pop Left): ", queueSet)

    # Clear
    stringSet.clear()
    stringSet.add("FirstElement")
    print("Clear(using del[] StringSet): ", stringSet)


    mixedTypeSet.clear()
    print("Clear(using del[] mixedTypeSet): ", mixedTypeSet)


if __name__ == '__main__':
    setMain()