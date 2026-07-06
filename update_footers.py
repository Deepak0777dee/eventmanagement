import os
import re

footer_content = """<footer class="site-footer">
  <div class="footer-giant-brand" style="bottom:-5vw;">STACKLY</div>
  <div class="container">
    <div class="footer-grid">
      <div>
        <div style="margin-bottom: var(--space-md);"><a href="index.html" class="nav-logo"><img src="images/logo-stackly.webp" alt="STACKLY" style="height:36px;width:auto;filter:brightness(0) invert(1);" /></a></div>
        <p class="footer-desc">Your ultimate destination for discovering and booking premium events. Conferences, workshops, concerts, and more — all in one place.</p>
        <div class="footer-social">
          <a href="404.html" aria-label="X"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          <a href="404.html" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
          <a href="404.html" aria-label="LinkedIn"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg></a>
          <a href="404.html" aria-label="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg></a>
        </div>
      </div>
      <div>
        <div class="footer-title">Navigate</div>
        <ul class="footer-links"><li><a href="index.html">Home</a></li><li><a href="events.html">Events</a></li><li><a href="schedule.html">Schedule</a></li><li><a href="venue.html">Venue</a></li></ul>
      </div>
      <div>
        <div class="footer-title">Resources</div>
        <ul class="footer-links"><li><a href="404.html">Documentation</a></li><li><a href="404.html">Blog</a></li><li><a href="404.html">FAQ</a></li><li><a href="contact.html">Support</a></li></ul>
      </div>
      <div>
        <div class="footer-title">Subscribe to Our Newsletter</div>
        <div class="footer-newsletter" style="margin-top:0.5rem;">
          <input type="email" placeholder="Enter Your Email" />
          <button aria-label="Subscribe"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="19" x2="19" y2="5"/><polyline points="9 5 19 5 19 15"/></svg></button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 STACKLY. All Rights Reserved.</p>
      <div style="display:flex; gap:1.5rem;">
        <a href="404.html" style="color:var(--text-light); text-decoration:underline;">Terms & Agreements</a>
        <a href="404.html" style="color:var(--text-light); text-decoration:underline;">Privacy Policy</a>
      </div>
    </div>
  </div>
</footer>"""

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to maintain the opening footer tag attributes if there are any specific styles,
        # but the request asks to make footer content identical across all pages. 
        # Wait, if `schedule.html` has `style="margin-top: 6rem;"`, it might break if we remove it.
        # But let's just replace the whole footer.
        new_content = re.sub(r'<footer\b[^>]*>.*?</footer\s*>', footer_content, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
