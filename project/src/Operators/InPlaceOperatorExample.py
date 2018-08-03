import operator

def main():

    x,y = 5,6
    a,b = 7,8

    # Incremental Add : x += y
    iAdd = operator.iadd(5, 6)
    print("iAdd: ", iAdd)

    # Incremental Concatenate
    iConCat = operator.iconcat("Hello", "World")
    print("iConCat:", iConCat)

    # Incremental Subtraction
    iSub = operator.isub(5, 6)
    print("iSub: ", iSub)

    # Incremental Multiplication
    iMul = operator.imul(5,6)
    print("iMul:", iMul)

    # Incremental Division
    iDiv = operator.itruediv(10, 5)
    print("iDiv: ", iDiv)

    # Incremental Modulus
    iMod = operator.imod(10, 6)
    print("iMod: ", iMod)

    # Incremental Exponential
    iPow = operator.ipow(2, 4)
    print("iPow: ", iPow)

if __name__ == '__main__':
    main()

'''
InPlace Operator

What ? 
- Behave similar to Normal operator except that they perform the action and assign the value to the fitst argument

Why ? 
- Well i think its because Python does NOT have ++, hence in order to increment, they would need to use inplace operator 

'''