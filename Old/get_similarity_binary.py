# Input: Product vectors
# Output: Similarity matrix for products
# Similarity matrix for products (No strings accepted!)
def get_similarity(products, product_vectors):
	# No. of products
	m = len(product_vectors)
	# Similarity matrix
	sim = np.ones((m, m))
	
	for i in range(m):
		for j in range(m):
			if i != j:
				sim[i][j] = cosine(product_vectors[i].toarray(), product_vectors[j].toarray())
			
	article_ids = products['article_id'].values
	header = str(article_ids).strip('[]')
	save.array("similarity_products", sim, fheader=header)