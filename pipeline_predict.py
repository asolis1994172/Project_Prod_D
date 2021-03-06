import joblib
import pandas as pd
import numpy as np
import config as cfg

import my_preprocessors as mypp

salary_price_model = joblib.load('Salary_pipeline.pkl')

def predict(X):
    predicts = salary_price_model.predict(X)
    ypreds = predicts
    print(ypreds)
    return(ypreds[0])