import numpy as np
import pandas as pd

from scipy.sparse import lil_matrix

# Input: Products
# Output: Feature vector for products.
# Converts each products features indicated with a string to binary vectors. (for similarity calculation purposes)
def vectorize(products):
	# List of feature names (corresponding to rows)
	fs = []
	# Transposed product feature list
	t = []
	
	# Missing features:
	# None :D
	features = ['brand', 'color', 'color_web', 'fit', 'heel_height', 'heel_shape', 'main_group', 'material', 'material_inside', 'material_inner_sole', 'material_outer_sole', 'removable_footbed', 'season', 'shaft_height', 'shaft_width', 'subgroup']
	
	# Add the features from the list above.
	for feature in features:
		fs, t = add_property(fs, t, products, feature)
		
	# Converts the list of vectors into an array
	t = np.asarray(t)
	# Transposes the matrix so each row is one product.
	mat = np.transpose(t)
	
	return fs, mat
	
# Input: Feature names, transpose matrix, product list, property names
# Output: Updated list of feature names and updated transpose matrix
# Adds a new feature to the existing matrix and adds the name to feature name list.
def add_property(fs, t, products, property):
	n_fs, n_t = vectorize_property(products, property)
	rows = len(n_fs)
	
	for f in n_fs:
		fs.append(f)
	for row in n_t:
		t.append(row)
	
	return fs, t
	
# Input: Products list, a product property
# Output: Feature names/possible values, corresponding matrix
# Makes a binary vector of possible values for a given property.
def vectorize_property(products, property):
	# All possible property values/feature names
	product_vals = products[property].values
	poss_vals = list(set(product_vals))
	
	rows = len(poss_vals)
	cols = len(products)
	
	mat = lil_matrix((rows, cols))
	
	for i in range(rows):
		val = poss_vals[i]
		
		for j in range(cols):
			if val == product_vals[j]:
				mat[i, j] = 1
				
	return poss_vals, mat