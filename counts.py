import pandas as pd

# Input: List of items + item label
# Output: Number of items
# Counts and prints number of items. (Used for both transactions + products)
def get(items, label):
	no_items = len(items)
	print("Total amount of " + label + ": " + str(no_items) + "\n")
	return no_items
	
# Input: Transactions
# Output: Average transactions per customer, max transactions per customer
# Calculates the average and maximum amount of purchases per customer. (Anonymous customers excluded)
def transactions_per_customer(transactions):
	customers = transactions['customer'].value_counts()
	no_customers = len(customers) - 1
	
	# Customers[0] is unknown customer; Accounts for 500K purchases.
	unknown = customers[0]
	# Customers[1] is the most frequent buyer.
	max = customers[1]
	avg = ((len(transactions) - customers[0]) / no_customers) 
	
	print("Amount of transactions by unknown customers: " + str(unknown))
	print("Amount of unique customers: " + str(no_customers))
	print("Maximum amount of articles bought by customer: " + str(max))
	print("Average amount of purchases per customer: " + str(avg) + "\n")
	
	return unknown, avg, max

# Input: Transactions, translation map between ID and ID description
# Output: Description frequencies in transactions
# Translates an ID into a description (using a given map) where possible.
def get_frequencies(transactions, id_map, id_type):
	ids = transactions[id_type].values
	descriptions = []
	
	missing = 0
	
	for id in ids:
		if id in id_map.keys():
			descriptions.append(id_map[id])
		# Include article numbers with missing description data.
		else:
			missing += 1
	
	translations = pd.Series(descriptions)
	return translations.value_counts(), missing