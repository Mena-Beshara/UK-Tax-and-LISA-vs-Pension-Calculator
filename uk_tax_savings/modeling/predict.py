import pandas as pd  
# FIXED: Changed to absolute import
from uk_tax_savings.config import PENSION_GROWTH_RATE, LISA_BONUS_FACTOR, WEEKS_IN_YEAR, FEE_FACTOR  

def run_savings_projection(age: int, weekly_payments: float, lisa_interest: float, tax_percentage: float) -> pd.DataFrame:  
    """  
    Projects the growth of a Lifetime ISA (LISA) vs. a Pension from the current age to age 60.  

    Args:  
        age: Current age (assumed next birthday).  
        weekly_payments: Weekly contribution (£) to the savings vehicle.  
        lisa_interest: Expected annual interest/growth rate for LISA (0.05 for 5%).  
        tax_percentage: The effective tax/NI deduction rate from income (used for pension relief).  

    Returns:  
        A pandas DataFrame with 'Age', 'LISA Value', and 'Pension Value'.  
    """  
      
    # Constants moved to config  
    # (Rest of the original code from savings_model.py remains unchanged)  
    lisa_years_contrib = 51 - age  
    if lisa_years_contrib <= 0:  
        return pd.DataFrame({'Age': [], 'LISA Value': [], 'Pension Value': []})  

    additional_years_growth = 10   

    annual_contribution = weekly_payments * WEEKS_IN_YEAR  
    lisa_1st_year = annual_contribution * LISA_BONUS_FACTOR  

    if tax_percentage == 0:  
        pension_1st_year = annual_contribution    
    else:  
        pension_1st_year = annual_contribution * (1 / (1 - tax_percentage))  

    lisa_values = [lisa_1st_year]  
    pension_values = [pension_1st_year]  

    for i in range(1, lisa_years_contrib):  
        lisa_annual_contribution = annual_contribution * LISA_BONUS_FACTOR  
        lisa_new_balance = ((lisa_values[i-1] * (1 + lisa_interest) + lisa_annual_contribution)) * FEE_FACTOR  
        lisa_values.append(lisa_new_balance)  
          
        if tax_percentage == 0:  
            pension_annual_contribution = annual_contribution  
        else:  
            pension_annual_contribution = annual_contribution * (1 / (1 - tax_percentage))  
              
        pension_new_balance = pension_values[i-1] * (1 + PENSION_GROWTH_RATE) + pension_annual_contribution  
        pension_values.append(pension_new_balance)  

    lisa_total_50 = lisa_values[-1]  
    pension_total_50 = pension_values[-1]  

    lisa_extended_values = [lisa_total_50]  
    pension_extended_values = [pension_total_50]  

    for i in range(1, additional_years_growth + 1):  
        lisa_new_balance = (lisa_extended_values[i-1] * (1 + lisa_interest)) * FEE_FACTOR  
        lisa_extended_values.append(lisa_new_balance)  
          
        pension_new_balance = pension_extended_values[i-1] * (1 + PENSION_GROWTH_RATE)  
        pension_extended_values.append(pension_new_balance)  

    all_lisa_values = lisa_values + lisa_extended_values[1:]  
    all_pension_values = pension_values + pension_extended_values[1:]  
    all_years = list(range(age, age + lisa_years_contrib + additional_years_growth))  

    comparison = pd.DataFrame({  
        'Age': all_years,  
        'LISA Value': all_lisa_values,  
        'Pension Value': all_pension_values  
    })  
      
    return comparison