import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# Page configuration
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💻",
    layout="wide"
)

# Project folder
folder = Path(__file__).parent

# Read HTML, CSS and JavaScript
html = (folder / "index.html").read_text(encoding="utf-8")
css = (folder / "style.css").read_text(encoding="utf-8")
js = (folder / "script.js").read_text(encoding="utf-8")

# Embed CSS
html = html.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>{css}</style>'
)

# Embed JavaScript
html = html.replace(
    '<script src="script.js"></script>',
    f'<script>{js}</script>'
)

# Embed profile photo
photo_path = folder / "photo.jpg"

if photo_path.exists():
    image = base64.b64encode(
        photo_path.read_bytes()
    ).decode("utf-8")

    photo_data = f"data:image/jpeg;base64,{image}"

    html = html.replace("photo.jpg", photo_data)
else:
    st.warning("Profile photo not found!")

# Display portfolio
components.html(
    html,
    height=1500,
    scrolling=True
)