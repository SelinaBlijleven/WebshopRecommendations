# Input: List of transactions, start index, end index
# Output: Lines between indices from transactions.
# Used for selecting lines between indices.
def select(transactions, x, y):
	lines = transactions[x:y]
	print("Selected lines from " + str(x) + " to " + str(y) + ":")
	print(str(lines) + "\n")
	return lines