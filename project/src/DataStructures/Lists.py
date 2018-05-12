def main():
    print("::::::::: Lists ::::::::: ")

    # Members
    stringList = ["Hello", "World", "Goodbye"]
    numbericList = [2, -5, 6, -8, 4, 2, -7]
    mixedTypeList = ["Lets", "Rule", "This", "World", 2, "Night", True]
    nestedList = [["a","b","c","d"],
                  ["x",8,"y",9],
                  [1,2,3,4]]


    # Print List
    print("Print Element #2 in String List: " + stringList[1])
    print("Print Element #3 in numberList: ", numbericList[3])
    print("Print All Elements in mixTypeList: ", mixedTypeList[1:7])
    print("Print all Elements in Nested List: ", nestedList[0:3])

    # How to create a new List
    modifiedStringList = []
    print("\nCreate New List: ", modifiedStringList)

    # Create a new list with elements from another list
    sliceModifiedStringList = stringList[:]
    print("New List With Slice[:]: ", sliceModifiedStringList)

    builtInModifiedStringList = list(stringList)
    print("Create new List from list(): ", builtInModifiedStringList)


    # Append
    appendedSingle = stringList                         # This DOES NOT  create a new List
    appendedSingle.append("Hiya")
    print("\nAppend(): ", appendedSingle)

    appendList = stringList[:]
    appendList.append(["Hi", "Mr.", "Tim"])                 # Adds only at the End
    print("Append(): ", appendList)
    # appendedSingle = stringList.append("Hiya")            # Error - This will not Work since append will return None

    # Extend
    newList = ["You", "Can", "Do", "The", "Thing"]
    extendList = stringList[:]
    extendList.extend(newList)
    print("Extend(): ", extendList)


    # Difference between Append and Extend
    print("The Difference between Append and Extend ... Append will add the entire List whole but extend will add each indiviual element into the list")

    # Index
    print("\nIndex of 'Goodbye': ", stringList.index("Goodbye")) #str() is required since we are getting a int from 'index()'

    # Insert
    print("\nIf you want to add in the End of the list, use Append. Otherwise use insert")
    insertList = stringList[:]
    insertList.insert(0, "Start")
    print("Insert(0): ", insertList)

    insertList.insert(len(insertList), "End")
    print("Insert(Length): ", insertList)

    # Remove
    removeList = insertList[:]
    removeList.remove("World")
    print("\nRemove('World'): ", removeList)

    # Pop
    print("\nYou can pop from the Last or Any position if you include the '[i]'")
    popList = insertList[:]
    print("Pop(): ", popList.pop())
    print("Pop([2]): ", popList.pop(2))

    # Count
    countList = insertList[:]
    countList.append("Hello")
    countList.append("Hello")
    print("Count(): ", countList.count("Hello"))

    # Sort
    sortList = numbericList[:]
    print("\nSort(): ", sortList.sort())                   # RETURNS NONE

    # Sorted
    sortedList = sorted(numbericList[:])
    print("Numeric Sorted(): ", sortedList)

    sortedList = sorted(countList[:])
    print("Alphabetic Sorted(): ", sortedList)

    #sortedList = sorted(mixedTypeList[:])          # Not supported when comparing a string and int
    #print("Mixed Sorted(): ", sortedList)

    #sortedList = sorted(nestedList[:])             # Not supported when comparing a string and int
    #print("NestedList Sorted(): ", sortedList)

    # Reverse
    reverseList = mixedTypeList[:]
    reverseList.reverse()
    print("\nReverse(): ", reverseList)

    # Slicing
    print("\nSlicing")
    print("a[start:end] # items start through end-1")
    print("a[start:]    # items start through the rest of the array")
    print("a[:end]      # items from the beginning through end-1")
    print("a[:]         # a copy of the whole array")
    print("Slice(3-6): ", mixedTypeList[3:6])


    # Traversing a List
    print("\nLooping using while Loop")
    i = 0
    while i < len(mixedTypeList):
        print(mixedTypeList[i])
        i+=1

    print("\nLooping using For Loop Range ")
    for i in range(len(mixedTypeList)):
        print(mixedTypeList[i])

    print("\nLooping using For in")
    for values in mixedTypeList:
        print(values)


    # Iterate Multiple list at the same time...
    print("\nIterate Multiple List ... Note: Index value is negated here")
    for values  in zip(stringList, mixedTypeList):
        print(values)
    print("Notice how the list only traverses until the shorter list ends...Thats it =/ ")

    # Filtering Lists
    filteredList = list(filter(lambda x : x > 0, numbericList))     # Fetch all positive numbers in List
    print("Filtered(Only postive numbers): ", filteredList)

    filteredList = list(filter(lambda x : x != "Hello", stringList))
    print("Filtered('Not Hello'): ", filteredList)

    # Lists as Stacks
    print("\nList as Stacks")
    stackList = mixedTypeList[:]
    stackList.append(False)
    stackList.append("AppendMe")
    stackList.append("999")
    print("StackList(Append): ", stackList)

    stackList.pop()
    stackList.pop()
    stackList.pop()
    print("StackList(Pop x 3): ", stackList)

    # Lists as Queues
    print("\nList as Queues")
    from collections import deque
    queueList = deque(mixedTypeList)
    queueList.append("OMG")
    queueList.append("BECKY")
    queueList.popleft()
    print("Queue(Pop Left): ", queueList)


    # Clear
    del stringList[:]
    print("Clear(using del[] StringList): ", stringList)

    del mixedTypeList[:]
    print("Clear(using del[] mixedTypeList): ", mixedTypeList)



# Main Class
if __name__ == '__main__':
    main();





'''


Lists 

What? 

How?


Notes:



Reference
http://thomas-cokelaer.info/tutorials/python/lists.html#list-comprehension


'''