def function1(arg1, *args):
    print("First Argument: ", arg1)

    for i in args:
        print("Argument: ", i)

    pass


def kArgsExampleFunction(**kwargs):
	if kwargs is not None:
		for key, value in kwargs.items():
			print ("%s == %s" %(key, value))



def main():

    # Example for *args
    function1("Hello", "World", "And", "Mr. ", "Tim")

    # Example of **kargs
    X = "Good"
    Y = "Morning"
    #kArgsExampleFunction(X, Y)                  # This will Fail, we need to define the key value pair in the brackets like below
    kArgsExampleFunction(X="Hello", Y="X")



if __name__ == '__main__':
    main()



'''
*args
- Allows you to pass any number of variables in the function


'''