import streamlit as st  
import pandas as pd  
import plotly.express as px  
import matplotlib.pyplot as plt  
import seaborn as sns  
import numpy as np  

# --- Tax Analysis Tab (Tab 1) ---  

def display_tax_analysis(tax_data: dict, income_pre_tax: int):  
    """Displays tax metrics and the updated Pie Chart for income breakdown."""  
    st.header("Income Breakdown")  
      
    # Metrics Row  
    col1, col2, col3, col4 = st.columns(4)  
    col1.metric("Gross Income", f"£{tax_data['income_pre_tax']:,.2f}")  
    col2.metric("Total Tax", f"£{tax_data['tax']:,.2f}")  
    col3.metric("National Insurance", f"£{tax_data['national_insurance']:,.2f}")  
    col4.metric("Take Home Pay",   
                f"£{tax_data['income_after_tax']:,.2f}",   
                delta=f"{tax_data['tax_percentage']*100:.1f}% Effective Tax")  
      
    st.divider()  
      
    # Updated Pie Chart (Simple, Closed Circle, Bigger Font, Vibrant Palette)  
    labels = ['Take-Home Pay', 'Income Tax', 'National Insurance']  
    values = [tax_data['income_after_tax'], tax_data['tax'], tax_data['national_insurance']]  
      
    # New, Visually Appealing Palette: Teal, Deep Red, Vibrant Orange  
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
        textfont_size=18   
    )  

    fig_pie.update_layout(  
        title_text="Income Distribution",  
        title_x=0.5,  
        showlegend=False  
    )  
      
    st.plotly_chart(fig_pie, width='stretch')  

# --- Savings Projection Tab (Tab 2) ---  

def display_savings_projection_charts(df: pd.DataFrame, age: int, lisa_years_contrib: int, additional_years_growth: int):  
    """Displays summary metrics, the Plotly Line chart, and the Seaborn Line chart."""  
    st.header("LISA vs Pension Comparison (To Age 60)")  
      
    lisa_final = df['LISA Value'].iloc[-1]  
    pension_final = df['Pension Value'].iloc[-1]  
    diff = pension_final - lisa_final  

    # Summary metrics  
    c1, c2, c3 = st.columns(3)  
    c1.info(f"**LISA @ 60:** £{lisa_final:,.2f}")  
    c2.success(f"**Pension @ 60:** £{pension_final:,.2f}")  
    c3.warning(f"**Difference (Pension - LISA):** £{diff:,.2f}")  

    # 1. Plotly Interactive Line Chart  
    st.subheader("Growth Over Time (Interactive)")  
    fig_line = px.line(  
        df,   
        x='Age',   
        y=['LISA Value', 'Pension Value'],  
        title='Interactive Comparison: LISA vs Pension',  
        labels={'value': 'Value (£)', 'Age': 'Age'}  
    )  
    # Add vertical line at age 50  
    age_50_index = df['Age'].where(df['Age'] == 50).first_valid_index()  
    if age_50_index is not None:  
        fig_line.add_vline(x=50, line_dash="dash", annotation_text="Age 50 (Contribs Stop)")  
          
    fig_line.update_layout(hovermode="x unified")  
    st.plotly_chart(fig_line, width='stretch')  
      
    st.divider()  
      
    # 2. Seaborn Line Chart with 5-Year Tags  
    st.subheader("Seaborn Growth Trajectory (5-Year Tags)")  

    # Prepare Data for Seaborn (Melt to long format)  
    df_long = df.melt('Age', var_name='Investment Type', value_name='Value')  

    # Setup the plot  
    fig_sns, ax = plt.subplots(figsize=(12, 7))  
    sns.set_style("whitegrid")  
      
    # Define colors for Seaborn plot  
    palette = {'LISA Value': '#1f77b4', 'Pension Value': '#d62728'}  

    # Draw the main lines  
    sns.lineplot(  
        data=df_long,   
        x='Age',   
        y='Value',   
        hue='Investment Type',   
        palette=palette,   
        linewidth=3,   
        ax=ax  
    )  

    # Logic to tag every 5 years  
    start_age = df['Age'].min()  
    end_age = df['Age'].max()  
      
    tag_ages = list(range(start_age, end_age + 1, 5))  
    if end_age not in tag_ages:  
        tag_ages.append(end_age)  

    # Filter the dataframe for only these ages  
    points_to_tag = df_long[df_long['Age'].isin(tag_ages)]  

    # Add text labels and markers  
    for _, row in points_to_tag.iterrows():  
        ax.plot(row['Age'], row['Value'], 'o', color='black', markersize=5, zorder=5)  
          
        label_text = f"£{row['Value']/1000:.0f}k"  
          
        # Offset to prevent overlap  
        if row['Investment Type'] == 'Pension Value':  
            xytext = (0, 15)   
            va = 'bottom'  
        else:  
            xytext = (0, -20)  
            va = 'top'  

        ax.annotate(  
            label_text,   
            xy=(row['Age'], row['Value']),   
            xytext=xytext,   
            textcoords='offset points',   
            ha='center',   
            va=va,  
            fontsize=10,  
            fontweight='bold',  
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="none", alpha=0.7)  
        )  

    # Final Styling  
    ax.yaxis.set_major_formatter(plt.matplotlib.ticker.StrMethodFormatter('£{x:,.0f}'))  
    ax.set_title("Projected Value at 5-Year Intervals", fontweight='bold')  
    ax.set_xlabel('Age', fontweight='bold')  
    ax.set_ylabel('Value (£)', fontweight='bold')  
    ax.grid(True, linestyle='--', alpha=0.5)  
    sns.despine()  
      
    # Render in Streamlit  
    st.pyplot(fig_sns)  
      
# --- Data Table Tab (Tab 3) ---  

def display_data_table(df: pd.DataFrame):  
    """Displays the raw data table and a download button."""  
    st.header("Detailed Data")  
    st.dataframe(df.style.format({"LISA Value": "£{:.2f}", "Pension Value": "£{:.2f}"}))  
      
    # Download button  
    csv = df.to_csv(index=False).encode('utf-8')  
    st.download_button(  
        "Download Data as CSV",  
        csv,  
        "savings_projection.csv",  
        "text/csv",  
        key='download-csv'  
    )  