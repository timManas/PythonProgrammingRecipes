import itertools

def listComprehension(symbol, type, side, TIF, price, quantity, algoParams):

    id = [[a, b, c, d, e, f, g] for a in symbol
          for b in type
          for c in side
          for d in TIF
          for e in price
          for f in quantity
          for g in algoParams]

    for i in range(len(id)):
        print(id[i], "\n")

    print("Total Permutation Size: ", len(id))

    # printing result
    print("All possible permutations using List Comprehension : " + str(id))

    pass


def iterTools(symbol, type, side, TIF, price, quantity, algoParams):

    combinedList = [symbol, type, side, TIF, quantity, algoParams]

    id = list(itertools.product(*combinedList))

    for i in range(len(id)):
        print(id[i], "\n")

    print("Total Permutation Size: ", len(id))

    # printing result
    print("All possible permutations using IterTools : " + str(id))

    pass


def main():

    symbol = ['AAPL', 'IBKR', 'IYZ']
    type = ['MKT', 'LMT']
    side = ['Buy', 'Sell']
    TIF = ['DAY', 'IOC', 'FOK', 'GTD', 'GTC']
    price = [10.1]
    quantity = [5]
    algoParams = ['MAXISO', 'BMO', 'TWAP', 'VWAP']


    #Method 1: Permutation by List Comprehension
    listComprehension(symbol, type, side, TIF, price, quantity, algoParams)

    print("\n\n\n =============================================== \n\n\n ")

    #Method 2: Permutation by IterTools
    iterTools(symbol, type, side, TIF, price, quantity, algoParams)




    # Method 1: Using List Comprehension





if __name__ == '__main__':
    main()