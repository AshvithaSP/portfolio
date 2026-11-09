import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import re

st.set_page_config(
    page_title="My Portfolio",
    page_icon="💻",
    layout="wide"
)

folder = Path(__file__).parent

# Read HTML, CSS and JavaScript
html = (folder / "index.html").read_text(encoding="utf-8")
css = (folder / "style.css").read_text(encoding="utf-8")
js = (folder / "script.js").read_text(encoding="utf-8")

# Embed CSS
html = re.sub(
    r'<link[^>]+href=["\']style\.css["\'][^>]*>',
    f'<style>{css}</style>',
    html
)

# Embed JavaScript
html = re.sub(
    r'<script[^>]+src=["\']script\.js["\'][^>]*>\s*</script>',
    f'<script>{js}</script>',
    html
)

# Embed profile image
if (folder / "profile.jpg").exists():
    image = base64.b64encode(
        (folder / "profile.jpg").read_bytes()
    ).decode()

    html = html.replace(
        "profile.jpg",
        f"data:image/jpeg;base64,{image}"
    )

# Display portfolio
components.html(
    html,
    height=1200,
    scrolling=True
)