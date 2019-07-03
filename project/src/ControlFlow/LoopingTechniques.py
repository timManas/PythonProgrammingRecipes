def main():

    # Ex1: Iterate using Enumerator
    print("Iterate using Enumerator")
    for key, value in enumerate(["Hello", "World", "Mr.", "Tim"]):
        print("Key: ", key, "   Value: ", value)

    # Ex2: Iterate using zip
    print("\nIterate using zip")
    questions = ["name", "colour", "shape"]
    answers = ["apple", "red", "circle"]

    for question, answer in zip(questions, answers):
        print("What is your ", question, " ? ", "   Answer: ", answer)

    # Ex3: Iterate using items()
    print("\nIterate using iterItem()")
    dict1 = {"a": "Hello", "b": "World", "c": "Mr", "d": "Tim"}
    for key, value in dict1.items():
        print("Key: ", key, "       value: ", value)



    # Ex4: Using sorted()
    print("\nUsing sorted()")
    list1 = [2,5,3,7,4,6,22,16,1]
    for i in sorted(list1):
        print(i)

    # Ex5: Using sorted() when we have duplicates
    print("\nUsing sorted() when we have duplicates")
    list2 = [1,2,5,2,5,2,5,2,5,2,5,6,8,3,2]
    for i in sorted(set(list2)):
        print(i)


    # Ex6: Using reversed()
    print("\nUsing reversed()")
    for i in reversed(list1):
        print(i)





if __name__ == '__main__':
    main()


'''

Why ?
- Very fast
- Reduces coding effort
- Makes the code more concise


enumerate() - used to loop through the container priting the index number with the value
zip() - combines two similar containers (list-list or dict-dict) while printing the values sequentially
      - Loop only exists only till small container ends
items() - Fetches the key value pair.
        - Very time consuming 
        - Takes alot of memory
        
sorted() - ONLY sorts when printed out
         - DOES NOT ACTUALLY sort the container     
         
reverse() - Prints the value in reverse order         
              

'''