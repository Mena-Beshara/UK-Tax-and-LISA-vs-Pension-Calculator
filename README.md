# UK Tax & Savings Calculator 💷

A comprehensive Streamlit-based web application for calculating UK income tax, National Insurance contributions, and projecting long-term savings growth comparing Lifetime ISAs (LISA) vs. workplace pensions.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📊 Key Finding: Are You Leaving £419,000 on the Table?

> **TLDR** — For UK professionals contributing £4,000/year over a full career, choosing the wrong savings vehicle isn't a small optimisation problem. The data shows a **112.8% (£419,067) difference in ROI** between a LISA and a Pension under the right conditions.

![Project Impact Dashboard](assets/impact_dashboard.png)

Most comparisons of LISA vs. Pension rely on simplified assumptions or incomplete modelling. This project takes a different approach: a **reproducible, data-driven experiment** built in Python that models both vehicles end-to-end — including UK tax bands, NI contributions, government bonus mechanics, compound growth, and management fees — then projects outcomes from your current age to 60.

The experiment used:
- **£4,000/year** contributions (LISA annual cap, maximising the government bonus)
- **Full career horizon** from age 25 to 60
- **Accurate 2025/26 UK tax rates** including Personal Allowance tapering
- **Scenario-specific tax relief** applied dynamically to pension contributions

The result: a LISA outperforms a pension by £419,067 for a basic-rate taxpayer under these conditions — a finding that isn't obvious without modelling the full picture. Want to run it against your own numbers? The Streamlit app lets you plug in your income, age, and contribution rate and see the projections instantly.

---

## ðŸŽ¯ Project Origin & Motivation

As a Data Scientist passionate about personal finance management, I'm always honing my data analysis skills to ask the right questions, uncover insights, and create visualizations that drive better decision-making. This project started when I pondered a key financial dilemma: **For long-term savings in the UK, is a Lifetime ISA (LISA) superior due to its tax-free withdrawals, or does a workplace pension win with upfront tax relief?**

Unable to find clear, data-driven answers online, I decided to build my own predictive model to analyze it.

### The Journey: From Excel to Production

**1. Research & Data Gathering**

I began by gathering verifiable data from official sources:

