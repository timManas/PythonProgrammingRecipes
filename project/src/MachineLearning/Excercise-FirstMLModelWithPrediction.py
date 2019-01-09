import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def firstMLModelWithPrediction():

    # Step 0 - Set up Data
    file_path = "/Users/timmanas/ProgrammingProjects/ProgrammingRecipesPython/res/melb_data.csv"
    home_data = pd.read_csv(file_path)
    print("Displaying Columns: ", home_data.columns)        # Display the columns

    # Step 1 - Specify the Prediction Target
    # Our Prediction Target will Sales Price ... hence we can print out list of columns and see what the Sale Price columns is
    print("\nSpecify Prediction Target")
    y = home_data.Price
    print(y)

    # Step 2 - Create DataFrame called X
    print("\nCreate DataFrame")
    feature_names = ['Rooms', 'Price']
    X = home_data[feature_names]
    print(X)

    # Step 3 - Review Data of X (Remember: X is the DataFrame)
    print("\nDescribe the DataFrame")
    print(X.describe())     # Describes the data
    print(X.head())         # Describes the head

    # Step 4 - Specify and Fit Model
    print("\nSpecify and Fit Model")
    model = DecisionTreeRegressor(random_state=1)
    model.fit(X,y)
    print(model)

    # Step 5 - Make Predictions
    print("\nPredicting based on Features")
    predictions = model.predict(X)
    print(predictions)



    pass


if __name__ == '__main__':
    firstMLModelWithPrediction()