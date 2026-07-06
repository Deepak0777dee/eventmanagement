import os
import re

directory = "c:\\Users\\D-ROCK\\Desktop\\eventmanagement"

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to move nav-hamburger inside the flex div
        # Find: </div>\s*<button class="nav-hamburger"
        # Replace with: <button class="nav-hamburger"...> \n </div>
        
        pattern = re.compile(r'(<a href="contact\.html" class="nav-contact-btn".*?</a>\s*)\n\s*</div>\s*<button class="nav-hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>', re.DOTALL)
        
        replacement = r'\1\n      <button class="nav-hamburger" aria-label="Toggle menu"><span></span><span></span><span></span></button>\n    </div>'
        
        new_content = pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
