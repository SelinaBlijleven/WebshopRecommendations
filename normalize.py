# Input: List of products, list of features
# Output: Products with the features given normalized
# Normalizes the features specified in the second argument.
def normalize(products, features):
	for f in features:
		values = products[f].values
		max = values[0]
		
		normalized = []
		
		for v in values:
			normalized.append(float(v)/max)
	return products