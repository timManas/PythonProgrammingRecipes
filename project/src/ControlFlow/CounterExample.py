from collections import Counter

def main():

    # Initialize using sequence of items
    counter1 = Counter(['B','B','A','B','C','A','B','B','A','C'])

    # Initialize using dictionary
    counter2 = Counter({"B": 5, "A": 3, "C":2})

    # Initialize using arguments
    counter3 = Counter(B=5, A=3, C=2)              #This will still work

    print("Initialize using sequence of Items: ", counter1)
    print("Initialize using dictionary: ", counter2)
    print("Initialize using arguments: ", counter3)


    # Update
    counter1.update(["B", "A", "C", "C"])
    print("Update counter1: ", counter1)            # Notice it ADDS ON TOP OF IT ... does not REPLACE IT
    



if __name__ == '__main__':
    main()


'''
Counter 

What ? 
- Objects which hold other objects (i.e its a counter for objects of similar types
- Provide a way to access objects and iterate over them
- Subclass of "Dict" (Dictionary)



'''