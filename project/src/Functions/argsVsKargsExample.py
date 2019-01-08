def function1(arg1, *args):  # Notice how we define the first argument here, but the rest is arbritary
    print("First Argument: ", arg1)

    for i in args:
        print("Argument: ", i)


def kArgsExampleFunction(**kwargs):  # Notice
    if kwargs is not None:
        for key, value in kwargs.items():
            print(key + " = " + value)


def main():
    # Example for *args
    function1("Hello", "World", "And", "Mr. ", "Tim")

    # Example of **kargs
    X = "Good"
    Y = "Morning"
    Z = "Tim"
    # kArgsExampleFunction(X, Y)                  # This will Fail, we need to define the key value pair in the brackets like below
    kArgsExampleFunction(X="Hello", Y="X", Z="JOY")


if __name__ == '__main__':
    main()

'''
Example #1: *args
- Allows you to pass any number of variables in the function


Example #2: **kwargs
- Allows an random # users to pass a key/value pair into the arguments 

'''
