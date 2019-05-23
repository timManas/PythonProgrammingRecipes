def dictionaryMain():
    print("::::::::: Dictionaries  ::::::::: ")

    # How to create a Dictionary
    stringDic = {"key1": "value1",
                 "key2": "value2",
                 "key3": "value3",
                 "key4": "value4",
                 "key5": "value5"}


    numDic = { 1: 1,
               2: 2,
               3: 3,
               4: 4,
               5: 5}


    mixDic = {"key1": 1,
                2 : "value2",                  # Key is a number, value is a string
              "key3": [1,2,3,4,5],             # This is a key/List pair
              "key4": {"X", "Y", "Z"},          # This is key/Set pair
                5: True
              # [1,2,3,4]: "HelloWorld"           # This does not work since we cannot hash a list
    }

    # How to print a dictionary
    print("\nHow to print a dictionary")
    printDictionary("StringDic", stringDic)
    printDictionary("NumericDic", numDic)
    printDictionary("MixDic", mixDic)

    # How to copy a Dictionary -
    print("\nHow to Copy a Constructor")
    copyStringDic1 = dict(stringDic)
    copyStringDic2 = stringDic.copy()
    copyNumericDic3 = numDic.copy()

    printDictionary("copyStringDic1", copyStringDic1)
    printDictionary("copyStringDic2", copyStringDic2)
    printDictionary("copyNumericDic3", copyNumericDic3)


    # How to add values to a dictionary
    print("\nAdd values to dictionary")
    copyStringDic1["Hello"] = "World"
    copyStringDic1["Smoking Sunset"] = "Latch"
    copyStringDic1["OMG"] = "BECKY"
    printDictionary("copyStringDic1", copyStringDic1)

    # How to insert multiple items at once to dictionary
    copyStringDic1.update({"Update1": 1, "Update2":2, "Update3":3})

    # Check the length of a dictionary
    print ("\nLength of CopyStringDic1: ", len(copyStringDic1))

    # Check if Key Exist in dictionary
    print ("\nCheck if Key 'Hello' exists: ", "Hello" in copyStringDic1)
    print ("Check if Key 'Tim' exists: ", "Tim" in copyStringDic1)
    print ("Check if Key '5' exits: ", 5 in mixDic)

    # Check if Value Exists in dictionary
    print ("\nCheck if Value 'value2' exists: ", "value2" in stringDic.values())
    print ("Check if Value 'Tim' exits: ", "Tim" in stringDic.values())
    print ("Check if Value 'True' exits: ", True in mixDic.values())
    print ("Check if Value '[1,2,3,4,5]' exits: ", [1, 2, 3, 4, 5] in mixDic.values())


    # Get only Keys from dictionary
    stringDicKeys = stringDic.keys()
    print ("\nKeys only of stringDic: ", stringDicKeys)

    # Get only Values form dictionary
    stringDicValues = stringDic.values()
    print ("Values only of stringDic: ", stringDicValues)

    # Sort the dictionary
    print ("\nSorting the dictionary by Keys")
    for key in sorted(copyStringDic1):
        print ("%s: %s" % (key, copyStringDic1[key]))


    print ("\nSorting the dictionary by Values")


    # Remove A key/value pair
    print ("\nRemove Key'Hello'")
    del copyStringDic1["Hello"]
    del copyStringDic1["OMG"]
    del copyStringDic1["Smoking Sunset"]
    printDictionary("Removed 'Hello", copyStringDic1)




def printDictionary(title, dictionary):
    print ("\nNow printing: ", title)
    for key, val in dictionary.items():
        print (key, ": ", val)


if __name__ == '__main__':
   dictionaryMain()



'''
Dictionaries

What ? 
- Used to store a key/value pair. Similar to hashmap

Why ? 


Notes
- Dictionaries are unordered. Therefore

'''