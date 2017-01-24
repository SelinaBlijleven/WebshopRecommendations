import pandas as pd

# Input: Products, property to identify, key to use.
# Output: Specified property for each key of the type. (For example for article ids or color ids)
# Links each ID to article property
def get_descriptions(products, property, id_type):
	map = {}
	
	ids = products[id_type].values
	properties = products[property]
	
	for i in range(len(ids)):
		id = ids[i]
		property = properties[i]
		
		if not id in map.keys():
			map[id] = property
	return map