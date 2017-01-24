########
# Main #
########
# Main function
# Input: Filename for product transactions
def main(fname):
	print "Reading transactions..."
	product_transactions = read(fname)
	keys = product_transactions[0]
	transactions = product_transactions[1:]
	print "Transactions read. " + str(len(transactions)) + " transactions found. \n"
	
	print "Sorting by customer..."
	customers = sort_customer_ID(transactions)
	print "Sorted by customers. " + str(len(customers.keys())) + " customers found. \n"
	
	print "Counting amount of purchases per customer."
	purchases = purchase_amount(customers)
	print purchases
	
###########
# Sorting #
###########
# Sorts the purchases by customer ID.
# Input: All unsorted transactions.
# Output: A dictionary that returns a list of transactions when queried with a customer ID.
def sort_customer_ID(transactions):
	customers = {}
	
	for line in transactions:
		customer = line[5]
		purchase = [line[1:4], line[6:]]
		
		if customer in customers.keys():
			customers[customer].append(purchase)
		else:
			customers[customer] = [purchase]
	return customers
	
############
# Analysis #
############
# Counts the amount of customers for each amount of purchases.
def purchase_amount(customers):
	purchases = {}
	
	for c in customers:
		no = len(customers[c])
		
		if no in purchases.keys():
			purchases[no] += 1
		else:
			purchases[no] = 1
	return purchases

######
# IO #
######
# Reads transaction lines
# Input: Filename for transactions file.
# Output: Array of transactions with their keys on the first line.
def read(fname):
	transactions = []

	for line in open(fname):
		line = (line.rstrip('\n').split(','))
		transactions.append(line)
	return transactions

# Call for main function.
if __name__ == "__main__":
	fname = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/small_product_transactions.csv"
	main(fname)