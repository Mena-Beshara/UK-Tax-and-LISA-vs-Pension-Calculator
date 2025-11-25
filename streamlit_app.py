"""
Streamlit App Entry Point
Usage: streamlit run streamlit_app.py
"""
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Quick Google Analytics injection for Streamlit (body injection).
# Replace `G-XXXXXXX` with your Measurement ID. This injects the
# gtag script into the page body via Streamlit's HTML support.
import streamlit as st

GA_SNIPPET = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-7RBX8SVNNC"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);} 
    gtag('js', new Date());
    gtag('config', 'G-7RBX8SVNNC', { 'send_page_view': true });
</script>
"""

# Inject snippet before the app UI renders. Note: this places the
# script in the page body, not the HTML <head> (Streamlit doesn't
# provide head access). For proper head insertion use a front-end
# proxy or host-level index.html.
st.markdown(GA_SNIPPET, unsafe_allow_html=True)

# Import all content from main app
from uk_tax_savings.app import *