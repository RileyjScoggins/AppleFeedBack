import sqlite3
import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

# Connect to the database
conn = sqlite3.connect('/Users/rileyscoggins/Desktop/AppleFeedBack/feedback.db')
cursor = conn.cursor()

# Retrieve the comments from the 'feedback' table
cursor.execute("SELECT comment FROM feedback")
comments = cursor.fetchall()

# Close the connection
conn.close()

# Count the frequency of each comment
comment_counts = Counter([comment[0] for comment in comments])

# Sort comments by frequency (most common first)
most_common_comments = comment_counts.most_common()

# Create the main window
root = tk.Tk()
root.title("Most Popular Feedback")

# Create a scrollable text area to display comments
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
text_area.grid(row=0, column=0, padx=10, pady=10)

# Add the most common comments to the text area
for comment, count in most_common_comments:
    text_area.insert(tk.END, f"Occurrences: {count}\n{comment}\n\n")

# Disable editing to make it read-only
text_area.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
