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
			x_num = is_num(x)
			if not x_num == None and x_num > 0:
				correct.append(categorize(x))
			else:
				corrected.append(h)
			
	products['heel_height'].replace(products['heel_height'], corrected,inplace=True)
	return products