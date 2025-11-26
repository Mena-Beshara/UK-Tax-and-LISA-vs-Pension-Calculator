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
    initial_sidebar_state="collapsed"  # Changed to collapsed for mobile
)  

# --- Custom CSS for Mobile Responsiveness ---
st.markdown("""
<style>
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        /* Reduce padding on mobile */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        /* Make metric values smaller on mobile */
        [data-testid="stMetricValue"] {
            font-size: 1.2rem;
        }
        
        /* Make metric labels smaller */
        [data-testid="stMetricLabel"] {
            font-size: 0.8rem;
        }
        
        /* Reduce title size on mobile */
        h1 {
            font-size: 1.5rem !important;
        }
        
        h2 {
            font-size: 1.3rem !important;
        }
        
        h3 {
            font-size: 1.1rem !important;
        }
        
        /* Make tabs more compact */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 0.75rem;
            font-size: 0.85rem;
        }
        
        /* Reduce chart heights on mobile */
        .js-plotly-plot {
            height: 300px !important;
        }
        
        /* Make number inputs more compact */
        .stNumberInput input {
            font-size: 0.9rem;
        }
    }
    
    /* Ensure charts are responsive */
    .js-plotly-plot .plotly {
        width: 100% !important;
        height: 100% !important;
    }
    
    /* Make dataframe scrollable on mobile */
    .dataframe-container {
        overflow-x: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- Title & Intro ---  
st.title("💷 UK Tax, LISA & Pension Calculator")  
st.markdown("""  
Calculate your **Effective Tax %** and compare **LISA vs. Pension** growth.  
""")  

# --- Sidebar Inputs ---  
st.sidebar.header("📊 User Inputs")  

try:  
    income_pre_tax = st.sidebar.number_input(  
        "Yearly Income (£)",   
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
        "Expected LISA Interest (Yearly %)",   
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

tab1, tab2, tab3 = st.tabs(["💰 Tax", "📈 Savings", "📊 Data"])  

with tab1:  
    st.header("Income Breakdown")
    
    # Responsive metrics - use 2 columns on mobile, 4 on desktop
    # First row
    col1, col2 = st.columns(2)  
    col1.metric("Gross Income", f"£{tax_data['income_pre_tax']:,.0f}")  
    col2.metric("Total Tax", f"£{tax_data['tax']:,.0f}")  
    
    # Second row
    col3, col4 = st.columns(2)
    col3.metric("National Insurance", f"£{tax_data['national_insurance']:,.0f}")  
    col4.metric("Take Home", 
                f"£{tax_data['income_after_tax']:,.0f}",   
                delta=f"{tax_data['tax_percentage']*100:.1f}% Tax")  
    
    st.divider()
    
    # Display the pie chart from the plots module
    from uk_tax_savings.plots import display_tax_analysis
    
    # Pie Chart
    labels = ['Take-Home Pay', 'Income Tax', 'National Insurance']  
    values = [tax_data['income_after_tax'], tax_data['tax'], tax_data['national_insurance']]  
    
    import plotly.express as px
    vibrant_palette = ['#00A9A5', '#D81E5B', '#FF9505']   

    fig_pie = px.pie(  
        names=labels,   
        values=values,   
        color_discrete_sequence=vibrant_palette  
    )  

    fig_pie.update_traces(  
        textposition='inside',   
        textinfo='percent+label',  
        hovertemplate='%{label}: <br>£%{value:,.2f}</br>',  
        marker=dict(line=dict(color='#000000', width=1)),  
        textfont_size=14  # Smaller font for mobile
    )  

    fig_pie.update_layout(  
        title_text="Income Distribution",  
        title_x=0.5,  
        showlegend=False,
        height=350  # Fixed height for mobile
    )  
    
    st.plotly_chart(fig_pie, use_container_width=True)

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
st.caption("**Note:** Tax calculations are estimates based on 2025/26 UK rates (England/NI). Savings projections assume post-tax contributions.")