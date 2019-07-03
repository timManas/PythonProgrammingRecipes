def main():

    # Simple Method
    a,b = 10, 20

    min = a if a < b else b
    print("Simple Method: ", min)

    #Using tuple
    # If true - display Hello
    # If false - display World
    print("Tuple Ternary Example: ", ("Hello", "World")[a < b])

    # Using Dictionary
    print("Dictionary Example: ", {True: "TrueX", False: "FalseX"}[a < b])

    # Using lambda ... dont forget the ()
    print("Lambda Example: ", (lambda: "B", lambda: "A")[a < b]())

if __name__ == '__main__':
    main()

'''
Ternary Operators

Syntax:
[on_true] if [expression] else [on_false] 


What ? 
Just a way to simply the if else statement into one line =/ ...thats it 



'''