def main():
    numericStringVal = "10010"
    stringVal = "Hello World"
    tupleVal = (('a', 1), ('f', 2), ('g', 3))

    charVal = "A"
    intVal = 56

    # Convert Any data type to int
    toInt = int(numericStringVal, 10)
    print("Converted datatype to int base 10: ", toInt)

    toInt = int(numericStringVal, 2)
    print("Converted datatype to int base 2: ", toInt)

    # Convert any data type to float
    toFloat = float(numericStringVal)
    print("Converted datatype to float: ", toFloat)

    # Character to Integer
    charToInt = ord(charVal)
    print("Converted Char to Int: ", charToInt)

    # Integer to hex
    intToHex = hex(intVal)
    print("Converted Int to Hex: ", intToHex)

    # Integer to octal
    intToOct = oct(intVal)
    print("Converted Int to Octal: ", intToOct)

    # String to a Tuple
    stringToTuple = tuple(stringVal)
    print("String to Tuple: ", stringToTuple)

    # String to a Set
    stringToSet = set(stringVal)
    print("String to Set: ", stringToSet)  # Remeber sets come in Random order

    # Convert to a List
    stringToList = list(stringVal)
    print("String to List: ", stringToList)

    # Convert tuple of order(key, value) to a dictionary
    tupleToDict = dict(tupleVal)
    print("Tuple (key, value) to Dictionary: ", tupleToDict)

    # Convert Integer to String
    intToString = str(intVal)
    print("Integer to String: ", intToString)

    # Convert real numbers to complex(real, imaginary)
    realToComplex = complex(1, 2)
    print("Real to Complex: ", realToComplex)


if __name__ == '__main__':
    main()
