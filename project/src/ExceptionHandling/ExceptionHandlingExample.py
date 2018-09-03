def main():

    a = [1,2,3,4]


    # Exception Block is Blank
    try:
        print("Exception Block is Blank")
        print("Second Element is 2: ", a[1] == 2)
        print("Third Elememt is 1:", a[2] == 1)

        print("Last element is: ", a[4])

    except :
        print("Error occured")


    # IndexError

    # IOError

    # ZeroDivisionError
    try:
        print("\nException Block is ZeroDivisionError")
        a = 3
        b = a / 0

        print("b: ", b)

    except ZeroDivisionError:
        print("Error occured: Cannot divide by Zero")



    # TypeError


    pass


if __name__ == '__main__':
    main()


'''
Exception Handling

- Similar to Exeption handling in Java (i.e Try/catch)
- We need to define a try block then a "except" block which catches the error

Most common forms of Exceptions are:
- IndexError
- ImportError
- IOError 
- ZeroDivisionError
- TypeError.

'''