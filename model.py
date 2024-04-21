import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def feature_importance(df):
    feature_names = ['Area', 'No. of Bedrooms', 'Resale']
    X = df[feature_names]
    y = df['Price']
    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.3, random_state=1)
    
    model = ExtraTreesRegressor()
    model.fit(train_X, train_y)
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 5))
    plt.title('Feature Importances')
    plt.bar(range(train_X.shape[1]), importances[indices], color="r", align="center")
    plt.xticks(range(train_X.shape[1]), train_X.columns[indices], rotation=90)
    plt.xlim([-1, train_X.shape[1]])
    st.pyplot(plt)

def train_and_evaluate(df):
    feature_names = ['Area', 'No. of Bedrooms', 'Resale']
    X = df[feature_names]
    y = df['Price']
    train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.3, random_state=1)

    model = RandomForestRegressor(random_state=1)
    model.fit(train_X, train_y)
    predictions = model.predict(val_X)
    st.write('Mean Absolute Error:', mean_absolute_error(val_y, predictions))
    st.write('R² score:', r2_score(val_y, predictions))
