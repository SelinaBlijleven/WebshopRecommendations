# Used libraries
import sys
import pandas as pd
import numpy as np

# Own code
import read
import correct
import save

import normalize
import similarity

# Input: Transaction file name, product file name
# Output: Evaluation of similarity measure
# Evaluation function.
def main(transaction_file, product_file, n):
	# FEATURES
	features = ['brand', 'color', 'color_web', 'fit', 'heel_height', 'heel_shape', 'main_group', 'material', 'material_inside', 'material_inner_sole', 'material_outer_sole', 'removable_footbed', 'season', 'shaft_height', 'shaft_width', 'subgroup']
	
	# READ DATA
	transactions, products = read.all(transaction_file, product_file)
	# Take smaller sample
	#transactions = transactions.sample(n)
	transactions = transactions[:n]
	# CORRECT DATA
	# Unique article numbers are already used and commented out in correct.py
	transactions, products = correct.all(transactions, products)
	
	# NORMALIZE FEATURES
	print("Normalizing features...")
	products = normalize.normalize(products, ['shaft_height', 'shaft_width', 'heel_height'])
	
	# GET REPEAT CUSTOMERS
	# Make series with amount of purchases for each customer.
	print("Getting repeat customers...")
	all_customers = transactions['customer'].value_counts()
	# List all customers with > 1 purchase.
	repeat_customers = all_customers[all_customers > 1]
	
	# Get similarity score with other purchases from customer.
	print("Calculating similarity from related purchases...")
	sims, article_ids = history_similarity(transactions, products, features, repeat_customers[1:])
	# Get average similarity score between products from sample.
	print("Calculating average similarity from sample...")
	gen_mean = average_similarity(products, features)
	
	# Get statistics
	print("Getting statistics...")
	sim_stats = get_stats(sims)
	
	# Save similarities, mean, median and standard deviation.
	print("Saving data...")
	save_results(article_ids, sims, sim_stats, gen_mean)
	
# Input: Transactions, products, features, list of customers with multiple customers
# Output: List of average similarities found with other purchases by customer.
# Calculates the average similarities for products based on purchase history of customer.
# These similarities in general should be higher than average, as we know the customer likes these.
# The similarity is calculated in the function instead of reading from file because of hardware restraints.
def history_similarity(transactions, products, features, repeat_customers):
	customers = repeat_customers.index.values.tolist()
	total_purchases = sum(repeat_customers.values)
	
	similarities = []
	article_ids = []
	
	products['article_id'].values

	for c in customers:
		# Get all purchases for customer.
		purchases = transactions[transactions['customer'] == c]
		# Get article numbers
		articles = purchases['article_id'].values
		
		for a in articles:
			if a in products['article_id'].values:
				p1 = products[products['article_id'] == a]
				avg_sim = get_similarity(products, features, p1, articles)
				
				if avg_sim != 0:
					similarities.append(avg_sim)
					article_ids.append(a)

	return similarities, article_ids

# Input: List of products, list of features, product, rest of purchase history from customer.
# Output: Average similarity for given product based on rest of purchase history.
# Calculates the average similarity with the rest of the purchase history.
def get_similarity(products, features, p1, all_articles):
	sim = 0
	no_others = len(all_articles) - 1
	
	for id in all_articles:
		# If product in product database, calculate similarity.
		if id in products['article_id'].values:
			p2 = products[products['article_id'] == id]
		
			if p1['article_id'].values != p2['article_id'].values:
				sim += similarity.cosine(features, p1.iloc[0], p2.iloc[0])
		# Else decrease amount of product used for average with one.
		else:
			no_others -= 1
	
	if no_others > 0:
		return sim / float(no_others)
	else:
		return 0
		
# Input: Products, features
# Output: Average similarity for a sample of products.
def average_similarity(products, features):
	sample_size = 500
	sample = products.sample(sample_size).index.values
	
	sim = 0
	
	for i1 in sample:
		for i2 in sample:
			if i1 != i2:
				sim += similarity.cosine(features, products.loc[i1, :], products.loc[i2, :])
	return sim / (sample_size * (sample_size - 1))
		
# Input: List of numbers
# Output: Dictionary with mean, median and standard deviation.
def get_stats(list):
	list_stats = {}
	
	list_stats['mean'] = np.mean(list)
	list_stats['median'] = np.median(list)
	list_stats['std'] = np.std(list)
	
	return list_stats
		
# Input: List of average similarities, article numbers, statistics general and customer-based.
# Output: File with average and customer-based stats, similarities and article numbers.
def save_results(article_ids, sims, sim_stats, gen_mean):
	save.array('average_similarity', ["Similarity data for items from purchase history."], "w+")
	save.array('average_similarity', ["Mean: ", sim_stats['mean'], "Median: ", sim_stats['median'], "Standard deviation: ", sim_stats['std']], "a")
	
	save.array('average_similarity', ["Similarity data average (from sample)"], "a")
	save.array('average_similarity', ["Mean: ", gen_mean], "a")
	
	save.array('average_similarity', [" "], "a")
	
	save.array('average_similarity', article_ids, "a")
	save.array('average_similarity', sims, "a")
	
if __name__ == "__main__":
	# Sample for transactions
	# Use 2735688 for all.
	n = 2735688

	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/"
	# These files contain the updated unique article IDs.
	transaction_file = path + "unique_product_transactions.csv"
	product_file = path + "unique_products.csv"
	
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	
	main(transaction_file, product_file, n)