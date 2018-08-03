def main():

    # Simple Method
    a,b = 10, 20

    min = a if a < b else b
    print("Simple Method: ", min)

    #Using tuple
    print("Tuple Ternary Example: ", ("Hello", "World")[a < b])

    # Using Dictionary
    print("Dictionary Example: ", {True: "True", False: "False"}[a < b])

    # Using lambda ... dont forget the ()
    print("Lambda Example: ", (lambda: "B", lambda: "A")[a < b]())

if __name__ == '__main__':
    main()

'''
Ternary Operators

Syntax:
[on_true] if [expression] else [on_false] 



'''