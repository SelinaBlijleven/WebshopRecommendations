# # Input: Product vectors
# # Output: Similarity matrix for products
# # Similarity matrix for products (No strings accepted!)
# def get_similarity(products):
	# # No. of products
	# m = len(products)
	# # Similarity matrix
	# sim = np.ones((m, m))
	
	# for i in range(m):
		# for j in range(m):
			# if i != j:
				# sim[i][j] = product_similarity.cosine(products[i], products[j])
			
	# article_ids = products['article_id'].values
	# header = str(article_ids).strip('[]')
	# save.array("similarity_products", sim, fheader=header)