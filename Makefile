.PHONY: run lint test  

run:  
	streamlit run uk_tax_savings/app.py  

lint:  
	flake8 uk_tax_savings  

test:  
	pytest uk_tax_savings  