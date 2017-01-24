import pandas as pd

def all(transaction_file, product_file):
	# Read transactions into dataframe
	print("Reading transactions into pandas dataframe...")
	transactions = pd.read_csv(transaction_file, encoding="ISO-8859-1")
	# Read products into dataframe
	print("Reading products into pandas dataframe...")
	products = pd.read_csv(product_file, encoding="ISO-8859-1")
	
	return transactions, products