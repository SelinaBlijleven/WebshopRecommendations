import pandas as pd

import save

# Input: List of products/transactions
# Output: List of products/transactions with unique article numbers
# Appends the color ID to each article ID to make all article IDs unique.
def correct(df, name):
	article_ids = df['article_id']
	color_ids = df['color_id']
	full_ids = []
	
	for i in range(len(article_ids)):
		article_id = article_ids[i]
		color_id = color_ids[i]
		full_id = str(article_id) + "-" + str(color_id)
		full_ids.append(full_id)
	
	df['article_id'] = full_ids
	save.dataframe("unique_" + name, df)
	return df