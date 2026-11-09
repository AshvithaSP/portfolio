import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import re

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💻",
    layout="wide"
)

# Project folder
folder = Path(__file__).parent

# Read HTML, CSS and JavaScript files
html = (folder / "index.html").read_text(encoding="utf-8")
css = (folder / "style.css").read_text(encoding="utf-8")
js = (folder / "script.js").read_text(encoding="utf-8")

# Embed CSS inside HTML
html = re.sub(
    r'<link[^>]+href=["\']style\.css["\'][^>]*>',
    f'<style>{css}</style>',
    html
)

# Embed JavaScript inside HTML
html = re.sub(
    r'<script[^>]+src=["\']script\.js["\'][^>]*>\s*</script>',
    f'<script>{js}</script>',
    html
)

# Embed profile photo
photo_path = folder / "photo.jpg"

if photo_path.exists():
    image = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    html = html.replace(
        "photo.jpg",
        f"data:image/jpeg;base64,{image}"
    )
else:
    st.warning("Profile photo not found. Please check photo.jpg.")

# Display portfolio
components.html(
    html,
    height=1200,
    scrolling=True
)