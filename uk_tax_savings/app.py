import streamlit as st  
import streamlit.components.v1 as components
import numpy as np  
import pandas as pd  
from uk_tax_savings.tax_calculator import calculate_tax_and_ni  
from uk_tax_savings.modeling.predict import run_savings_projection  
from uk_tax_savings.plots import (  
    display_tax_analysis,   
    display_savings_projection_charts,   
    display_data_table  
)

# --- Page Configuration ---  
st.set_page_config(  
    page_title="UK Tax & Savings Calculator",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# --- SIMPLE CONSENT SYSTEM ---

# Initialize session state
if 'cookies_accepted' not in st.session_state:
    st.session_state.cookies_accepted = None

def add_google_analytics():
    """Add Google Analytics tracking"""
    GA_ID = "G-7RBX8SVNNC"  
    
    ga_code = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{GA_ID}', {{
            'anonymize_ip': true,
            'allow_google_signals': false,
            'allow_ad_personalization_signals': false
        }});
    </script>
    """
    components.html(ga_code, height=0)

# --- SHOW CONSENT DIALOG ---
if st.session_state.cookies_accepted is None:
    # Create a centered container
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    border-radius: 15px; color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);'>
            <h1 style='margin: 0; font-size: 48px;'>🍪</h1>
            <h2 style='margin: 20px 0 10px 0;'>Cookie Consent</h2>
            <p style='font-size: 16px; opacity: 0.95; line-height: 1.6;'>
                Welcome to the UK Tax & Savings Calculator!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Information box
        st.info("""
        **We use cookies and analytics to improve your experience.**
        
        **What we collect:**
        - ✓ Anonymous usage patterns
        - ✓ Page views and interactions  
        - ✓ Device and browser information
        - ✓ General location (country/city)
        
        **What we DON'T collect:**
        - ✗ Your income or calculation data
        - ✗ Personal information
        - ✗ Anything that identifies you
        """)
        
        st.success("🔒 All data is anonymous and GDPR compliant")
        
        # Consent buttons
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("✓ Accept All Cookies", type="primary", use_container_width=True):
                st.session_state.cookies_accepted = True
                st.rerun()
        
        with col_btn2:
            if st.button("✗ Decline", use_container_width=True):
                st.session_state.cookies_accepted = False
                st.rerun()
        
        st.caption("You can change your choice anytime in the sidebar settings.")
    
    st.stop()  # Don't show the rest of the app until consent is given

# --- Load Analytics if Accepted ---
if st.session_state.cookies_accepted:
    add_google_analytics()

# --- Main App Content ---
st.title("💷 UK Tax, LISA & Pension Calculator")  
st.markdown("""  
This application calculates your **Effective Tax Percentage** and projects the growth of a **LISA vs. Pension** based on your contributions and tax relief benefits.  
""")

# Show consent status badge
if st.session_state.cookies_accepted:
    st.success("✓ Analytics enabled")
else:
    st.info("📊 Analytics disabled - You can still use all features!")

# --- Sidebar Inputs ---  
st.sidebar.header("User Inputs")  

try:  
    income_pre_tax = st.sidebar.number_input(  
        "Total Yearly Income (£)",   
        min_value=0,   
        value=35000,   
        step=1000,  
        help="Enter your total gross income before tax."  
    )  
      
    age = st.sidebar.number_input(  
        "Current Age",   
        min_value=18,   
        max_value=49,   
        value=25,  
        step=1,  
        help="You must be under 50 to open/contribute to a LISA."  
    )  
      
    weekly_payments = st.sidebar.number_input(  
        "Weekly Contribution (£)",   
        min_value=0.0,   
        value=50.0,   
        step=10.0  
    )  
      
    lisa_interest_input = st.sidebar.number_input(  
        "Expected LISA/Investment Interest (Yearly %)",   
        min_value=0.0,   
        value=5.0,   
        step=0.5  
    )  
    lisa_interest = lisa_interest_input / 100  

except Exception as e:  
    st.error(f"Error in input values: {e}")  
    st.stop()

# --- Cookie Settings in Sidebar ---
st.sidebar.markdown("---")
st.sidebar.subheader("🍪 Cookie Settings")

# Show current status
if st.session_state.cookies_accepted:
    st.sidebar.success("Status: Analytics Enabled")
else:
    st.sidebar.info("Status: Analytics Disabled")

# Reset button
if st.sidebar.button("Change Cookie Preferences", use_container_width=True):
    st.session_state.cookies_accepted = None
    st.rerun()

# Privacy policy
with st.sidebar.expander("📋 Privacy Policy"):
    st.markdown("""
    **Data Collection:**
    - Only anonymous usage data
    - No personal financial information
    - GDPR & UK law compliant
    
    **Contact:** MenaBeshara60@gmail.com
    """)

# --- Core Logic Execution ---  

# 1. Run Tax Calculation  
tax_data = calculate_tax_and_ni(income_pre_tax)  
tax_data['income_pre_tax'] = income_pre_tax  

# 2. Run Savings Projection  
comparison_df = run_savings_projection(  
    age=age + 1,
    weekly_payments=weekly_payments,  
    lisa_interest=lisa_interest,  
    tax_percentage=tax_data['tax_percentage']  
)  

# --- DISPLAY RESULTS ---  

tab1, tab2, tab3 = st.tabs(["💰 Tax Analysis", "📈 Savings Projection", "📊 Data Table"])  

with tab1:  
    display_tax_analysis(tax_data, income_pre_tax)

with tab2:  
    lisa_years_contrib = 51 - (age + 1)  
    additional_years_growth = 10  
      
    display_savings_projection_charts(  
        comparison_df,   
        age=age + 1,   
        lisa_years_contrib=lisa_years_contrib,   
        additional_years_growth=additional_years_growth  
    )

with tab3:  
    display_data_table(comparison_df)

# Footer  
st.markdown("---")
st.caption("Note: Tax calculations are estimates based on standard 2025/26 UK rates (England/NI) and do not include specific factors like student loans, council tax, or specific tax codes. All savings projections assume contributions are made from post-tax income.")