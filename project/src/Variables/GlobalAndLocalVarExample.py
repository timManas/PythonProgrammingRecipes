var = "CONQUER"

def main():
    printExample1()
    printExample2()
    printExample3()

def printExample1():
    var = "Hello World"
    print("Printing Local Var: ", var)

def printExample2():
    print("Printing External Var: ", var)


def printExample3():
    global var
    var = "Hello World"
    print("Printing Local Var: ", var)

if __name__ == '__main__':
    main()