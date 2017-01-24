# Input: List of products
# Output: List of products with non-sale items removed.
# Removes all items used internally from products.
def remove_nonsale(products):
	total = len(products)
	sale_products = products[products['main_group'] != 'Verbruik']
	sale_no = len(sale_products)
	print(str(total - sale_no) + " non-sale items removed from product list. \n")
	return sale_products
	
# Input: List of transactions
# Output: All transactions where product was kept.
# Removes all returned items from the transactions.
def remove_returns(transactions):
	total = len(transactions)
	unreturned = transactions[transactions['quantity'] != -1]
	unreturned_no = len(unreturned)
	print(str(total - unreturned_no) + " returned items removed from transactions. \n")
	return unreturned