- **UK Tax Bands (2025/26)** from [GOV.UK](https://www.gov.uk/income-tax-rates):
  - Personal Allowance: up to Â£12,570 at 0%
  - Basic Rate: Â£12,571 to Â£50,270 at 20%
  - Higher Rate: Â£50,271 to Â£125,140 at 40%
  - Additional Rate: over Â£125,140 at 45%

- **National Insurance Rates** (employee contributions):
  - 0% up to Â£12,570/year
  - 8% on earnings between Â£12,571 and Â£50,270
  - 2% above Â£50,270

- **Historical Returns Research**:
  - UK workplace pensions: 5-8% annual growth over recent five-year periods (PensionBee, September 2024)
  - Cash LISAs: top rates above 4% AER (Moneyfacts, November 17, 2025)
  - Stocks-and-shares LISAs: can match market returns of 5-7% historically

- **LISA Rules** (HMRC guidelines):
  - Annual contribution cap: Â£4,000
  - Government bonus: 25% (up to Â£1,000 free per year)
  - Contribution age limit: 18-50

**2. Prototyping in Excel**

I organized my thoughts in Excel first, building a predictive model with formulas for:
- Compound growth calculations
- Tax breakdowns (including personal allowance tapering over Â£100,000)
- 1% LISA management fee approximation
- Projections from current age to 60

This helped me ask critical questions:
- How do varying interest rates impact outcomes?
- What visualizations best highlight differences?
- Which factors have the most significant effect on long-term savings?

I experimented with different chart types:
- Bar charts for interval comparisons
- Line graphs for growth trends
- Pie charts for income distribution

**3. Migration to Python & Jupyter**

To sharpen my Python skills and make the model dynamic, I migrated everything to a Jupyter Notebook using:
- **Pandas** for data handling and manipulation
- **Matplotlib/Seaborn** for static visualizations
- **Plotly** for interactive charts
- **NumPy** for efficient numerical computations

This made the model truly dynamicâ€”users can input their specific parameters:
- Income level
- Current age
- Weekly contributions (e.g., Â£50 for partial max)
- Expected LISA interest rate (e.g., 7%)

The result: customized projections and interactive visualizations tailored to individual circumstances.

**4. Production Web Application**

After refining the model and receiving encouragement from my mentor, I built this production-ready Streamlit application. This step taught me:
- Better code structure and modularization
- Error handling and input validation
- Creating intuitive user interfaces
- Deploying data science solutions for real-world use

The goal: make this simple yet powerful tool accessible to everyone, not just those familiar with Python or data analysis.

## ðŸ“Š Key Findings from the Analysis

After extensive modeling and scenario testing, here are the data-driven conclusions:

### 1. Higher-Rate Taxpayers (earning over Â£50,270)
**Recommendation**: Balance between LISA and pension contributions

**Why?**
- Pensions offer 40-45% tax relief (claimable via self-assessment per HMRC)
- Higher tax relief often outweighs the 25% LISA bonus
- Consider maxing out LISA (Â£4,000/year) for the guaranteed bonus, then prioritizing pension
- The tax relief on pensions becomes increasingly valuable at higher income levels

**Example**: A Â£100 pension contribution only costs you Â£60 (or even Â£55 at additional rate)

### 2. Basic-Rate Taxpayers (up to Â£50,270)
**Recommendation**: LISAs often outperform

**Why?**
- 25% LISA bonus is comparable to 20% basic-rate pension tax relief
- LISA withdrawals are completely tax-free at 60
- Pension withdrawals are subject to income tax (25% tax-free, then marginal rate)
- Greater flexibility with LISA for first-time home purchase

**Example**: Â£4,000 LISA contribution becomes Â£5,000 immediately with government bonus

### 3. Additional Insights
- **Volatility matters**: Stocks-and-shares LISAs can achieve higher returns but come with risk
- **Time horizon**: The earlier you start, the more compound growth amplifies differences
- **Tax rate changes**: If you expect your tax rate to drop in retirement, pensions become more attractive
- **Flexibility**: LISAs offer more liquidity for first-time home purchases (up to Â£450,000)

## ðŸŽ¯ Features

### Tax Calculation
- **Accurate UK Tax Bands**: Uses 2025/26 tax rates for England, Wales, and Northern Ireland
- **Personal Allowance Tapering**: Automatically calculates PA erosion for high earners (Â£100,000+)
- **National Insurance**: Includes both primary and secondary NI thresholds
- **Effective Tax Rate**: Displays your true tax burden as a percentage
- **Visual Breakdown**: Interactive pie chart showing income distribution

### Savings Projection
- **LISA vs Pension Comparison**: Side-by-side comparison of both savings vehicles
- **Tax Relief Modeling**: Accurately models pension tax relief at your marginal rate
- **LISA Government Bonus**: Includes 25% government bonus (up to Â£1,000/year)
- **Compound Growth**: Projects growth from current age to 60
- **Interactive Charts**: 
  - Plotly interactive line charts with hover details
  - Seaborn static charts with 5-year interval markers
  - Downloadable CSV data export

### User-Friendly Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Updates**: All calculations update instantly as you adjust inputs
- **Tabbed Interface**: Organized display of tax analysis, projections, and raw data
- **Input Validation**: Prevents invalid entries and provides helpful tooltips

## ðŸ“ˆ How It Works

### Tax Calculation Logic
The calculator implements the UK tax system with the following bands (2025/26):

| Income Range | Tax Rate | Notes |
|-------------|----------|-------|
| Â£0 - Â£12,570 | 0% | Personal Allowance |
| Â£12,571 - Â£50,270 | 20% | Basic Rate |
| Â£50,271 - Â£125,140 | 40% | Higher Rate |
| Â£125,140+ | 45% | Additional Rate |

**Special Rules:**
- Personal Allowance reduces by Â£1 for every Â£2 earned over Â£100,000
- National Insurance: 8% on Â£12,571-Â£50,270, then 2% above
- Completely accurate for England, Wales, and Northern Ireland (Scotland has different rates)

### LISA Calculation
A Lifetime ISA is designed for first-time homebuyers and retirement savings:

- **Government Bonus**: 25% on contributions up to Â£4,000/year (max Â£1,000 bonus)
- **Contribution Period**: From age 18-50
- **Growth Period**: Continues growing until age 60
- **Management Fees**: Assumes 1% annual fee (adjustable in code)
- **Weekly Contribution Cap**: Â£76.92/week = Â£4,000/year for max bonus

**Formula**: 
```
Year N Value = (Previous Year Ã— (1 + Interest Rate) + Annual Contribution Ã— 1.25) Ã— 0.99
```

### Pension Calculation
Workplace pensions benefit from automatic tax relief:

- **Tax Relief**: Contributions receive tax relief at your marginal rate
  - Basic rate (20%): Â£80 contribution â†’ Â£100 in pension
  - Higher rate (40%): Â£80 contribution â†’ Â£133.33 effective (via self-assessment)
  - Additional rate (45%): Â£80 contribution â†’ Â£145.45 effective
- **Contribution Period**: From current age to 50
- **Growth Rate**: Assumes 4% annual growth (conservative estimate)
- **Access**: Can access from age 55 (increasing to 57 in 2028)

**Formula**:
```
Pension Contribution = Weekly Payment Ã— 52 Ã— (1 / (1 - Tax Rate))
```

## ðŸš€ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/uk-tax-savings-calculator.git
cd uk-tax-savings-calculator
```

2. **Create a virtual environment** (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
# Using Python module syntax (recommended)
python -m streamlit run uk_tax_savings/app.py

# Or using streamlit directly
streamlit run uk_tax_savings/app.py
```

5. **Access the app**
Open your browser and navigate to:
```
http://localhost:8501
```

### ðŸŒ Web Application Access

**Not familiar with Python?** No problem! I've built a web-based version that's accessible directly through your browserâ€”no installation required.

**Contact me for access**: MenaBeshara60@gmail.com

Simply send me an email, and I'll provide you with the link to the hosted application where you can start calculating immediately!

## ðŸ“ Project Structure

```
uk-tax-savings-calculator/
â”œâ”€â”€ uk_tax_savings/
â”‚   â”œâ”€â”€ __init__.py              # Package initialization
â”‚   â”œâ”€â”€ app.py                   # Main Streamlit application
â”‚   â”œâ”€â”€ config.py                # Tax rates and constants
â”‚   â”œâ”€â”€ tax_calculator.py        # Tax and NI calculation logic
â”‚   â”œâ”€â”€ plots.py                 # Visualization functions
â”‚   â”œâ”€â”€ modeling/
â”‚   â”‚   â”œâ”€â”€ __init__.py
â”‚   â”‚   â””â”€â”€ predict.py           # Savings projection model
â”‚   â”œâ”€â”€ dataset.py               # Placeholder for data functions
â”‚   â””â”€â”€ features.py              # Placeholder for feature engineering
â”œâ”€â”€ requirements.txt             # Python dependencies
â”œâ”€â”€ pyproject.toml              # Project metadata
â”œâ”€â”€ setup.cfg                   # Linting configuration
â”œâ”€â”€ README.md                   # This file
â””â”€â”€ Makefile                    # Build commands (optional)
```

## ðŸŽ® Usage Guide

### Basic Usage

1. **Enter Your Income**: Input your gross annual income in the sidebar
2. **Set Your Age**: Enter your current age (18-49 for LISA contributions)
3. **Choose Weekly Contribution**: Decide how much you can save per week
4. **Set Expected Returns**: Adjust the expected investment growth rate
5. **Review Results**: Switch between tabs to see tax breakdown, projections, and raw data

### Example Scenarios

#### Scenario 1: Basic Rate Taxpayer
- Income: Â£35,000
- Age: 25
- Weekly Contribution: Â£50
- Expected Interest: 5%

**Result**: LISA and pension perform similarly, with LISA having slight edge due to government bonus and tax-free withdrawals.

#### Scenario 2: Higher Rate Taxpayer
- Income: Â£75,000
- Age: 30
- Weekly Contribution: Â£76.92 (max LISA)
- Expected Interest: 6%

**Result**: Pension typically outperforms LISA due to 40% tax relief vs 25% LISA bonus. Consider splitting contributions.

#### Scenario 3: Additional Rate Taxpayer
- Income: Â£150,000
- Age: 35
- Weekly Contribution: Â£100
- Expected Interest: 7%

**Result**: Pension significantly outperforms LISA (45% tax relief). Max out LISA for diversity, prioritize pension for remainder.

### Interpreting Results

**Tax Analysis Tab:**
- Shows your effective tax rate (total deductions as % of income)
- Visualizes where your money goes (take-home, tax, NI)
- Useful for understanding your true tax burden

**Savings Projection Tab:**
- Compare final values at age 60
- See when each investment overtakes the other
- Understand the impact of contribution periods vs growth periods
- Interactive charts allow you to hover for exact values

**Data Table Tab:**
- Download full year-by-year breakdown
- Useful for detailed financial planning
- Can import into Excel/Google Sheets for further analysis

## âš™ï¸ Configuration

### Modifying Tax Rates
Edit `uk_tax_savings/config.py`:

```python
# Tax constants (2025/26 UK rates)
PA = 12570                    # Personal Allowance
BR_END = 50270               # Basic Rate Band end
HR_TRAP_START = 100000       # Start of PA erosion
AR_START = 125140            # Additional Rate start

BR_TAX_RATE = 0.20           # Basic Rate: 20%
HR_TAX_RATE = 0.40           # Higher Rate: 40%
AR_TAX_RATE = 0.45           # Additional Rate: 45%
```

### Modifying Savings Assumptions
```python
PENSION_GROWTH_RATE = 0.04   # 4% annual growth
LISA_BONUS_FACTOR = 1.25     # 25% government bonus
FEE_FACTOR = 0.99            # 1% annual management fee
```

## âš ï¸ Limitations & Disclaimers

**IMPORTANT**: This is an illustrative data science tool with limitations. This calculator provides **estimates only** and does not account for:

- âŒ Student loan repayments (Plan 1, 2, 4, or Postgraduate)
- âŒ Pension salary sacrifice arrangements
- âŒ Scottish income tax rates (which differ from England/Wales/NI)
- âŒ Welsh income tax rates (minimal differences)
- âŒ Marriage allowance transfers
- âŒ Childcare vouchers or other salary sacrifice schemes
- âŒ Dividend income tax
- âŒ Capital gains tax
- âŒ Inflation adjustments
- âŒ Future changes in tax policy or rates
- âŒ Employer pension contributions (beyond tax relief)
- âŒ LISA withdrawal penalties (25% if withdrawn before 60 for non-qualifying reasons)

**Important Notes:**
- LISA withdrawals before 60 (except for first home purchase or terminal illness) incur a 25% penalty
- Pension access rules may change (currently 55, rising to 57 in 2028)
- Investment returns are not guaranteed and can be negative
- Past performance does not indicate future results

**âš–ï¸ Legal Disclaimer**: This tool is for educational and planning purposes only. It is NOT financial advice. Always check [GOV.UK](https://www.gov.uk/) for the most current tax information and consult with a qualified financial advisor before making investment decisions. Do your own research.

## ðŸ› ï¸ Development

### Running Tests
```bash
# Install development dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/
```

### Code Formatting
```bash
# Install black
pip install black

# Format code
black uk_tax_savings/
```

### Linting
```bash
# Install flake8
pip install flake8

# Run linter
flake8 uk_tax_savings/
```

## ðŸ“ Contributing

Contributions are welcome! This is a learning project, and I'm eager to collaborate with other data scientists and developers interested in fintech applications.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Scottish/Welsh tax rate support
- Student loan repayment calculations
- Salary sacrifice modeling
- Mobile responsiveness improvements
- Additional chart types
- Historical data tracking
- Multi-year comparison tools
- Inflation adjustment features
- API development for programmatic access

## ðŸ’¬ Let's Connect!

I'm passionate about data-driven finance and always looking to connect with like-minded professionals!

**Interested in discussing:**
- LISA vs. Pension strategies
- Data science in personal finance
- Financial modeling techniques
- Streamlit application development
- Open-source collaboration

**Reach out:**
- ðŸ“§ Email: MenaBeshara60@gmail.com
- ðŸ’¼ GitHub: (https://github.com/Mena-Beshara)
- ðŸ”— LinkedIn: https://www.linkedin.com/in/menabeshara/

**Thoughts on LISA vs. pension? Let's discuss!**

## ðŸ“„ License

This project is licensed under the MIT License - see the LICENSE file for details.

## ðŸ‘¤ Author

**Mena Beshara**
- Email: MenaBeshara60@gmail.com
- Role: Data Scientist passionate about personal finance and predictive modeling

## ðŸ™ Acknowledgments

- Special thanks to my mentor who encouraged me to publish this project
- Built with [Streamlit](https://streamlit.io/) - making data science applications accessible
- Visualization powered by [Plotly](https://plotly.com/) and [Seaborn](https://seaborn.pydata.org/)
- Data manipulation with [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/)
- Project structure inspired by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- UK tax information from [GOV.UK](https://www.gov.uk/income-tax-rates)
- LISA information from [Money Helper](https://www.moneyhelper.org.uk/)
- Pension data from [PensionBee](https://www.pensionbee.com/)
- LISA rates from [Moneyfacts](https://moneyfacts.co.uk/)

## ðŸ“ž Support & Feedback

If you encounter any issues, have questions, or want to provide feedback:

1. **Check existing issues**: Browse the [Issues](https://github.com/Mena-Beshara) page
2. **Create a new issue**: Provide detailed description of the problem or suggestion
3. **Email directly**: MenaBeshara60@gmail.com
4. **Request web app access**: If you're not familiar with Python, contact me for the hosted version

**Your feedback helps improve this tool for everyone!**


## ðŸ“š Additional Resources

### Official UK Tax & Savings Information
- [GOV.UK - Income Tax Rates](https://www.gov.uk/income-tax-rates)
- [GOV.UK - National Insurance Rates](https://www.gov.uk/national-insurance-rates-letters)
- [HMRC - Tax Relief on Pensions](https://www.gov.uk/tax-on-your-private-pension/pension-tax-relief)

### LISA Information
- [Money Helper - Lifetime ISA](https://www.moneyhelper.org.uk/en/savings/types-of-savings/lifetime-isas)
- [Which? - Lifetime ISA Guide](https://www.which.co.uk/money/savings-and-isas/isas/lifetime-isas-explained)
- [Moneyfacts - LISA Rates](https://moneyfacts.co.uk/savings-accounts/lifetime-isas/)

### Pension Information
- [Money Helper - Workplace Pensions](https://www.moneyhelper.org.uk/en/pensions-and-retirement/building-your-retirement-pot/workplace-pensions)
- [Pension Wise - Free Guidance](https://www.pensionwise.gov.uk/)
- [PensionBee - Performance Data](https://www.pensionbee.com/)

### Data Science & Visualization
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python](https://plotly.com/python/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)

---

**Made with â¤ï¸ for better financial planning and data-driven decision making**

*A data science project demonstrating the power of predictive modeling in personal finance*