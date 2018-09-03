class myError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))






def main():

    try:
        # We explicitly want the exception to be raised
        raise(myError(3*2))

    except myError as error:
        print("A new exception occured: ", error.value)



if __name__ == '__main__':
    main()


'''
Rasie
- Allows developer to rasie a specific Exception. It explicityly invokes the Exception to be called


"... as Error"
- Allows us to define custom exceptions by the user.

How? 
1. Create a new class which inherits from the Exception Class
2. Defined exceptions as "error" in the except line 

'''