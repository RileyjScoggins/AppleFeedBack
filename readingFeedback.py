import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your uploaded database
db_path = '/Users/rileyscoggins/Desktop/AppleFeedBack/feedback.db'

def read_and_visualize_db(db_path):
    # Connect to the database
    conn = sqlite3.connect(db_path)
    
    # Fetch table names
    query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(query_tables, conn)
    print("Tables in the database:")
    print(tables)

    # Fetch data from one table (adjust the table name if needed)
    table_name = tables.iloc[0, 0]  # First table; change index as needed
    query_data = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query_data, conn)

    print(f"\nData from the table '{table_name}':")
    print(df.head())

    # Visualization Example
    # Replace 'column_name' with a relevant column from your data
    if 'column_name' in df.columns:
        sns.countplot(data=df, x='column_name')
        plt.title(f'Distribution of {table_name}')
        plt.show()

    conn.close()
    return df

# Run the function
data = read_and_visualize_db(db_path)
