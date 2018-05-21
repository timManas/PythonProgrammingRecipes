import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt
from numpy.ma import column_stack


def dataFrameExample():
    print("::::::::: Pandas - DataFrame  ::::::::: ")

    # Create an Empty Data Frame
    emptyDataFrame = pd.DataFrame()
    print("Empty: ", emptyDataFrame)

    # Create a Data Frame from Lists
    oneDdata = [1, 2, 3, 4, 5]
    listDataFrame = pd.DataFrame(oneDdata)
    print("\nDataFrame from List:\n", listDataFrame)

    # Create a Data Frame from Dict of ndArrays / List
    twoDdata = [["A", 10], ["B", 20],  ["C", 30], ["D", 40], ["E", 50]]
    listDataFrame2 = pd.DataFrame(twoDdata)
    print("\nDataFrame from List:\n", listDataFrame2)

    print("\nYou can set the  Row and Column Name")
    twoDdata2 = [["A", 100], ["B", 200],  ["C", 300], ["D", 400], ["E", 500]]
    listDataFrame3 = pd.DataFrame(twoDdata2, columns=["Name", "Age"], dtype=float)
    print("\nDataFrame from List with Labeled Row and Column index:\n", listDataFrame3)

    # Create a DataFrame from  Dicts/List
    data = {"Name" : ["Tim", "John", "Manas"], "Age" : [10, 20, 30]}
    dictListdataFrame = pd.DataFrame(data)
    print("\nCreate a DataFrame from Dict/List:\n", dictListdataFrame)           # Notice how 0,1,2 header is blank ? Well this is the header

    # Create a DataFrame from Dict/List with index labeled
    dictListdataFrame2 = pd.DataFrame(data=data, index=[101, 102, 103])
    print("\nCreate a DataFrame from Dict/list with Index labeled:\n", dictListdataFrame2)

    # Create a DataFrame from List of Dicts
    data = [{"a": 2, "b": 4}, {"a": 10, "b": 20, "c": 30}]
    listOfDicDataFrame = pd.DataFrame(data)
    print("\nCreate a Dataframe from List of Dicts:\n", listOfDicDataFrame)

    data = [{"a": 2, "b": 4}, {"a": 10, "x": 20, "c": 30 , "b": 40}]
    listOfDicDataFrame = pd.DataFrame(data)
    print("\nCreate a Dataframe from List of Dicts:\n", listOfDicDataFrame)

    # Create a DataFrame from Dict of Series
    data = {"one" : pd.Series([1,2,3], index = ["a", "b", "c"]), "two": pd.Series([1,2,3,4,5], index = ["a","b", "c", "d", "e"])}
    dictSeriesDataFrame = pd.DataFrame(data)
    print("\nCreate a Datafrom from Dict of Series: \n", dictSeriesDataFrame)

    # Retrieve columns only
    print("\nRetrieve column 'one' only: \n",  dictSeriesDataFrame["one"])
    print("\nRetrieve column 'two' only: \n",  dictSeriesDataFrame["two"])

    # How to add to columns
    dictSeriesDataFrame["three"] = pd.Series([10, 20, 30], index=["a", "b", 'c'])
    print("\nAdded column to dictSeriesDataFrame: \n", dictSeriesDataFrame)

    dictSeriesDataFrame["three"] = pd.Series([100, 200, 300], index=["a", "e", 'x'])
    print("\nAdded column to dictSeriesDataFrame: \n", dictSeriesDataFrame)             # Notice how 300 is not part of DataFrame

    # How to delete columns
    del dictSeriesDataFrame["three"]
    print("\nDeleted column 'three': \n", dictSeriesDataFrame)

    # How to select row by label
    print("\nRows can be accessed using the loc function")
    print("\nPrinting row 'a': \n", dictSeriesDataFrame.loc["a"])
    print("\nPrinting row 'b': \n", dictSeriesDataFrame.loc["b"])

    # How to select row by integer location
    print("\nRows can also be accesed using the iloc function - Integer Location")
    print("\nPriting the row #2: \n", dictSeriesDataFrame.iloc[1])

    # How to select multiple rows can be used using the slice function
    print("\nPrinting multiple rows using slice function: \n", dictSeriesDataFrame[1:4])

    # How to add additional rows to a data frame
    df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['a', 'b'])
    df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
    df = df.append(df2)
    print("\nAdd additional rows: \n", df)

    # Delete a row
    df = df.drop(0)
    print("\nDeleting a row: \n", df)


if __name__ == '__main__':
    dataFrameExample()


'''
Pandas DataStructure: "Data Frame"

What ? 
- Data frames are two dimensional data structure. Data is set up in tabular structure with rows and columns
- Columns could of different types
- Size is Mutable
- Labeled axes (rows and columns)
- Can perform arithmentic operations on rows and columns


Why ? 


How ? 
pandas.DataFrame(data, index, columns, dtype, copy)
data - data can come in the form of ndarray, series, map, list, dict and also OTHER DATAFRAMES
index - Index must be UNIQUE and hashable.
dtype - represent the data Type. If none, data type is inferred
copy - copy data. Default is False



'''