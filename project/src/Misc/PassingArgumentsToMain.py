#!/usr/bin/python

import sys

def passingArgumentsExample():
    print("# Arguments: ", len(sys.argv))
    print("Argument List: ", str(sys.argv))

if __name__ == '__main__':
    passingArgumentsExample()


'''
How to Execute
1. To to terminal and go this python exact location
2. Enter this command: python PassingArgumentsToMain.py "Hello World" arg2 "Tim Mans" arg4 "Michaela M"


What ? 
- We are now able to pass in arguments 
- Allows user some form of control on how the python script will operate

'''