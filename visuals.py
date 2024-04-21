import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_count(data, title):
    df1 = data[data['Resale'] == 0]
    df2 = data[data['Resale'] == 1]
    palette = sns.color_palette("husl", 8)
    st.subheader(title)
    fig, ax = plt.subplots(1, 2, figsize=(15, 10))
    sns.countplot(y='Location', data=df1, order=df1.Location.value_counts().index[:10], ax=ax[0], palette=palette)
    ax[0].set_title('Number of New Properties')
    sns.countplot(y='Location', data=df2, order=df2.Location.value_counts().index[:10], ax=ax[1], palette=palette)
    ax[1].set_title('Number of Resale Properties')
    plt.tight_layout(pad=3.0)
    st.pyplot(fig)

def cat_plot(data, title):
    st.subheader(title)
    palette = sns.color_palette("husl", 8)
    fig = sns.catplot(x="No. of Bedrooms", y="Price", data=data, palette=palette)
    plt.title('Number of Bedrooms vs Price')
    st.pyplot(fig)

def scatter_plot(data, title):
    st.subheader(title)
    fig, ax = plt.subplots()
    sns.scatterplot(x="Area", y="Price", data=data, color="#4e89ae", marker="P", ax=ax)
    plt.title('Area in square feet vs Price')
    plt.gcf().set_size_inches(8, 6)
    st.pyplot(fig)
