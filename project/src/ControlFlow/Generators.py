def main():

    # Generator Function Example
    print("Generator Function")
    for i in generatorExample():
        print("i: ", i )


    # Generator Object Example
    print("\nGenerator Object")
    x = generatorExample()

    print(x.__next__())
    print(x.__next__())
    print(x.__next__())


def generatorExample():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    main()


'''
Generators Function 

What ? 
- Can come in the form of a function
- Defined like a function but whenever it needs to generate a value, it uses "yield" instead of "return"
- If the body of the function contains "yield", the function automatically becomes a generator


Generator Object

What ? 
- Generator function return generator Objects
- Generator objects are called by
    - using the next method on the G.O 
    - using G.O in for loop
    
    
Why do we use this ? 
- Stream processing or handling large input files
- Able to segregate different files since we split them up into different parts
    

'''