import pandas as pd

# Input: Products, specification for exact color or colorweb
# Output: Descriptions for color IDs
# Links each color ID to its colour description or colour web. Returns
# a map that can be used to translate colour IDs to colour/colour web.
def get_descriptions(products, web):
	map = {}
	
	ids = products['color_id'].values
	colors = products['color'].values
	color_webs = products['color_web']
	
	for i in range(len(ids)):
		if not ids[i] in map.keys():
			if web == False:
				map[ids[i]] = colors[i]
			else:
				map[ids[i]] = color_webs[i]
			
	return map