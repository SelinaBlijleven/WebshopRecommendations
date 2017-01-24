# Author: Selina Blijleven
# Student Number: 10574689

# Problems are indicated in comments with !!!

# Used libraries/functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial.distance import cosine

# My scripts
import read
import correct
import save

import counts
import returns

import correct

import property_frequencies
import lines

import normalize
import similarity

def main(transaction_file, product_file):
	# FEATURES
	features = ['brand', 'color', 'color_web', 'fit', 'heel_height', 'heel_shape', 'main_group', 'material', 'material_inside', 'material_inner_sole', 'material_outer_sole', 'removable_footbed', 'season', 'shaft_height', 'shaft_width', 'subgroup']
	
	# DATAFRAMES
	transactions, products = read.all(transaction_file, product_file)
	
	# RETURNS
	# Get list of returns and number of returns.
	print("Counting number and percentage of returns...")
	no_transactions = counts.get(transactions, "transactions")
	returned_transactions, no_returns = returns.get(transactions, no_transactions)
	
	# CORRECT DATA
	# Unique article numbers are already used and commented out in correct.py
	print("Correcting data...")
	transactions, products = correct.all(transactions, products)
	
	# TRANSACTION & PRODUCT COUNT
	print("Counting transactions and products...")
	# Get number of transactions
	no_transactions = counts.get(transactions, "transactions")
	# Get average transactions per customer + max per customer
	unknown, avg_transactions, max_transactions = counts.transactions_per_customer(transactions)
	# Get number of products
	no_products = counts.get(products, "products")
	
	# PLOT FREQUENCIES PROPERTY VALUES
	# Make and save plots for product properties. Figures are saved in folder /output/.
	#print("Plotting frequencies for article property values...")
	#property_frequencies.plot(transactions, products)
	
	# Print lines x until y from all transactions.
	#print("Getting selected lines...")
	#selected_lines = lines.select(transactions, 0, 3)
	
	# NORMALIZE FEATURES
	print("Normalizing features...")
	products = normalize.normalize(products, ['shaft_height', 'shaft_width', 'heel_height'])
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
	
	# Similarity is calculated per product and appended to similarity file.
	# The similarity matrix can not be made at once because of memory constraints.
	for i in range(m):
		p1 = article_ids[i]
	
		# Write header to file, overwriting the file if necessary
		save.array("Similarity/" + str(p1), ["article_id", "similarity"], "w+")
	
		for j in range(m):
			if i != j:
				p2 = article_ids[j]
				sim = similarity.cosine(features, products.loc[i, :], products.loc[j, :])
				save.array("Similarity/" + str(p1), [p2, sim])
		
# Main function
if __name__ == "__main__":
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/"
	#transaction_file = path + "small_product_transactions.csv"
	transaction_file = path + "unique_product_transactions.csv"
	#product_file = path + "20160429_products.csv"
	product_file = path + "unique_products.csv"
	main(transaction_file, product_file)