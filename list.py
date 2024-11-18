import sqlite3

# Connect to the database
conn = sqlite3.connect('/Users/rileyscoggins/Desktop/AppleFeedBack/feedback.db')
cursor = conn.cursor()

# Retrieve the comments from the 'feedback' table
cursor.execute("SELECT comment FROM feedback")
comments = cursor.fetchall()

# Print all the comments
for comment in comments:
    print(comment[0])

# Close the connection
conn.close()
