import pandas as pd
import numpy as np
import math

# Input: Products
# Output: Products with heel height corrected to a range
# Corrects the heel height in cms to its range (was also used in some datapoints)
# Laag (0 - 2,5 cm)
# Middel (3 - 4,5 cm)
# Hoog (5 - 6,5 cm)
# Zeer hoog (> 7 cm)
def correct(products):
	heights = products['heel_height']
	corrected = []

	for h in heights:
		if str(h).isdigit():
			corrected.append(categorize(h))
		else:
			x = str(h).replace(",", ".")
			if len(x) > 0 and x[0].isdigit():
				corrected.append(categorize(x))
			else:
				corrected.append(h)
			
	products['heel_height'] = corrected
	return products

def categorize(h):
	x = float(h)
		
	if (x >= 0 and x <= 2.5):
		return "Laag (0 - 2,5 cm)"
	if (x >= 3 and x <= 4.5):
		return "Middel (3 - 4.5 cm)"
	if (x >= 5 and x <= 6.5):
		return "Hoog (5 - 6,5 cm)"
	if (x >= 7):
		return "Zeer hoog (> 7 cm)"
		
# Input: String
# Output: Integer in string/False
# If string is a number, convert to number. Otherwise return false.
def is_num(x):
	try:
		
		c = float(x)
	except(ValueError):
		return -1
		