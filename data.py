import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data()
def load_data():
    files = ['Bangalore.csv', 'Delhi.csv', 'Chennai.csv', 'Hyderabad.csv', 'Mumbai.csv', 'Kolkata.csv']
    data_frames = []
    for file in files:
        df = pd.read_csv(f'data/{file}').replace(9, np.nan).dropna()
        df['Price'] = df['Price']/100000
        data_frames.append(df)
    return data_frames