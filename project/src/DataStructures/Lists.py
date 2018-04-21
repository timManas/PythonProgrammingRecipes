
def main():

    # Members
    stringList = ["Hello", "World", "Goodbye"]
    numbericList = [2, 5, 6, 8, 4, 2, 7]
    mixedTypeList = ["Lets", "Rule", "This", "World", 2, "Night", True]
    nestedList = [[1,2,3,4],
                  ["a","b","c","d"],
                  ["x",8,"y",9]]


    # Print List
    print "Print Element #2 in String List: " + stringList[1]
    print "Print Element #3 in numberList: ", numbericList[3]            # Notice how we had to use "," for numeric values
    print "Print All Elements in mixTypeList: ", mixedTypeList[1:7]
    print "Print all Elements in Nested List: ", nestedList[0:3]

    # How to create a new List
    modifiedStringList = []
    print "Create New List: " + ".".join(modifiedStringList)

    # Create a new list with elements from another list
    sliceModifiedStringList = stringList[:]
    print "New List With Slice[:]: " + ".".join(sliceModifiedStringList)

    builtInModifiedStringList = list(stringList)
    print "Create new List from list(): " + ".".join(builtInModifiedStringList)
    

    # Append
    appendedSingle = stringList                         # This DOES NOT  create a new List
    appendedSingle.append("Hiya")
    print "Append(): " + ",".join(appendedSingle)

    appendList = stringList[:]
    appendList.append(["Hi", "Mr.", "Tim"])
    #print "Append(): " + "".join(appendList)            # Error - Expected String, List found
    print "Append(): " + ",".join(str(v) for v in appendList)       #Join connects elements inside of a list of String, NOT ints

    # appendedSingle = stringList.append("Hiya")            # Error - This will not Work since append will return None

    # Extend
    newList = ["You", "Can", "Do", "The", "Thing"]
    extendList = stringList[:]
    extendList.extend(newList)
    print "Extend(): " + ",".join(str(v) for v in extendList)

    # Difference between Append and Extend
    print "The Difference between Append and Extend ... Append will add the entire List whole but extend will add each indiviual element into the list"

    # Index


    # Insert


    # Remove


    # Pop


    # Count


    # Sort


    # Reverse


    # Slicing


    # Traversing a List


    # Filtering Lists


    # Lists as Stacks


    # Lists as Queues


    # How to Copy a List


    # Inserting items into a Sorted List


    # Reverse a List



    # Clear







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