


def main():

    list1 = [1,2,3,4]
    tuple1 = tuple(list1)

    # function1(list1)          # This line should fail because we are passing in a list ...which is just one value
    # function1(tuple1)         # This line will fail,.. why ? list1 is tuple but represent only one argument which is "a"

    # UnPacking
    function1(*list1)

    # Packing
    function2(10,20,30,40)
    function2("x", "y", "z")

# This is packing with a set number of Arguments
def function1(a,b,c,d):
    print("UnPacking Example Valus: ", a,b,c,d)


# Packing with Arbritrary number of Arguments
def function2(*args):

    for i in range(0, len(args)):
        print(args[i])

if __name__ == '__main__':
    main()

'''

Packing 

What?
- When we dont know exactly how many arguments to pass in a function -> we use packing

How ?
- In the function declaration, we use the *args are the arguemnt ...ex. function2(*args)
- We still pass in the argument same as always but the function is take in arbritray number of arguments 


UnPacking

What ? 
- Unpacks a list so it values can be passed off as parameters

How ?
- We use the * in the function call ...ex. function1(*list)


What is the differentce ? 
Packing -> * is on the function argument 
Unpacking -> * is on the function call


'''