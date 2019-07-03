import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

def modelValidation():
    file_path = "/Users/timmanas/ProgrammingProjects/ProgrammingRecipesPython/res/melb_data.csv"
    home_data = pd.read_csv(file_path)

    y = home_data.Price

    features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
    X = home_data[features]

    # Sets data to be randomly set to be trained or analyzed
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

    model = DecisionTreeRegressor()
    model.fit(train_X, train_y)


    predicted_home_prices = model.predict(val_X)

    # This is where you calculate the Error
    mae = mean_absolute_error(val_y, predicted_home_prices)
    print("Mean Absolute Error: ", mae)






if __name__ == '__main__':
    modelValidation()



'''
What is model validation ?
- Evaluate the predictive accuracy of the model


Example of Model Validation: Mean Absolute Error (MAE)
formula:
error = actual - predicted
If House cost is $150,000 and predicted price is $100,000. Then error is $50,000

Note: To calculate MAE, a model is required

'''