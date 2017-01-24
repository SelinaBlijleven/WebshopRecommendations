import pandas as pd
import numpy as np
import math

# Input: Products
# Output: Products with heel height corrected to a range
# Corrects the heel height in cms to its range (was also used in some datapoints)
# 0 Laag (0 - 2,5 cm)
# 1 Middel (3 - 4,5 cm)
# 2 Hoog (5 - 6,5 cm)
# 3 Zeer hoog (> 7 cm)
def correct_heel(products):
	heights = products['heel_height']
	corrected = []

	for h in heights:
		if str(h).isdigit():
			corrected.append(heel_range(h))
		else:
			x = str(h).replace(",", ".")
			if len(x) > 0 and x[0].isdigit():
				corrected.append(heel_range(x))
			elif len(x) > 3:
				corrected.append(heel_category(x))
			else:
				corrected.append(h)
			
	products['heel_height'] = corrected
	return products

# Input: Float in string format
# Output: Identifier of heel height range.
def heel_range(h):
	x = float(h)
		
	if (x >= 0 and x <= 2.5):
		return 0
	elif (x >= 3 and x <= 4.5):
		return 1
	elif (x >= 5 and x <= 6.5):
		return 2
	elif (x >= 7):
		return 3
		
# Input: String of >3 chars (to exclude nans)
# Output: Range identifier
# Range identifiers are used to calculate similarity after normalization.
def heel_category(h):
	if h == "Laag (0 - 2,5 cm)":
		return 0
	elif h == "Middel (3 - 4.5 cm)":
		return 1
	elif h == "Hoog (5 - 6,5 cm)":
		return 2
	elif h == "Zeer hoog (> 7 cm)":
		return 3
		
# Input: Products
# Output: Products with shaft width/height corrected to a range
# Shaft width is a column with mixed ranges and loose numbers. These are all
# corrected to an identifier corresponding to a range. These identifiers can be
# normalized and used in similarity.
def correct_shaft(products, f='shaft_width'):
	values = products[f]
	corrected = []
	
	for v in values:
		x = str(v)
		if x[:2].isdigit():
			corrected.append(shaft_range(x[:2]))
		else:
			corrected.append(v)
			
	products[f] = corrected
	return products

# Input: Float in string format
# Output: Number of range of shaft width
# Numbers are used for similarity in width.
def shaft_range(v):
	x = float(v)
	
	if (x < 22):
		return 0
	if (x >= 22 and x <= 25):
		return 1
	if (x >= 26 and x <= 29):
		return 2
	if (x >= 30 and x <= 33):
		return 3
	if (x >= 34 and x <= 37):
		return 4
	if (x >= 38 and x <= 41):
		return 5
	if (x > 41):
		return 6
	
# Input: String
# Output: Integer in string/-1
# If string is a number, convert to number. Otherwise return -1.
def is_num(x):
	try:
		c = float(x)
	except(ValueError):
		return -1
		