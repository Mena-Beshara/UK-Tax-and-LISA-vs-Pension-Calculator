import numpy as np  
# FIXED: Changed to absolute import
from uk_tax_savings.config import (  
    PA, BR_END, HR_TRAP_START, AR_START,  
    BR_TAX_RATE, HR_TAX_RATE, AR_TAX_RATE,  
    NI_BR_RATE, NI_HR_RATE  
)  

def calculate_tax_and_ni(income_pre_tax: int) -> dict:  
    """  
    Calculates UK Income Tax and National Insurance (NI) based on gross yearly income.  
    Assumes standard Personal Allowance (PA) and tax bands for England/NI.  
    Does not include Scottish/Welsh rates or employee pension contributions.  
    """  
    tax = 0  
    national_insurance = 0  
      
    # --- 1. Determine Taxable Income and PA ---  
    personal_allowance = PA  
    taxable_income = income_pre_tax - PA  

    if income_pre_tax > HR_TRAP_START and income_pre_tax < AR_START:  
        # Personal Allowance erosion (£1 lost for every £2 over £100,000)  
        pa_lost = (income_pre_tax - HR_TRAP_START) / 2  
        personal_allowance = max(0, PA - pa_lost)  
        taxable_income = income_pre_tax - personal_allowance  
    elif income_pre_tax >= AR_START:  
        # PA is completely removed  
        personal_allowance = 0  
        taxable_income = income_pre_tax  

    # --- 2. Calculate Income Tax ---  
      
    # Taxable income above £50,270 (Higher Rate/Additional Rate)  
    if taxable_income > (BR_END - personal_allowance):  
        br_taxable = (BR_END - personal_allowance)  
        hr_ar_taxable = taxable_income - br_taxable  

        # Basic Rate Tax  
        tax += br_taxable * BR_TAX_RATE  
          
        # Higher/Additional Rate Tax  
        if income_pre_tax > AR_START:  
            # Additional Rate segment  
            ar_taxable = income_pre_tax - AR_START  
            hr_taxable = AR_START - BR_END  
              
            tax += hr_taxable * HR_TAX_RATE  
            tax += ar_taxable * AR_TAX_RATE  
              
        else: # Only Higher Rate segment applies  
            tax += hr_ar_taxable * HR_TAX_RATE  
      
    # Taxable income within Basic Rate band  
    elif taxable_income > 0:  
        tax += taxable_income * BR_TAX_RATE  
      
    # --- 3. Calculate National Insurance (NI) ---  
      
    # Taxable NI starts at £12,570  
    ni_eligible_income = max(0, income_pre_tax - PA)  
      
    if ni_eligible_income > 0:  
        # Income above £50,270 (Higher Rate NI)  
        if ni_eligible_income > (BR_END - PA):  
            ni_br_band = (BR_END - PA)  
            ni_hr_band = ni_eligible_income - ni_br_band  
              
            national_insurance += ni_br_band * NI_BR_RATE  
            national_insurance += ni_hr_band * NI_HR_RATE  
          
        # Income within Basic Rate NI band  
        else:  
            national_insurance += ni_eligible_income * NI_BR_RATE  

    # --- 4. Final Calculations ---  
    income_after_tax = income_pre_tax - tax - national_insurance  
    total_deductions = tax + national_insurance  
    tax_percentage = total_deductions / income_pre_tax if income_pre_tax > 0 else 0  

    return {  
        "tax": tax,  
        "national_insurance": national_insurance,  
        "income_after_tax": income_after_tax,  
        "total_deductions": total_deductions,  
        "tax_percentage": tax_percentage,  
    }