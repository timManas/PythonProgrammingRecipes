def simpleGeneratorFunction():
    print("Starting Yield 1")
    yield 1

    print("Starting Yield 2")
    yield 2

    print("Starting Yield 3")
    yield 3


def main():

    for value in simpleGeneratorFunction():
        print("Value: ", value)




if __name__ == '__main__':
    main()


'''
Yield ?

What ? 
- Suspends function calls and sends value back to user
- Retains in it's state and resumes where it left off 

Note
- When function resumes, we continues where it last left off in the function 

'''