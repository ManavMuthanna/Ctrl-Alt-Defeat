import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def predict_price(unseen_data):
    df1 = pd.read_csv('../data/Bangalore.csv')
    df2 = pd.read_csv('../data/Delhi.csv')
    df3 = pd.read_csv('../data/Chennai.csv')
    df4 = pd.read_csv('../data/Hyderabad.csv')
    df5 = pd.read_csv('../data/Mumbai.csv')
    df6 = pd.read_csv('../data/Kolkata.csv')

    df1.replace(9, np.nan, inplace=True)
    df2.replace(9, np.nan, inplace=True)
    df3.replace(9, np.nan, inplace=True)
    df4.replace(9, np.nan, inplace=True)
    df5.replace(9, np.nan, inplace=True)
    df6.replace(9, np.nan, inplace=True)

    df1 = df1.dropna()
    df2 = df2.dropna()
    df3 = df3.dropna()
    df4 = df4.dropna()
    df5 = df3.dropna()
    df6 = df4.dropna()

    # print(f"Bangalore:{df1.shape}\n")
    # print(f"Delhi:{df2.shape}\n")
    # print(f"Chennai:{df3.shape}\n")
    # print(f"Hyderabad:{df4.shape}\n")
    # print(f"Mumbai:{df5.shape}\n")
    # print(f"Kolkata:{df6.shape}\n")

    df1['Price'] = df1['Price']/100000
    df2['Price'] = df2['Price']/100000
    df3['Price'] = df3['Price']/100000
    df4['Price'] = df4['Price']/100000
    df5['Price'] = df5['Price']/100000
    df6['Price'] = df6['Price']/100000

    frames = [df1,df2,df3,df4,df5,df6]
    merged = pd.concat(frames)
    merged = merged.rename(columns={"Children'splayarea": "ChildrenPlayArea"})
    merged = merged.dropna()
    merged = merged.reset_index(drop=True)

    feature_names = ['Area', 'Resale', 'Gasconnection', 'RainWaterHarvesting', 'Intercom', 
                 'No. of Bedrooms', 'LiftAvailable', '24X7Security', 'CarParking', 
                 'ChildrenPlayArea', 'Gymnasium', 'VaastuCompliant']


    X = merged[feature_names]
    y = merged['Price']

    final_model = DecisionTreeRegressor(max_depth=None, min_samples_split=2, min_samples_leaf=1)  # Replace with your best parameters
    final_model.fit(X, y)

    # unseen_data = pd.DataFrame({
    # 'Area': [1200, 1500, 1000],  # Example values for Area in square feet
    # 'Resale': [1, 0, 1],          # Example values for Resale (1 for resale available, 0 for not available)
    # 'Gasconnection': [0, 1, 1],   # Example values for Gasconnection (1 for available, 0 for not available)
    # 'RainWaterHarvesting': [1, 1, 0],  # Example values for RainWaterHarvesting
    # 'Intercom': [0, 1, 0],        # Example values for Intercom
    # 'No. of Bedrooms': [2, 3, 2], # Example values for No. of Bedrooms
    # 'LiftAvailable': [1, 1, 0],   # Example values for LiftAvailable
    # '24X7Security': [1, 1, 0],    # Example values for 24X7Security
    # 'CarParking': [1, 1, 0],      # Example values for CarParking
    # 'ChildrenPlayArea': [1, 0, 1],# Example values for ChildrenPlayArea
    # 'Gymnasium': [1, 1, 0],       # Example values for Gymnasium
    # 'VaastuCompliant': [1, 0, 1]  # Example values for VaastuCompliant
    # })


    predictions = final_model.predict(unseen_data)
    return predictions