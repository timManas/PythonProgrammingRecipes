import pandas as pd

def loadData():
    melbourne_file_path = "/Users/timmanas/ProgrammingProjects/ProgrammingRecipesPython/res/melb_data.csv"
    homeData = pd.read_csv(melbourne_file_path)
    pd.set_option('display.max_columns', None)

    # Generates the data on screen. Remember to put the printf
    print(homeData.describe())


if __name__ == '__main__':
    loadData()