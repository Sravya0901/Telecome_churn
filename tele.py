import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('path_to_your_data.csv')

# Function to generate insights and visualizations
def generate_insights(data):
    # Overview of the data
    st.write("### Data Overview")
    st.dataframe(data.head())

    # Summary statistics
    st.write("### Summary Statistics")
    st.write(data.describe())

    # Data Visualization - Example using countplot
    st.write("### Churn Count")
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Churn', data=data, palette='pastel')
    st.pyplot()

    # You can add more visualizations here based on your requirements

# Main function to run the Streamlit app
def main():
    # Set the title and description of the app
    st.title('Telecom Customer Churn Analysis')
    st.write("This application provides insights on customer churn data.")

    # Display insights
    generate_insights(data)

if __name__ == '__main__':
    main()
