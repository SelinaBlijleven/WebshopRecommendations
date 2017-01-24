import pandas as pd

# Input: Products
# Output: Brand names for each article ID
# Links each article ID to brand name.
def get_descriptions(products):
	map = {}
	
	ids = products['article_id'].values
	brands = products['brand']
	
	for i in range(len(ids)):
		if not ids[i] in map.keys():
			map[ids[i]] = brands[i]
			
	return map