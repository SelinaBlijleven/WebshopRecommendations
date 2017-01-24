import math
import numpy as np

# Input: List of features, product vectors
# Output: Cosine distance between two vectors
# Calculates similarity between two vectors with formula 1 - (u.v/(||u||2 * ||v||2))
# Calculates dot product and squared magnitude for string properties and integer properties
# apart first and adds them.
def cosine(features, p1, p2):
	dot_product, p1_mag2, p2_mag2 = dot(features, p1, p2)
	return 1 - (dot_product/(p1_mag2 * p2_mag2))
	
# Input: List of (string value) features to compare, product vectors
# Output: Dot product of vectors for indicated features, squared magnitudes of vectors
# This function is used to calculate the dot product and squared magnitudes of the features using
# strings as their value. The dot product is only incremented if the features have the exact same value.
# If the property value for either product is missing the feature is not used in similarity calculation.
def dot(features, p1, p2):
	sum = 0
	p1_mag2 = 0
	p2_mag2 = 0

	for f in features:
		val1 = p1[f]
		val2 = p2[f]
		
		# Property with integers
		if not isinstance(val1, str) and not isinstance(val2, str) and not np.isnan(val1) and not np.isnan(val2):
			p1_mag2 += val1**2
			p2_mag2 += val2**2
			
			sum += val1 * val2
				
		# Property with strings	
		else:
			p1_mag2 += 1**2
			p2_mag2 += 1**2

			if val1 == val2:
				sum += 1
			
	return sum, p1_mag2, p2_mag2