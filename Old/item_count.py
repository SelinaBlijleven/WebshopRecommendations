# Input: List of items + item label
# Output: Number of items
# Counts and prints number of items. (Used for both transactions + products)
def get(items, label):
	no_items = len(items)
	print("Total amount of " + label + ": " + str(no_items) + "\n")
	return no_items