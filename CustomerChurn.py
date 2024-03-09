# POST the independent features (parameters) of our dataset to the URL.

# Create a data model using pydantic
from pydantic import BaseModel

# Create a class(pydantic data model) that inherits from the BaseModel class
class Churn(BaseModel):
    CreditScore: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Geography_France: int
    Geography_Germany: int
    Geography_Spain: int
    Gender_Female: int
    Gender_Male: int



