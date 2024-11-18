import pandas as pd
from ClearList import comments  # Import the list of comments from ClearList.py

# Create a DataFrame from the list of comments
df = pd.DataFrame(comments, columns=['Comment'])

# Write the DataFrame to an Excel file
excel_file = '/Users/rileyscoggins/Desktop/AppleFeedBack/Comments.xlsx'
df.to_excel(excel_file, index=False, engine='openpyxl')

print(f"Comments have been written to {excel_file}")
