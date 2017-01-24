# Author: Selina Blijleven
# Student Number: 10574689

# Problems are indicated in comments with !!!

# Used libraries/functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import cosine

# My scripts
import save
import counts
import returns

import correct_ranges
import filter_products
import property_frequencies
import lines

import normalize
import product_similarity

def main(transaction_file, product_file):
	# FEATURES
	features = ['brand', 'color', 'color_web', 'fit', 'heel_height', 'heel_shape', 'main_group', 'material', 'material_inside', 'material_inner_sole', 'material_outer_sole', 'removable_footbed', 'season', 'shaft_height', 'shaft_width', 'subgroup']
	
	# DATAFRAMES
	# Read transactions into dataframe
	print("Reading transactions into pandas dataframe...")
	transactions = pd.read_csv(transaction_file)
	# Read products into dataframe
	print("Reading products into pandas dataframe...")
	products = pd.read_csv(product_file)
	
	# CORRECT DATA
	#print("Correcting data...")
	# Remove not-for-sale products
	products = filter_products.remove_nonsale(products)
	# Remove returned products
	transactions = filter_products.remove_returns(transactions)
	# Correct heel height to ranges
	#products = correct_ranges.correct_heel(products)
	# Correct shaft height to ranges
	products = correct_ranges.correct_shaft(products, 'shaft_height')
	# Correct shaft width to ranges
	products = correct_ranges.correct_shaft(products, 'shaft_width')
	
	# TRANSACTION & PRODUCT COUNT
	#print("Counting transactions and products...")
	# Get number of transactions
	#no_transactions = counts.get(transactions, "transactions")
	# Get average transactions per customer + max per customer
	#avg_transactions, max_transactions = counts.transactions_per_customer(transactions)
	# Get number of products
	#no_products = counts.get(products, "products")
	
	# RETURNS (Cannot be used after removing returns under CORRECT DATA)
	# Get list of returns and number of returns.
	#print("Counting number and percentage of returns...")
	#returned_transactions, no_returns = returns.get(transactions, no_transactions)
	
	# PLOT FREQUENCIES PROPERTY VALUES
	# Make and save plots for product properties. Figures are saved in folder /output/.
	#print("Plotting frequencies for article property values...")
	#property_frequencies.plot(transactions, products)
	
	# Print lines x until y from all transactions.
	#print("Getting selected lines...")
	#selected_lines = lines.select(transactions, 0, 3)
	
	# NORMALIZE FEATURES
	print("Normalizing features...")
	products = normalize.normalize(products, ['shaft_height'])
	# CALCULATE PRODUCT SIMILARITY
	print("Calculating product similarity...")
	get_similarity(products, features)

# Input: Product vectors
# Output: Similarity matrix for products
# Similarity matrix for products (No strings accepted!)
def get_similarity(products, features):
	# No. of products
	m = len(products)
	# Save article numbers on first line
	article_ids = products['article_id'].values
	# Write header to file, overwriting the file if necessary
	save.array("similarity_products", article_ids, "w")
	
	# Similarity is calculated per product and appended to similarity file.
	# The similarity matrix can not be made at once because of memory constraints.
	for i in range(m):
		# Similarity array
		sim = np.ones((m))
		
		for j in range(m):
			sim[j] = product_similarity.cosine(features, products.loc[i, :], products.loc[j, :])
		save.array("similarity_products", sim)
		
# Main function
if __name__ == "__main__":
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/"
	transaction_file = path + "small_product_transactions.csv"
	#transaction_file = path + "20160429_product_transactions.csv"
	product_file = path + "small_products.csv"
	#product_file = path + "20160429_products.csv"
	main(transaction_file, product_file)