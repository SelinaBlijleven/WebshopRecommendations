# Author: Selina Blijleven
# Student Number: 10574689

# Problems are indicated in comments with !!!

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

from scipy.spatial.distance import cosine

def main(transaction_file, product_file):
	transactions = pd.read_csv(transaction_file)
	products = pd.read_csv(product_file)
	
	# Get number of transactions.
	no_transactions = get_item_count(transactions, "transactions")
	# Get number of products.
	no_products = get_item_count(products, "products")
	
	# Get list of returns and number of returns.
	returns, no_returns = get_returns(transactions, no_transactions)
	
	# Pairs color ID with color description
	colour_descriptions = get_colour_descriptions(products)
	
	# Get frequencies per color ID.
	colour_counts = get_colour_counts(transactions, colour_descriptions)
	# Plot frequencies
	plot_colour_counts(colour_counts)
	
	# Print lines x until y from all transactions.
	#selected_lines = get_lines(transactions, 0, 3)
	
	#get_similarity(products)
	
# Input: List of items
# Output: Number of items
# Counts and prints number of items. (Used for both transactions + products)
def get_item_count(items, label):
	no_items = len(items)
	print("Total amount of " + label + ": " + str(no_items) + "\n")
	return no_items
	
# Input: List of transactions, number of transactions
# Output: List of returns, percentage of returns
# Provides return information.
def get_returns(transactions, no_transactions):
	returns = transactions[transactions.quantity == -1]
	no_returns = len(returns)
	print("Amount of returns: " + str(no_returns))
	print("Percentage of returns: " + str(no_returns/no_transactions * 100) + "\n")
	return returns, no_returns
	
# Input: List of transactions, start index, end index
# Output: Lines between indices from transactions.
# Used for selecting lines between indices.
def get_lines(transactions, x, y):
	lines = transactions[x:y]
	print("Selected lines from " + str(x) + " to " + str(y) + ":")
	print(str(lines) + "\n")
	return lines
	
# !!! Missing colours in series.
# Input: Products
# Output: Descriptions for color IDs
# Links each color ID to its description in products, without
# duplicates.
def get_colour_descriptions(products):
	map = pd.Series(products.color, index=products.color_id)
	map = map.drop_duplicates()
	return map
	
# Input: List of transactions
# Output: Frequencies per color with description
def get_colour_counts(transactions, colour_descriptions):
	colour_counts = transactions.color_id.value_counts()
	colour_counts = translate_colour(colour_counts, colour_descriptions)
	return colour_counts

# Input: Colour frequencies with IDs
# Output: Colour frequencies with color descriptions
# Translates a colour ID into a description where possible.	
def translate_colour(colour_counts, colour_description):
	ids = (colour_counts.index)
	descriptions = []
	
	for id in ids:
		description = colour_description.get(id, default=None)
		if description != None:
			descriptions.append(description)
		else:
			descriptions.append(id)
	
	return pd.Series(colour_counts.values, index=descriptions)

# Input: Colour frequency counts
# Output: Plot of frequencies	
def plot_colour_counts(colour_counts):
	colour_counts.plot(kind='bar')
	
	plt.title("Amount of transactions per color")
	plt.xlabel("Color ID")
	plt.ylabel("Frequency in transaction")
	
	plt.tight_layout()
	plt.show()
	
def get_similarity(products):
	# No. of products
	m = len(products)
	# Similarity matrix
	sim = np.zeros((m, m))
	
	for i in range(m):
		for j in range(m):
			sim[i][j] = cosine(products[i,products[i, 'color_id']], products[j,products[j, 'color_id']])
			
	print(sim)
	
	
# Main function
if __name__ == "__main__":
	transaction_file = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/20160429_product_transactions.csv"
	product_file = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/20160429_products.csv"
	main(transaction_file, product_file)