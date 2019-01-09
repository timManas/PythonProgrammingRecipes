import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def loadData():
    melbourne_file_path = "/Users/timmanas/ProgrammingProjects/ProgrammingRecipesPython/res/melb_data.csv"
    origData = pd.read_csv(melbourne_file_path)
    pd.set_option('display.max_columns', None)

    # Generates the data on screen. Remember to put the printf
    print(origData.describe())

    # See only the columns
    print("\nList of Columns")
    print(origData.columns)


    # If you take a closer look at the Melbourne Data, you will see some blank cells
    # You can handle these missing values by using the dropna
    origData = origData.dropna(axis=0)
    print(origData.describe())
    # Notice the difference in the data ?

    # Using a "Series" to pull out variable using the dot notation
    print("\nUsing Series to pull out variables")
    priceSeries = origData.Price
    print(priceSeries)


    # Using "Features" - These are columns that are inputted to our model to make predictions.
    # We may not want to use all features but need to specify the ones we do want to use
    print("\nUsing Features to select certain columns")
    homeDataFeatures = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    dataWithFeaturesOnly = origData[homeDataFeatures]

    print("\n Now Describe this new Data")
    print(dataWithFeaturesOnly.describe())

    print("\n Now we describe the HEAD")
    print(dataWithFeaturesOnly.head())


    print("\nBuilding new Model")
    origModel = DecisionTreeRegressor(random_state=1)
    dataWithFeaturesOnly.head()
    origModel.fit(dataWithFeaturesOnly, priceSeries)

    print("\nMake Predictions")
    print(origModel.predict(dataWithFeaturesOnly.head()))



if __name__ == '__main__':
    loadData()