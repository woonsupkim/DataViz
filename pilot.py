import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    try:
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            data = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def summarize_data(data):
    print("\n### Data Summary ###")
    print(data.info())
    print("\n### Basic Statistics ###")
    print(data.describe())
    print("\n### Null Values ###")
    print(data.isnull().sum())

def visualize_business_data(data):
    print("\nGenerating Business Visualizations...")
    numeric_cols = data.select_dtypes(include=['number']).columns

    # Revenue Trend Visualization
    if 'date' in data.columns and 'revenue' in numeric_cols:
        data['date'] = pd.to_datetime(data['date'])
        revenue_trend = data.groupby('date')['revenue'].sum().reset_index()
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=revenue_trend, x='date', y='revenue')
        plt.title('Revenue Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        plt.show()

    # Customer Segmentation
    if 'customer_id' in data.columns and 'revenue' in numeric_cols:
        customer_revenue = data.groupby('customer_id')['revenue'].sum().reset_index()
        plt.figure(figsize=(10, 6))
        sns.histplot(customer_revenue['revenue'], bins=20, kde=True)
        plt.title('Customer Revenue Distribution')
        plt.xlabel('Revenue')
        plt.ylabel('Count')
        plt.show()

    # A/B Test Results
    if 'group' in data.columns and 'conversion_rate' in numeric_cols:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=data, x='group', y='conversion_rate')
        plt.title('A/B Test Conversion Rates')
        plt.xlabel('Group')
        plt.ylabel('Conversion Rate')
        plt.show()

    # Product Performance
    if 'product' in data.columns and 'revenue' in numeric_cols:
        product_revenue = data.groupby('product')['revenue'].sum().sort_values(ascending=False)
        plt.figure(figsize=(10, 6))
        product_revenue.plot(kind='bar')
        plt.title('Revenue by Product')
        plt.xlabel('Product')
        plt.ylabel('Revenue')
        plt.show()

def generate_business_insights(data):
    print("\n### Business Insights ###")
    
    # Insight 1: Top-performing products
    if 'product' in data.columns and 'revenue' in data.columns:
        top_products = data.groupby('product')['revenue'].sum().sort_values(ascending=False).head(3)
        print("Top-performing products:")
        print(top_products)

    # Insight 2: High-value customers
    if 'customer_id' in data.columns and 'revenue' in data.columns:
        high_value_customers = data.groupby('customer_id')['revenue'].sum().sort_values(ascending=False).head(3)
        print("\nHigh-value customers:")
        print(high_value_customers)

    # Insight 3: Conversion Rate Analysis
    if 'group' in data.columns and 'conversion_rate' in data.columns:
        group_means = data.groupby('group')['conversion_rate'].mean()
        print("\nConversion Rate by Group:")
        print(group_means)

def generate_business_recommendations(data):
    print("\n### Business Recommendations ###")

    # Recommendation 1: Target High-value Customers
    if 'customer_id' in data.columns and 'revenue' in data.columns:
        print("- Focus on nurturing relationships with high-value customers identified in the data.")

    # Recommendation 2: Optimize Product Pricing or Marketing
    if 'product' in data.columns and 'revenue' in data.columns:
        print("- Review pricing or marketing strategies for underperforming products to boost revenue.")

    # Recommendation 3: Refine A/B Testing
    if 'group' in data.columns and 'conversion_rate' in data.columns:
        print("- Conduct further analysis on A/B test results to validate significant differences in conversion rates.")

    # Recommendation 4: Address Seasonal Trends
    if 'date' in data.columns and 'revenue' in data.columns:
        print("- Use seasonal revenue trends to plan inventory and marketing campaigns effectively.")

def main():
    print("Welcome to the Business Data Analysis and Visualization Tool")
    file_path = input("Please enter the path to your CSV or Excel file: ").strip()
    if not os.path.exists(file_path):
        print("The specified file does not exist. Please try again.")
        return
    
    data = load_data(file_path)
    if data is None:
        return
    
    summarize_data(data)
    visualize_business_data(data)
    generate_business_insights(data)
    generate_business_recommendations(data)
    print("\nAnalysis Complete!")

if __name__ == "__main__":
    main()
