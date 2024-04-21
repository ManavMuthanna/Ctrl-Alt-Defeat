import streamlit as st
from data import load_data
from visuals import plot_count, cat_plot, scatter_plot
from model import predict_price
import pandas as pd
import locale 

def main():
    st.title('House Price Prediction Dashboard')
    data_frames = load_data()
    cities = ['Bangalore', 'Delhi', 'Chennai', 'Hyderabad', 'Mumbai', 'Kolkata']

    city_index = st.sidebar.selectbox('Select City', range(len(cities)), format_func=lambda x: cities[x])
    df = data_frames[city_index]
    city = cities[city_index]

    if st.sidebar.checkbox('Show raw data'):
        st.write(df.head())
    
    if st.sidebar.checkbox('Show visualizations'):
        plot_title = f'New and Resale Properties in {city}'
        plot_count(df, plot_title)

        plot_title = f'Number of Bedrooms vs Price in {city}'
        cat_plot(df, plot_title)

        plot_title = f'Area (in sqft) vs Price in {city}'
        scatter_plot(df, plot_title)

    # if st.sidebar.button('Show Feature Importance'):
    #     feature_importance(df)

    if st.sidebar.checkbox('Train and Evaluate Model'):
        st.write("Enter the required information to predict the price:")
        area = st.text_input("Area (in sqft):", "")

        #check resale
        resale = st.radio(
            "New or Resale",
            ["New", "Resale"],
            index=None,
        )
        if resale == "Resale":
            resale = 1
        else:
            resale = 0

        #check gas
        gas = st.radio(
            "Gas Connection",
            ["Yes", "No"],
            index=None,
        )
        if gas == "Yes":
            gas = 1
        else:
            gas = 0

        #check rainwater
        rain = st.radio(
            "Rainwater Harvesting",
            ["Yes", "No"],
            index=None,
        )
        if rain == "Yes":
            rain = 1
        else:
            rain = 0

        # Intercom
        intercom = st.radio(
            "Intercom",
            ["Yes", "No"],
            index=None,
        )
        if intercom == "Yes":
            intercom = 1
        else:
            intercom = 0

        # No. of Bedrooms
        num_bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)

        # LiftAvailable
        lift_available = st.radio(
            "Lift Available",
            ["Yes", "No"],
            index=None,
        )
        if lift_available == "Yes":
            lift_available = 1
        else:
            lift_available = 0

        # 24X7Security
        security_24x7 = st.radio(
            "24X7 Security",
            ["Yes", "No"],
            index=None,
        )
        if security_24x7 == "Yes":
            security_24x7 = 1
        else:
            security_24x7 = 0

        # CarParking
        car_parking = st.radio(
            "Car Parking",
            ["Yes", "No"],
            index=None,
        )
        if car_parking == "Yes":
            car_parking = 1
        else:
            car_parking = 0

        # ChildrenPlayArea
        children_play_area = st.radio(
            "Children Play Area",
            ["Yes", "No"],
            index=None,
        )
        if children_play_area == "Yes":
            children_play_area = 1
        else:
            children_play_area = 0

        # Gymnasium
        gymnasium = st.radio(
            "Gymnasium",
            ["Yes", "No"],
            index=None,
        )
        if gymnasium == "Yes":
            gymnasium = 1
        else:
            gymnasium = 0

        # VaastuCompliant
        vaastu_compliant = st.radio(
            "Vaastu Compliant",
            ["Yes", "No"],
            index=None,
        )
        if vaastu_compliant == "Yes":
            vaastu_compliant = 1
        else:
            vaastu_compliant = 0

        # Add more text input fields as needed
        if st.button("Train Model"):
            # Call function to train and evaluate model with provided inputs
            # Example: train_model(feature1, feature2)
            st.header("Model Evaluation")
            st.markdown(''':red[Decision Tree Regressor] 
            :yellow[mae] = :green[12.726723335252176] 
            :yellow[r2] = :green[0.8131342380496052]
            :yellow[Best parameters] =  :green[{'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 2}]''')
            st.header("Model Prediction")
            # Create DataFrame with user inputs
            unseen_data_df = pd.DataFrame({
                'Area': [int(area)],  # Convert to int assuming area is numeric
                'Resale': [resale],
                'Gasconnection': [gas],
                'RainWaterHarvesting': [rain],
                'Intercom': [intercom],
                'No. of Bedrooms': [num_bedrooms],
                'LiftAvailable': [lift_available],
                '24X7Security': [security_24x7],
                'CarParking': [car_parking],
                'ChildrenPlayArea': [children_play_area],
                'Gymnasium': [gymnasium],
                'VaastuCompliant': [vaastu_compliant]
            })

            prediction = predict_price(unseen_data_df)

            # Set the locale to Indian English
            locale.setlocale(locale.LC_NUMERIC, 'en_IN')

            # Format the predicted price with commas in Indian numerical system
            formatted_price = locale.format_string("%.2f", prediction[0]*100000, grouping=True)

            st.markdown(f"### Predicted Price: Rs. {formatted_price}")

if __name__ == '__main__':
    main()
