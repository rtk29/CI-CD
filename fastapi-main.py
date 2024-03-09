from fastapi import FastAPI
import pickle
from CustomerChurn import Churn
import pandas as pd 
#import numpy as np

# Instantiate the FastAPI class
app = FastAPI()

# Load the pickle file
pickle_in = open("churn_classifier.pkl", "rb")
churn_classifier = pickle.load(pickle_in)

# Specify the route for the API(URL)
@app.get('/')
async def get():
    return {'Intro': 'Hello World', 'Number': '3434'}

# Store all the independent and dependent features in a list
features = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 
              'Geography_France', 'Geography_Germany', 'Geography_Spain', 'Gender_Female', 'Gender_Male', 'Prediction']

# Create a dataframe to store user inputs and predictions
user_data = pd.DataFrame(columns = features)
print(len(user_data))

# POST path parameter function to make predictions on the data.
@app.post('/predict')

# Use pydantic data model as the path operation parameter in the below function
async def predict_customer_churn(input: Churn):
    # Convert the parameter of type Churn(pydantic data model) to a dictionary
    input = input.dict()

    # Make prediction
    prediction = churn_classifier.predict([[input['CreditScore'], input['Age'], input['Tenure'], input['Balance'], input['NumOfProducts'], input['HasCrCard'],
                                            input['IsActiveMember'], input['EstimatedSalary'], input['Geography_France'], input['Geography_Germany'],
                                            input['Geography_Spain'], input['Gender_Female'], input['Gender_Male']]])
    
    if(prediction[0] == 1):
        prediction = "Customer churned"
    else:
        prediction = "Customer did not churn"

    # Store user input and prediction in the DataFrame
    user_data.loc[len(user_data)] = [input[key] for key in features[:-1]] + [prediction]
    
    # Save the DataFrame to an Excel file
    user_data.to_excel('user_data_predictions.xlsx', index=False)
    
    return {'Customer Churn Prediction': prediction}



