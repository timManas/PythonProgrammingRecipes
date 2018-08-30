import math

def main():

    num1 = 3.563247

    # ceil()
    print("ceil(): ", math.ceil(num1))

    # floor()
    print("floor(): ", math.floor(num1))

    # fabs()
    print("fabs(): ", math.floor(num1))

    # factorial()
    print("factorial(): ", math.factorial(3))

    # copysign()
    print("copysign(): ", math.copysign(10, -3.323))

    # gcd()
    print("gcd(): ", math.gcd(12, 9))




if __name__ == '__main__':
    main()


'''
ceil() - Gets the highest integer number ..aka it rounds up

floor() - Gets the lowest integer number ...aka it rounds down

fabs() - Returns the absolute value of a number ... aka gets rid of the decimal

factorial() - Generates the factorial sum. Must only be integer number ...no decimals

copysign(a,b) - Copys the sign of b and applies it to a

gcd(a,b) - Fetches the greated common denominator between two numbers

'''