import os

files_to_fix = [
    r"c:\Users\D-ROCK\Desktop\eventmanagement\schedule.html",
    r"c:\Users\D-ROCK\Desktop\eventmanagement\venue.html",
    r"c:\Users\D-ROCK\Desktop\eventmanagement\contact.html"
]

mobile_menu_html = '<div class="mobile-menu"><a href="index.html">Home</a><a href="events.html">Events</a><a href="schedule.html">Schedule</a><a href="venue.html">Venue</a><a href="contact.html">Contact Us</a><div class="mobile-login-wrap"><a href="login.html" style="display:flex;align-items:center;justify-content:center;padding:0.8rem;border-radius:999px;background:var(--primary);color:var(--bg-main);font-weight:700;font-size:0.9rem;">Login</a></div></div>\n'

for path in files_to_fix:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '<div class="mobile-menu">' not in content:
            content = content.replace('</nav>', '</nav>\n' + mobile_menu_html, 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {os.path.basename(path)}")
        else:
            print(f"{os.path.basename(path)} already has mobile menu")
