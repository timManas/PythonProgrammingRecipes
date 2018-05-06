def stringMain():
    print "::::::::: Strings ::::::::: "

    # Create new String
    longText = "Lorem ipsum dolor sit amet, consectetur Lorem elit. Lorem in lobortis felis, nec fermentum nibh. Donec bibendum placerat ex, eu pharetra velit efficitur quis. Vestibulum in in nec massa ultrices pretium. Ut euismod laoreet fermentum. Aliquam rhoncus mi purus, in blandit lectus condimentum eu. Nullam sed turpis consequat, semper nisl nec, mollis odio. Curabitur gravida augue ac purus laoreet fermentum."
    alphaString = "hello world"
    numericString = "1, 2, 3, 4, 5"
    alphaNumericString = "HelloWord1234455"
    digitString = "123456789"
    whiteSpaceString = "        Hello World         "
    str = "10000000this is string example....wow!!!10000001";

    # Copying a String
    print "Copy - You do not need to copy a String since they are immutable"

    # Updating a String
    copyAlphaString = alphaString[:] + " Mr Tim"
    print "\nUpdating String: " + copyAlphaString


    # Concatenate String
    print "Concatenate String: " + "This is concatenation using '+'"

    # Slice - Gives the character from the given index
    print "\nSlice[5] : " + alphaString[5]
    print "Slice[6] : " + alphaString[6]
    print "Slice[7] : " + alphaString[7]

    # Range Slice - Value does not include index - 1
    print "\nRangeSlice[:]: " + alphaString[:]
    print "RangeSlice[3:]: " + alphaString[3:]
    print "RangeSlice[:7]: " + alphaString[:7]

    # String Formatter
    print "\nString formatter() - My name is %s and weight is %d kg!" % ('Tim', 200)

    # Capitalize()
    capitializeString = alphaString.capitalize()
    print "Capitalize(): " + capitializeString

    # Count
    print "\nCount 'Lorem' appears: ", longText.count("Lorem", 0, len(longText))
    print "Count 'in' appears: ", longText.count("in", 0, len(longText))

    # Find
    print "\nFind 'Lorem' appears: ", longText.find("Lorem", 0, len(longText))
    print "Find 'Tim' appears: ", longText.find("Tim", 0, len(longText))

    # Index - Same as find but raises an exception if target is NOT found
    print "\nIndex 'Lorem' appears: ", longText.index("Lorem", 0, len(longText))
    # print "Index 'Tim' appears: ", longText.index("Tim", 0, len(longText))        # Should produce an error if uncommented

    # Check if String alpha numeric - Spaces, commas and white characters cause this to be False
    print "\nIs AlphaNumeric longText? : ", longText.isalnum()
    print "Is AlphaNumeric alphaString? : ", alphaString.isalnum()
    print "Is AlphaNumeric alphaNumericString? : ", alphaNumericString.isalnum()

    # Is Digit ?
    print "\nIs Digit on digitString: ", digitString.isdigit()
    print "Is Digit alphaNumericString? : ", alphaNumericString.isdigit()

    # Is Lower case ?
    print "\nIs LowerCase on longtext: ", longText.islower()
    print "Is Lowercase on alphaString: ", alphaString.islower()

    # Join
    seperator = "-"
    sequence = ("a", "b", "c")
    print "join() alphaString & nnumeric with seperator ':::'  - " + seperator.join(sequence)


    # Max() - Returns max alphabetical character appears in the string
    print "Max() for AlphaString: ", max(alphaString)
    print "Max() for NumericString: ", max(numericString)


    # Replace
    replaceString = alphaString.replace("world", "Tim")
    print "\nReplace() World with Tim: " + replaceString

    # Strip  - Remove both leading and trailing white spaces
    print "\nStrip(): ", str.strip("1")
    print "String() whiteSpaceString:" + whiteSpaceString.strip()



if __name__ == '__main__':
    stringMain()