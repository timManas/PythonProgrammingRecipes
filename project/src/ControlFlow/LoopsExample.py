def main():

    # Ex1: While loop
    count = 0
    while(count < 3):
        print("Count: ", count)
        count = count + 1

    # Ex2: For In Loop
    print("List Iteration")
    list1 = ["Hello", "World", "&", "Tim"]
    for i in list1:
        print("Element: ", i)

    print("\nTuple Iteration")
    tuple1 = ("I", "Love", "Programming")
    for i in tuple1:
        print("Tuple Element: ", i)

    print("\nIterate over each character in a String")
    string1 = "Hello Mr Tim, How Are You Today"
    for i in string1:
        print(i)

    print("\nDictionary Iteration")
    dict1 = dict()
    dict1["a"] = "Hello"
    dict1["b"] = "Mr. Tim"
    dict1["c"] = "Hi"
    for i in dict1:
        print("Key: ", i, "     Value: ", dict1[i])



    # Ex3: Continue Statement
    print("\nContinue Example")
    for letter in "HelloWorld":
        if letter == "e":
            continue

        print(letter)


    # Ex4: Break statement
    print("\nBreak Example")
    for letter in "HelloMrTim":
        if(letter == "T"):
            break

        print(letter)



if __name__ == '__main__':
    main()


'''
While Loop

Syntax:
while expression:
    statement(s)
    
For In Loop

Syntax:
for iterator_var in sequence:
    statements(s)


'''