# 📊 Data Analysis Project: E-Commerce Public Dataset 💻

**Name:** Namira Ra’ufa Dayyana  
**Email:** naufayaa@gmail.com  
**ID Dicoding:** naufaya

## 🚀 **Business Problem**

In this project, I explore the E-Commerce Public Dataset to address the following questions:
1. Which customer segments contribute the most to the company’s revenue?
2. Which products or product categories generate the most revenue?

## 📦 **Data Wrangling**

Data wrangling is an essential part of any analysis, and here’s how I prepared the data for this project:

**A. Load Data**

I loaded the following datasets:
- customers_dataset.csv
- geolocation_dataset.csv
- order_items_dataset.csv
- order_payments_dataset.csv
- order_reviews_dataset.csv
- orders_dataset.csv
- product_category_name_translation.csv
- products_dataset.csv
- sellers_dataset.csv

**B. Merge and Clean Data**
- Merged order-related datasets (order_items, order_payments, order_reviews) for a complete order overview.
- Combined product data with product categories to get better insights.
- Dropped irrelevant columns to focus on the analysis (like timestamps, unnecessary product details, etc.).

## 🔍 **Exploratory Data Analysis (EDA)**

I performed a thorough analysis to understand the data’s structure and identify potential issues:

**A. Data Info**
- Investigated the data types, missing values, and duplicates.
- Dropped rows with missing or duplicate data to ensure consistency.

**B. Outliers Detection**

Outliers were detected using the Interquartile Range (IQR) method, which helped in identifying extreme data points that might affect the analysis.
- Some outliers were retained as they may indicate valuable business insights, such as premium customers or one-off large transactions.

## 📈 **Visualization & Explanatory Analysis**

With the cleaned data, I created several visualizations to answer the business questions:

1. **Customer Segments Contributing to Revenue**

I identified the top 10 customers by revenue:
- **Insight:** A small number of customers contribute to a significant portion of revenue. The top 2 customers alone contribute approximately 30% of the total revenue!

2. **Best-Selling Product Categories**

By grouping the data by product categories, I found that:
- Top categories such as bed_bath_table and health_beauty generate the most revenue.
- Low-performing categories like auto and garden_tools are generating under $900K.

3. **Revenue by City**

The analysis revealed that Sao Paulo leads in sales with $2.7M in revenue, followed by Rio de Janeiro with $1.5M.

## 💡 **RFM Analysis**

RFM (Recency, Frequency, Monetary) analysis is a powerful technique for understanding customer behavior. In this project, I performed the following steps:
1. **Recency:** Calculated how many days have passed since a customer’s last purchase.
2. **Frequency:** Counted the number of orders each customer made.
3. **Monetary:** Measured how much each customer has spent.

The RFM Scores helped me segment customers into groups based on their buying behavior, enabling targeted marketing strategies.

## 🔨 **Tools & Libraries**

This project was built using Python and the following libraries:
- pandas
- numpy
- matplotlib
- seaborn

## 💬 **Conclusions & Insights**
- The analysis provided deep insights into the behavior of customers and product performance.
- Strategies for increasing revenue could focus on retaining high-value customers, expanding successful product categories, and targeting specific cities with tailored marketing efforts.

## 📂 **Project Files**

The project includes the following files:
1. Dataset: CSV files used for analysis.
2. Jupyter/Colab Notebook: The code used to perform the analysis.
3. Streamlit Dashboard: Interactive dashboard showcasing key insights.
4. requirements.txt: List of dependencies required to run the project.
5. README.md: Documentation for the project.

## 🚀 **How to Run the Streamlit Dashboard**

To run the Streamlit dashboard, follow these steps:

1. **Clone or Download the Project**
   - Clone the repository to your local machine or download the ZIP file.

2. **Install Dependencies**
   - Make sure you have Python 3.8 or higher installed.
   - Install the necessary dependencies listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Streamlit Dashboard**
   - In your terminal, navigate to the project directory and run the following command:
     ```bash
     streamlit run dashboard.py
     ```

4. **Access the Dashboard**
   - After running the command, your browser should automatically open the Streamlit dashboard. If it doesn't, you can manually go to `http://localhost:8501` in your web browser.

💡 **Note:**
- The dashboard includes interactive elements to visualize the key insights, such as customer segments contributing to revenue and the best-selling product categories.

Thank you for checking out my project! I hope you found the analysis insightful. Feel free to reach out for any questions or collaborations. 🚀

🔗 **Find me online**  
[LinkedIn: Namira Ra'ufa Dayyana](https://www.linkedin.com/in/namira-ra-ufa-dayyana-a5a909251/)  
[Portfolio: Namira's Data Science Portfolio](https://www.datascienceportfol.io/naufaya)
