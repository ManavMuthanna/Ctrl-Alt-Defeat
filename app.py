import streamlit as st
from data import load_data
from visuals import plot_count, cat_plot, scatter_plot
from model import feature_importance, train_and_evaluate

def main():
    st.title('House Price Prediction Dashboard')
    data_frames = load_data()
    cities = ['Bangalore', 'Delhi', 'Chennai', 'Hyderabad', 'Mumbai', 'Kolkata']

    city_index = st.sidebar.selectbox('Select City', range(len(cities)), format_func=lambda x: cities[x])
    df = data_frames[city_index]
    city = cities[city_index]

    if st.sidebar.checkbox('Show raw data'):
        st.write(df.head())

    plot_title = f'New and Resale Properties in {city}'
    plot_count(df, plot_title)

    plot_title = f'Number of Bedrooms vs Price in {city}'
    cat_plot(df, plot_title)

    plot_title = f'Area vs Price in {city}'
    scatter_plot(df, plot_title)

    if st.sidebar.button('Show Feature Importance'):
        feature_importance(df)

    if st.sidebar.button('Train and Evaluate Model'):
        train_and_evaluate(df)

if __name__ == '__main__':
    main()
