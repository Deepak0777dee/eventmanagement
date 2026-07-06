import os
import re

directory = "c:\\Users\\D-ROCK\\Desktop\\eventmanagement"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace bad navigation links
        new_content = content.replace('<a href="404.html">Events</a>', '<a href="events.html">Events</a>')
        new_content = new_content.replace('<a href="404.html">Schedule</a>', '<a href="schedule.html">Schedule</a>')
        new_content = new_content.replace('<a href="404.html">Venue</a>', '<a href="venue.html">Venue</a>')
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed navigation links in {filename}")
