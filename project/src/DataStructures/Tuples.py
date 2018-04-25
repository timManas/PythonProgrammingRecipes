def main():
    print "::::::::: Tuples and Sequences ::::::::: "
    print "Tuples are immutable. Once you define it, it cannot be deleted or modified (add, edit, etc)"


    # How to create a Tuple # 1
    stringTuple = "Hello", "World", "Goodbye", "Mr.", "World"
    numericTuple = 1,2,3,4,5

    # How to create a Tuple # 2
    mixedTuple = ("Lets", "Rule", "This", "World", 2, "Night", True)
    nestedTuple = (("a", "b", "c", "d"),
                  ["x", 8, "y", 9],                                     # Notice this is a Tuple
                  [1, 2, 3, 4])

    # Print Tuple
    print "Print Element #2 in String Tuple: " + stringTuple[1]
    print "Print Element #3 in numberTuple: ", numericTuple[3]
    print "Print All Elements in mixTypeTuple: ", mixedTuple[1:7]
    print "Print all Elements in Nested Tuple: ", nestedTuple[0:3]

    # How to create a new Tuple
    modifiedStringTuple = ()
    print "\nCreate New Tuple: ", modifiedStringTuple

    # Create a new Tuple with elements from another Tuple
    sliceModifiedStringTuple = stringTuple[:]
    print "New Tuple With Slice[:]: ", sliceModifiedStringTuple

    builtInModifiedStringTuple = tuple(stringTuple)
    print "Create new Tuple from Tuple(): ", builtInModifiedStringTuple

    # Index
    print "\nIndex of 'Goodbye': ", stringTuple.index("Goodbye") #str() is required since we are getting a int from 'index()'

    # Count
    countTuple = stringTuple[:]
    print "Count(): ", countTuple.count("World")

    # Slicing
    print "\nSlicing"
    print "a[start:end] # items start through end-1"
    print "a[start:]    # items start through the rest of the array"
    print "a[:end]      # items from the beginning through end-1"
    print "a[:]         # a copy of the whole array"
    print "Slice(3-6): ", mixedTuple[3:6]


    # Traversing a Tuple
    print "\nLooping using while Loop"
    i = 0
    while i < len(mixedTuple):
        print mixedTuple[i]
        i+=1

    print "\nLooping using For Loop Range "
    for i in range(len(mixedTuple)):
        print mixedTuple[i]

    print "\nLooping using For in"
    for values in mixedTuple:
        print values


    # Filtering Tuples
    filteredTuple = tuple(filter(lambda x : x > 0, numericTuple))     # Fetch all positive numbers in Tuple
    print "Filtered(Only postive numbers): ", filteredTuple

    filteredTuple = tuple(filter(lambda x : x != "Hello", stringTuple))
    print "Filtered('Not Hello'): ", filteredTuple


# Main Class
if __name__ == '__main__':
    main()