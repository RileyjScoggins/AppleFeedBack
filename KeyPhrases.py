import sqlite3
import tkinter as tk
from tkinter import scrolledtext
from collections import Counter

# Define key phrases for common issues
key_phrases = {
    "battery issues": ["battery life", "short battery", "charges quickly", "doesn't last", "tethered to charger"],
    "price concerns": ["too expensive", "price too high", "overpriced", "costly", "not worth the price"],
    "performance issues": ["lag", "slow", "unresponsive", "glitch", "delay", "freezes", "stuttering"],
    "comfort issues": ["uncomfortable", "heavy", "bulky", "tight", "pressure on nose", "painful", "headache"],
    "design concerns": ["design flaw", "poor design", "ugly", "unattractive", "awkward design", "too big"],
    "audio issues": ["audio quality", "no sound", "poor audio", "sound is bad", "audio cuts out"],
    "software issues": ["software bug", "software crash", "software glitches", "not working", "not responding"],
    "compatibility issues": ["doesn't work", "incompatible", "not supported", "no app support"]
}

# Connect to the database
conn = sqlite3.connect('/Users/rileyscoggins/Desktop/AppleFeedBack/feedback.db')
cursor = conn.cursor()

# Retrieve the comments from the 'feedback' table
cursor.execute("SELECT comment FROM feedback")
comments = cursor.fetchall()

# Close the connection
conn.close()

# Initialize a Counter for key phrase occurrences
issue_counts = Counter()

# Loop through each comment and check for key phrases
for comment in comments:
    comment_text = comment[0].lower()  # Convert to lowercase for case-insensitive matching
    for issue, phrases in key_phrases.items():
        for phrase in phrases:
            if phrase in comment_text:
                issue_counts[issue] += 1

# Sort issues by frequency (most common first)
sorted_issues = issue_counts.most_common()

# Create the main window
root = tk.Tk()
root.title("Main Issues in Feedback")

# Create a scrollable text area to display the results
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text_area.grid(row=0, column=0, padx=10, pady=10)

# Add the issues and their counts to the text area
for issue, count in sorted_issues:
    text_area.insert(tk.END, f"Issue: {issue.capitalize()}\nOccurrences: {count}\n\n")

# Disable editing to make it read-only
text_area.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
