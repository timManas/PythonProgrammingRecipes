import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

def seriesExample():
    print("::::::::: Pandas - Series  ::::::::: ")

    numericData = numpy.array(["1", "2", "3", "4", "5"])
    alphaData = numpy.array(["a", "b", "c", "d", "e"])
    numericDic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

    # How to create an Empty Series
    emptySeries = pd.Series()
    print("\nCreate Empty Series: ", emptySeries)

    # How to create a Series from n-dimensional array
    dataSeries1 = pd.Series(numericData)
    print("\nCreate a Series from n-dimensional array: ", dataSeries1)             # Notice we did not assign index so by default, pandas assigned the indexes

    dataSeries2 = pd.Series(alphaData, [100, 101, 102, 103, 104])
    print("Create a Series from n-dimensional array: ", dataSeries2)

    # How to create a Series from a dictionary
    dictSeries = pd.Series(numericDic)
    print("\nCreate a Series from a dictionary: ", dictSeries)

    dictSeries2 = pd.Series(numericDic, ["x", "y", "z", "a", "b"])
    print("Create a Series from a dictionary: ", dictSeries2)       # Notice here that x,y,z is replaced with a NAN since it cannot find that key

    # How to create a Series from a Scalar
    scalarSeries = pd. Series(5, [100, 200, 300, 400, 500])
    print("\nCreate a Series from Scalar: ", scalarSeries)

    # How to access data from Series with Position
    print("\nData from Series can be accessed similar to that of numPy Arrays")
    print("Access the 4th Element from dataSeries: ", dataSeries1[3])
    print("Access the 3rd Element from numericDic: ", dictSeries[1])
    print("Access the 1st Element from dicSeries2: ", dictSeries2[0])
    print("Access the 4th Element from dicSeries2: ", dictSeries2[3])


    # How to retrieve the first Three Elements
    print("\nYou can retrieve any amount of Elements in Series")
    print("Retrieving the first three Element in dataSeries1: ", dataSeries1[:3])
    print("Retrieving the first three Element in dataSeries1: ", dataSeries2[:3])
    print("Retrieving the first three Element in dictSeries: ", dictSeries[:3])
    print("Retrieving the first three Element in dictSeries2: ", dictSeries2[:3])

    # How to retrieve the Element using the "Key"
    print("\n You can retrieve any element using the Key")
    print("Access the Element with Key '100': ", scalarSeries[100])
    print("Access the Element with Key '500': ", scalarSeries[500])



if __name__ == '__main__':
    seriesExample()



'''
Pandas DataStructure: "Series"

What ? 
- Series is a immutable (DOES NOT CHANGE) one dimensional homogeneous array and size 
- Capable of holding data of any type (integer, string, float, python objects, etc)


Why ?

How ? 
pandas.Series(data, index, dtype, copy)
data - data can come in the form of a list
index - Index must be UNIQUE and hashable.
dtype - represent the data Type. If none, data type is inferred
copy - copy data. Default is False

Notes


'''