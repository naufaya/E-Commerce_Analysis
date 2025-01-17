import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
data = pd.read_csv('/Users/naufaya/Downloads/E-Commerce Public Dataset/dataset_complete.csv')

# Convert 'order_purchase_timestamp' to datetime
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'], errors='coerce')

# Set up the page
st.set_page_config(page_title="E-Commerce Dashboard", page_icon=":bar_chart:", layout="centered")
st.title('E-Commerce Data Analysis Dashboard')
st.write('This dashboard provides insights into customer segments, product categories, and city-based revenue analysis.')

# Sidebar for navigation
st.sidebar.header('Filters')
city_filter = st.sidebar.selectbox('Select City', data['customer_city'].unique())
category_filter = st.sidebar.selectbox('Select Product Category', data['product_category_name_english'].unique())

# Sidebar for Date Range Filter
st.sidebar.header('Date Range')
start_date = st.sidebar.date_input('Start Date', data['order_purchase_timestamp'].min().date())
end_date = st.sidebar.date_input('End Date', data['order_purchase_timestamp'].max().date())

# Filter data based on user input
filtered_data = data[(data['customer_city'] == city_filter) & 
                     (data['product_category_name_english'] == category_filter) &
                     (data['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
                     (data['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

# Section 1: Customer Segments Contribution
st.header('Customer Segments Contribution')
st.write(f'Showing data for {city_filter} and category {category_filter}')
if not filtered_data.empty:
    customer_segment_plot = filtered_data.groupby('Segment')['revenue'].sum().plot(kind='bar', color='skyblue')
    customer_segment_plot.set_title('Customer Segments Contribution')
    customer_segment_plot.set_xlabel('Customer Segment')
    customer_segment_plot.set_ylabel('Total Revenue')
    st.pyplot(customer_segment_plot.figure)
else:
    st.write("No data available for the selected filters.")

# Section 2: Product Categories Contribution
st.header('Product Categories Contribution')
if not filtered_data.empty:
    category_revenue = filtered_data.groupby('product_category_name_english')['revenue'].sum().sort_values(ascending=False)
    st.bar_chart(category_revenue)
else:
    st.write("No data available to plot product categories.")

# Section 3: City-Based Revenue Insights
st.header('City-Based Revenue Insights')
city_revenue = data.groupby('customer_city')['revenue'].sum().sort_values(ascending=False)
st.bar_chart(city_revenue)

# Section 4: RFM Analysis Insights
st.header('RFM Analysis')
rfm_data = pd.read_csv('/Users/naufaya/Downloads/E-Commerce Public Dataset/rfm_analysis.csv')
rfm_data_sorted = rfm_data.sort_values('Recency', ascending=False)
st.write(rfm_data_sorted.head())

# Section 5: Outlier Analysis
st.header('Outlier Analysis')
revenue_threshold = st.sidebar.slider('Revenue Threshold for Outliers', min_value=100, max_value=5000, value=1000)
outlier_data = data[data['revenue'] > revenue_threshold]
st.write(outlier_data)

# Optional: Add download button for the processed data
st.download_button(
    label="Download Filtered Data",
    data=filtered_data.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv"
)