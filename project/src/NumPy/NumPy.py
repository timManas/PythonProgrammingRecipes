import numpy as np
import matplotlib.pyplot as plt


def numPyExample():
    # Single one dimensional array
    stock_list = [3.5, 5, 2, 8, 4.2]
    oneDimenArray = np.array(stock_list)                    # This was technially returns ??
    print(oneDimenArray, type(oneDimenArray))

    # Multi dimensional array
    multiDimenArray = np.array([[1, 2], [5, 6]])              # Dont forget the Extra [] for the the outer to represent this as an array ... this was 'A' ?
    print(multiDimenArray, type(multiDimenArray))

    matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrixB = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])


    # Dot Product between
    print("\nDot Product between A & B: ", np.dot(matrixB, matrixA))

    # Cross Product between
    print("\nCross Product between A & B: ", np.cross(matrixA, matrixB))

    # How to access the dimensions of the array
    print("\nDimensions of the array: ", multiDimenArray.shape)

    # Slice an numpy Array
    print("Slice Array from Element 1-3: ", oneDimenArray[1:3])

    # Print only rows
    print("Print Rows only: ", multiDimenArray[0, :])

    # Print only columns
    print("Print Colums only: ", multiDimenArray[:, 0])

    # Print only specific row
    print("Print 1st row: ", multiDimenArray[0])
    print("Print 2nd row: ", multiDimenArray[1])

    # Print specific Element in the multiDimArray
    print("Print the element from (1,1): ", multiDimenArray[1,1])

    # Print Log on Arrays
    print("\nLog on Arrays: ", np.log(multiDimenArray))

    # Print Mean on Arrays
    print("Mean on Arrays: ", np.mean(multiDimenArray))

    # Print Max on Arrays
    print("Max on Arrays: ", np.max(multiDimenArray))

    # Print Scalar values multiplied with Array ... this should still produce an array
    print("Sclar*Array: ", oneDimenArray*2 + 5)

    # Print the Standard Deviation
    print("\nStandard Deviation of one dimensional array: ", np.std(oneDimenArray))
    print("Standard Deviation of multi dimensional array:", np.std(multiDimenArray))


    # Simulating stocks
    print("\nSimulating Base Asset ")
    N = 10
    assets = np.zeros((N, 100))             # The zeroes method creates an array with the dimensions and filled with ALL Zeroes
    returns = np.zeros((N, 100))            # This will be (10 X 100) size array

    R_1 = np.random.normal(1.01, 0.03, 100)     # The random module is very useful. For this method, we draw 100 random numbers
    returns[0] = R_1
    assets[0] = np.cumprod(R_1)                 # Calculates the cumalative asset price
    print(assets[0])                            # This is the base asset cumalative price

    # Generate Assets that are correlated with R_i
    for i in range(1, N):
        R_i = R_1 + np.random.normal(0.001, 0.02, 100)
        returns[i] = R_i                                    # Set each row of returns equal to the new R_1 array
        assets[i] = np.cumprod(R_i)
        pass

    mean_returns = [(np.mean(R)-1) * 100 for R in returns]
    print("Mean Return: ", mean_returns)

    return_volatility = [np.std(R) for R in returns]
    print ("Volatility: ", return_volatility)

    plt.bar(np.arange(len(mean_returns)), mean_returns)
    plt.xlabel("Stock")
    plt.ylabel("Returns")
    plt.title('Returns for {0} Random Assets'.format(N))
    plt.show()



    print("\nPortfolio creation & Calculating Expected return & risk")
    # First we generate N random weights for each asset in the portfolio
    weights = np.random.uniform(0, 1, N)
    weights = weights / np.sum(weights)
    print("Weights: ", weights)

    '''
    To calculate the mean return of the portfolio, we have to scale each asset's return by its designated weight. 
    We can pull each element of each array and multiply them individually, 
    but it's quicker to use NumPy's linear algebra methods. The function that we want is dot(). 
    This will calculate the dot product between two arrays for us. So if  v=[1,2,3]  and  w=[4,5,6] , then: v⋅w=1×4+2×5+3×6
    '''

    portforlioReturns = np.dot(weights, mean_returns)
    print("PortFolio Returns: ", portforlioReturns)



    # NAN
    print("\nNAN Example")
    vector = np.array([1, 2, 3, 4, np.nan, 6, 7, 8])
    print("NAN Exaxmple: ", vector)
    print("Mean of NAN exmaple: ", np.mean(vector))                 # If a array has a nan, then it fucks up our test signigicantly
    print("How to get rid of NAN in the dataset: ", vector[~np.isnan(vector)])                                # How to get rid of a NAN in the data set
    print("Calculating mean with NAN in the dataset: ", np.nanmean(vector))



if __name__ == '__main__':
    numPyExample()

""""
Numpy

What ? 
- Python package which is highly required for performing mathematical calculations
- Used for multi dimension array calculations and provides mathematical formulas without having the need to create them from scratch
- Integrates with Pandas to handle large datasets 

How ? 
- use "import numpy as np", to download the package onto Python


"""
