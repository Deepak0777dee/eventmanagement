import os
import re

directory = "c:\\Users\\D-ROCK\\Desktop\\eventmanagement"
files_to_update = ['dashboard.html', 'my-events.html', 'messages.html', 'wallet.html', 'settings.html']

for filename in files_to_update:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Add the email div right under the user name div
        if '<div class="sidebar-user-email"' not in content:
            content = content.replace(
                '<div class="sidebar-user-name" id="userName">User Name</div>',
                '<div class="sidebar-user-name" id="userName">User Name</div>\n      <div class="sidebar-user-email" id="userEmail" style="font-size: 0.75rem; color: var(--text-secondary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">user@example.com</div>'
            )
            
        # Update the JS to populate the email
        if "document.getElementById('userEmail').textContent = user.email;" not in content:
            content = content.replace(
                "document.getElementById('userName').textContent = user.name;",
                "document.getElementById('userName').textContent = user.name;\n    if(document.getElementById('userEmail')) document.getElementById('userEmail').textContent = user.email;"
            )
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
