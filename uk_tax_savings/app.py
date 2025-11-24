import streamlit as st  
import numpy as np  
import pandas as pd  
# Import the modular components - FIXED: Changed to absolute imports
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

# --- Title & Intro ---  
st.title("💷 UK Tax, LISA & Pension Calculator")  
st.markdown("""  
This application calculates your **Effective Tax Percentage** and projects the growth of a **LISA vs. Pension** based on your contributions and tax relief benefits.  
""")  

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
      
    # Age is adjusted to next birthday (age + 1) in the savings model,   
    # but the input label should reflect current age. Max age is 49 for LISA rules.  
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

# 1. Run Tax Calculation  
tax_data = calculate_tax_and_ni(income_pre_tax)  

# Add gross income back to the dict for the UI display  
tax_data['income_pre_tax'] = income_pre_tax  

# 2. Run Savings Projection  
# Pass the calculated effective tax rate to the savings model  
comparison_df = run_savings_projection(  
    age=age + 1, # Use next birthday in calculation, as per original script logic  
    weekly_payments=weekly_payments,  
    lisa_interest=lisa_interest,  
    tax_percentage=tax_data['tax_percentage']  
)  

# --- DISPLAY RESULTS (Calling Visualization Functions) ---  

tab1, tab2, tab3 = st.tabs(["💰 Tax Analysis", "📈 Savings Projection", "📊 Data Table"])  

with tab1:  
    display_tax_analysis(tax_data, income_pre_tax)  

with tab2:  
    # Need to pass contribution periods for chart annotations  
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