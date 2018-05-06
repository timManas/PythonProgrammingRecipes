def setMain():
    print "::::::::: Set  ::::::::: "

    # Members
    stringSet = {"Hello", "World", "Goodbye"}
    numericSet = {2, -5, 6, -8, 4, 2, -7}
    mixedTypeSet = {"Lets", "Rule", "This", "World", 2, "Night", True}
    # nestedSet = {{"a", "b", "c", "d"}, ("x", 8, "y", 9), [1, 2, 3, 4]}          # Cannot have variable type Sets

    # Print Set
    print "Print Element #2 in String Set: " + stringSet[1]
    print "Print Element #3 in numberSet: ", numericSet[3]
    print "Print All Elements in mixTypeSet: ", mixedTypeSet[1:7]

    # How to create a new Set
    modifiedStringSet = {}
    print "\nCreate New Set: ", modifiedStringSet

    # Create a new Set with elements from another Set
    builtInModifiedStringSet = set(stringSet)
    print "\nCreate new Set from Set(): ", builtInModifiedStringSet

    # Append
    appendedSingle = stringSet  # This DOES NOT  create a new Set
    appendedSingle.append("Hiya")
    print "\nAppend(): ", appendedSingle

    appendSet = stringSet[:]
    appendSet.append(["Hi", "Mr.", "Tim"])  # Adds only at the End
    print "Append(): ", appendSet
    # appendedSingle = stringSet.append("Hiya")            # Error - This will not Work since append will return None

    # Extend
    newSet = ["You", "Can", "Do", "The", "Thing"]
    extendSet = stringSet[:]
    extendSet.extend(newSet)
    print "Extend(): ", extendSet

    # Difference between Append and Extend
    print "The Difference between Append and Extend ... Append will add the entire Set whole but extend will add each indiviual element into the Set"

    # Index
    print "\nIndex of 'Goodbye': ", stringSet.index(
        "Goodbye")  # str() is required since we are getting a int from 'index()'

    # Insert
    print "\nIf you want to add in the End of the Set, use Append. Otherwise use insert"
    insertSet = stringSet[:]
    insertSet.insert(0, "Start")
    print "Insert(0): ", insertSet

    insertSet.insert(len(insertSet), "End")
    print "Insert(Length): ", insertSet

    # Remove
    removeSet = insertSet[:]
    removeSet.remove("World")
    print "\nRemove('World'): ", removeSet

    # Pop
    print "\nYou can pop from the Last or Any position if you include the '[i]'"
    popSet = insertSet[:]
    print "Pop(): ", popSet.pop()
    print "Pop([2]): ", popSet.pop(2)

    # Count
    countSet = insertSet[:]
    countSet.append("Hello")
    countSet.append("Hello")
    print "Count(): ", countSet.count("Hello")

    # Sort
    sortSet = numericSet[:]
    print "\nSort(): ", sortSet.sort()  # RETURNS NONE

    # Sorted
    sortedSet = sorted(numericSet[:])
    print "Numeric Sorted(): ", sortedSet

    sortedSet = sorted(countSet[:])
    print "Alphabetic Sorted(): ", sortedSet

    sortedSet = sorted(mixedTypeSet[:])
    print "Mixed Sorted(): ", sortedSet



    # Reverse
    reverseSet = mixedTypeSet[:]
    reverseSet.reverse()
    print "\nReverse(): ", reverseSet

    # Slicing
    print "\nSlicing"
    print "a[start:end] # items start through end-1"
    print "a[start:]    # items start through the rest of the array"
    print "a[:end]      # items from the beginning through end-1"
    print "a[:]         # a copy of the whole array"
    print "Slice(3-6): ", mixedTypeSet[3:6]

    # Traversing a Set
    print "\nLooping using while Loop"
    i = 0
    while i < len(mixedTypeSet):
        print mixedTypeSet[i]
        i += 1

    print "\nLooping using For Loop Range "
    for i in range(len(mixedTypeSet)):
        print mixedTypeSet[i]

    print "\nLooping using For in"
    for values in mixedTypeSet:
        print values

    # Iterate Multiple Set at the same time...
    print "\nIterate Multiple Set ... Note: Index value is negated here"
    for values in zip(stringSet, mixedTypeSet):
        print values
    print "Notice how the Set only traverses until the shorter Set ends...Thats it =/ "

    # Filtering Sets
    from collections import Set
    filteredSet = Set(filter(lambda x: x > 0, numericSet))  # Fetch all positive numbers in Set
    print "Filtered(Only postive numbers): ", filteredSet
    filteredSet = Set(filter(lambda x: x != "Hello", stringSet))
    print "Filtered('Not Hello'): ", filteredSet

    # Sets as Stacks
    print "\nSet as Stacks"
    stackSet = mixedTypeSet[:]
    stackSet.append(False)
    stackSet.append("AppendMe")
    stackSet.append("999")
    print "StackSet(Append): ", stackSet

    stackSet.pop()
    stackSet.pop()
    stackSet.pop()
    print "StackSet(Pop x 3): ", stackSet

    # Sets as Queues
    print "\nSet as Queues"
    from collections import deque
    queueSet = deque(mixedTypeSet)
    queueSet.append("OMG")
    queueSet.append("BECKY")
    queueSet.popleft()
    print "Queue(Pop Left): ", queueSet

    # Clear
    del stringSet[:]
    print "Clear(using del[] StringSet): ", stringSet

    del mixedTypeSet[:]
    print "Clear(using del[] mixedTypeSet): ", mixedTypeSet


if __name__ == '__main__':
    setMain()