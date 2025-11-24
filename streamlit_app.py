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

# Import all content from main app
from uk_tax_savings.app import *