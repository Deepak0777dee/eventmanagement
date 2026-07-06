import os

directory = "c:\\Users\\D-ROCK\\Desktop\\eventmanagement"
old_str = "onclick=\"window.location.href='login.html'\""
new_str = "onclick=\"window.location.href='404.html'\""

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content.replace(old_str, new_str)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced in {filename}")
