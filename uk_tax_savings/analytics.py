import streamlit as st  
import numpy as np  
import pandas as pd  
from uk_tax_savings.tax_calculator import calculate_tax_and_ni  
from uk_tax_savings.modeling.predict import run_savings_projection  
from uk_tax_savings.plots import (  
    display_tax_analysis,   
    display_savings_projection_charts,   
    display_data_table  
)
# NEW: Import analytics functions
from uk_tax_savings.analytics import (
    inject_google_analytics, 
    display_analytics_notice,
    track_event
)

# --- Page Configuration ---  
st.set_page_config(  
    page_title="UK Tax & Savings Calculator",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# --- Google Analytics Integration ---
# Try to load GA ID from secrets, fallback to None for local dev
try:
    GA_MEASUREMENT_ID = st.secrets["analytics"]["google_analytics_id"]
    inject_google_analytics(GA_MEASUREMENT_ID)
except (KeyError, FileNotFoundError):
    # No analytics in development mode
    GA_MEASUREMENT_ID = None
    pass

# --- Title & Intro ---  
st.title("💷 UK Tax, LISA & Pension Calculator")  
st.markdown("""  
This application calculates your **Effective Tax Percentage** and projects the growth of a **LISA vs. Pension** based on your contributions and tax relief benefits.  
""")

# --- Display Analytics Notice ---
display_analytics_notice()

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

# --- Core Logic Execution ---  

# Track calculation event
if GA_MEASUREMENT_ID:
    # Determine income bracket for analytics (no specific amounts)
    if income_pre_tax <= 12570:
        bracket = "below_personal_allowance"
    elif income_pre_tax <= 50270:
        bracket = "basic_rate"
    elif income_pre_tax <= 125140:
        bracket = "higher_rate"
    else:
        bracket = "additional_rate"
    
    track_event('tax_calculation', {
        'income_bracket': bracket,
        'age_group': f"{(age // 10) * 10}s"  # e.g., "20s", "30s"
    })

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
    if GA_MEASUREMENT_ID:
        track_event('view_tax_analysis')

with tab2:  
    lisa_years_contrib = 51 - (age + 1)  
    additional_years_growth = 10  
      
    display_savings_projection_charts(  
        comparison_df,   
        age=age + 1,   
        lisa_years_contrib=lisa_years_contrib,   
        additional_years_growth=additional_years_growth  
    )
    if GA_MEASUREMENT_ID:
        track_event('view_savings_projection')

with tab3:  
    display_data_table(comparison_df)
    if GA_MEASUREMENT_ID:
        track_event('view_data_table')

# Footer  
st.markdown("---")  
st.caption("Note: Tax calculations are estimates based on standard 2025/26 UK rates (England/NI) and do not include specific factors like student loans, council tax, or specific tax codes. All savings projections assume contributions are made from post-tax income.")