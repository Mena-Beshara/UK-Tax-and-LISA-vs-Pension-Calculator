# UK Tax and LISA vs Pension Calculator

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/uk-tax-calculator)
![GitHub Last Commit](https://img.shields.io/github/last-commit/yourusername/uk-tax-calculator)

This repository contains a Jupyter Notebook (`UK_Tax_and_LISA_vs_Pension_Calculator.ipynb`) that implements a comprehensive calculator for UK income tax, National Insurance contributions, and a comparison of Lifetime ISA (LISA) versus workplace pension growth. The tool is designed for educational and estimation purposes, using the UK tax bands for the 2025/26 tax year. It provides detailed breakdowns, growth projections, and visualizations to help users understand their take-home pay and long-term savings options.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Tax Calculation Details](#tax-calculation-details)
- [LISA Calculation Details](#lisa-calculation-details)
- [Pension Calculation Details](#pension-calculation-details)
- [Visualizations](#visualizations)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description

The calculator uses the current UK tax bands to calculate your income tax and National Insurance contributions for the tax year 2025/26. It takes into account the personal allowance tapering for incomes over £100,000.

It also simulates the growth of contributions to a Lifetime ISA (LISA) and a workplace pension, projecting values up to age 60. The tool assumes user inputs for age, weekly contributions, and expected interest rates, then compares the two savings vehicles over time.

This project is built in Python using libraries like NumPy, Pandas, Matplotlib, Seaborn, Plotly, and Pygwalker for data analysis and visualization. It is ideal for personal finance planning, but **not a substitute for professional financial advice**.

## Features

- **Income Tax and NI Calculation**: Computes total tax, National Insurance, take-home pay, and deduction percentage based on annual income.
- **LISA vs Pension Comparison**: Projects growth from the user's current age to 60, including government bonuses for LISA and tax relief for pensions.
- **Interactive Visualizations**:
  - Bar chart comparing LISA and pension values at 5-year intervals.
  - Line chart showing continuous growth with markers every 5 years.
  - Pie chart for income breakdown (tax, NI, take-home pay).
  - Interactive Plotly line chart for dynamic exploration.
  - Pygwalker integration for Tableau-style data exploration.
- **Output Savings**: Charts are saved as PNG files (e.g., `tax_savings_lisa_vs_pension_bar_chart.png`).
- **User Inputs**: Prompts for income, age, weekly contributions, and LISA interest rate.
- **Edge Case Handling**: Manages scenarios like zero tax percentage or users aged 50+ (no further LISA contributions).

## Requirements

- Python 3.11+
- Jupyter Notebook or JupyterLab for running the `.ipynb` file.
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `plotly`
  - `pygwalker`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/uk-tax-calculator.git
   cd uk-tax-calculator
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not present, install manually:
   ```
   pip install numpy pandas matplotlib seaborn plotly pygwalker
   ```

4. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```
   Open `UK_Tax_and_LISA_vs_Pension_Calculator.ipynb` in your browser.

## Usage

1. Run the notebook cells sequentially.
2. When prompted:
   - Enter your annual income (e.g., £50,000).
   - Enter your current age (e.g., 30).
   - Enter weekly LISA/pension contribution (e.g., £50 for the example below).
   - Enter expected annual LISA interest rate (e.g., 7%).
3. The script will output:
   - Tax and NI breakdowns.
   - A DataFrame comparing LISA and pension growth year-by-year.
   - Key differences at ages 50 and 60.
   - Visualizations (displayed inline and saved as PNG files).
4. Explore the data interactively using the Pygwalker widget at the end.

**Note**: This calculation does not include pension contributions in the tax computation, as noted in the output.

## Examples

### Sample Input
- Annual Income: £50,000
- Age: 30
- Weekly Contribution: £50
- LISA Interest Rate: 7%

### Sample Output
```
This program calculates the Effective Tax Percentage on Income.
(Please note this calculation doesn't include Pension contribution)
Your total tax payment will be £7,486.00
Your total National Insurance will be: £2,994.40
Your Take Home pay will be: £39,519.60
Your Deductions percentage is: 20.96%
```

For the LISA vs Pension growth comparison, see the charts below for detailed projections.

LISA value at age 50: approximately £117,590  
Pension value at age 50: £97,955.20  
Difference at age 50 (Pension - LISA): -£19,635 (LISA higher)

Final LISA value at age 60: £209,160  
Final Pension value at age 60: £144,998  
Difference at age 60 (Pension - LISA): -£64,162 (LISA higher)

### An Example of the Calculations

#### User Interface Input
![Web-based Application UI](Lisa-pension-calculator.png)

#### LISA vs Pension Bar Chart
![LISA vs Pension Bar Chart](tax_savings_lisa_vs_pension_bar_chart.png)

#### LISA vs Pension Line Chart
![LISA vs Pension Line Chart](tax_savings_lisa_vs_pension_line_chart.png)

#### Income Breakdown Pie Chart
![Income Breakdown Pie Chart](income_breakdown_pie.png)

## Tax Calculation Details

- **Personal Allowance**: £12,570 (tapers for incomes over £100,000).
- **Basic Rate (20%)**: £12,571 - £50,270.
- **Higher Rate (40%)**: £50,271 - £125,140.
- **Additional Rate (45%)**: Over £125,140.
- **National Insurance**: 8% on basic band, 2% on higher/additional.
- Handles cases from no tax to additional rate payers.

## LISA Calculation Details

A Lifetime ISA (LISA) gets a 25% government bonus on contributions up to £4,000 per year (equivalent to £76.92 per week). This means for every £1 you save, the government adds 25p. You can contribute until age 50.

The calculator assumes a 1% annual management fee for the LISA and continues growth until age 60 (10 years after final contribution).

## Pension Calculation Details

Workplace pensions benefit from tax relief at your marginal rate. Basic rate taxpayers get 25% uplift (£80 contribution becomes £100 in your pension), while higher rate taxpayers can claim additional relief through self-assessment.

The calculator assumes a 4% annual growth rate for the pension after contributions stop at age 50, continuing until age 60.

## Visualizations

- **Bar Chart**: Compares values at 5-year intervals, saved as `tax_savings_lisa_vs_pension_bar_chart.png`.
- **Line Chart**: Shows continuous growth with markers, saved as `tax_savings_lisa_vs_pension_line_chart.png`.
- **Pie Chart**: Income breakdown, saved as `income_breakdown_pie.png`.
- **Interactive Plotly Chart**: Hover for details.
- **Pygwalker**: Drag-and-drop data exploration interface.

## Limitations

This calculator provides estimates only and doesn't account for:

- Student loan repayments
- Pension salary sacrifice arrangements
- Marriage allowance transfer
- Other deductions like childcare vouchers
- Inflation or changes in tax policy

Tax rules can change; always verify with official sources like HMRC.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss.

1. Fork the repo.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed by me and it has been developed by Mena-Beshara.

## Contact

- Author: [Mena-Beshara]
- GitHub: [Mena-Beshara](https://github.com/mena-beshara)
- Email: your.email@example.com

For questions or suggestions, feel free to open an issue!
