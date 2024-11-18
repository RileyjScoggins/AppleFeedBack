import sqlite3
import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

# Define the list of keywords to track
keywords = ["battery", "price", "design", "comfort", "performance", "audio", "display", "service", "lag", "app"]

# Connect to the database
conn = sqlite3.connect('/Users/rileyscoggins/Desktop/AppleFeedBack/feedback.db')
cursor = conn.cursor()

# Retrieve the comments from the 'feedback' table
cursor.execute("SELECT comment FROM feedback")
comments = cursor.fetchall()

# Close the connection
conn.close()

# Initialize a Counter for keyword occurrences
keyword_counts = Counter()

# Loop through each comment and count occurrences of the keywords
for comment in comments:
    for keyword in keywords:
        keyword_counts[keyword] += comment[0].lower().count(keyword)

# Sort keywords by frequency (most common first)
sorted_keywords = keyword_counts.most_common()

# Create the main window
root = tk.Tk()
root.title("Keyword Occurrences in Feedback")

# Create a scrollable text area to display the results
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.grid(row=0, column=0, padx=10, pady=10)

# Add the keyword counts to the text area
for keyword, count in sorted_keywords:
    text_area.insert(tk.END, f"Keyword: {keyword.capitalize()}\nOccurrences: {count}\n\n")

# Disable editing to make it read-only
text_area.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
