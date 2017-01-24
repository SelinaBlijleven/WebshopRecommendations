# Used libraries
import pandas as pd

# Correction + filter code
import correct_ranges
import correct_identifiers
import filter

# Input: Raw data
# Output: Filtered + corrected data
def all(transactions, products):
	print("Correcting data...")
	
	# Append color number to article_id
	# This takes some time, so the /Data folder contains the updated .csv files.
	#print("Updating article numbers in products...")
	#products = correct_identifiers.correct(products, "products")
	#print("Updating article numbers in transactions...")
	#transactions = correct_identifiers.correct(transactions, "product_transactions")
	
	# Remove not-for-sale products
	print("Removing non-sale products...")
	products = filter.remove_nonsale(products)
	# Correct heel height to ranges
	print("Correcting heel height ranges...")
	products = correct_ranges.correct_heel(products)
	# Correct shaft width to ranges
	print("Correcting shaft width ranges...")
	products = correct_ranges.correct_shaft(products, 'shaft_width')
	
	return transactions, products