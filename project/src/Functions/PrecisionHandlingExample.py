import math

def main():
    var1 = 3.456345453


    print("\nFetching Precision")

    # trunc()
    print("trunc(): ", math.trunc(var1))

    # ceil()
    print("ceil(): ", math.ceil(var1))

    # floor()
    print("floor(): ", math.floor(var1))

    print("\nSetting Precision")


    # Using "%"
    print("\nUsing the % function")
    print("The value using 2 decimal places", "%.2f"%var1)
    print("The value using 3 decimal places", "%.3f" % var1)
    print("The value using 4 decimal places", "%.4f" % var1)
    print("The value using 5 decimal places", "%.5f" % var1)

    # Using format
    print("\nUsing the format function")
    print("The value using 2 decimal places", "{0:.2f}".format(var1))
    print("The value using 3 decimal places", "{0:.3f}".format(var1))
    print("The value using 4 decimal places", "{0:.4f}".format(var1))
    print("The value using 5 decimal places", "{0:.5f}".format(var1))

    # Using the round function
    print("\nUsing the round function")
    print("The value using 2 decimal places", round(var1, 2))
    print("The value using 3 decimal places", round(var1, 3))
    print("The value using 4 decimal places", round(var1, 4))
    print("The value using 5 decimal places", round(var1, 5))



if __name__ == '__main__':
    main()


'''
trunc
- Eliminate all decimal part of the float number
- Returns only Integer part

ceil 
- Fetches the least integer greater than given number

floor
- Fetch the least integer smaller than given number

'''