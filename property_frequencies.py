# Used libraries/functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Own scripts
import counts

# Input: Transaction dataframe, product dataframe
# Output: Plots in folder
# Plots the value frequencies for all properties. All figures are automatically saved to folder /output/.
# Individual plots can be shown by adding show=True to the arguments of the plot_property function.
def plot(transactions, products):
	# FREQUENCY PLOTS OF ARTICLE PROPERTIES
	# Colour
	plot_property(transactions, products, 'color', "Amount of transactions per colour", "Colour", id_type='color_id')
	# Colour web
	plot_property(transactions, products, 'color_web', "Amount of transactions per colour web", "Colour web", id_type='color_id')
	# Brand
	plot_property(transactions, products, 'brand', "Amount of transactions per brand", "Brand")
	# Main group
	plot_property(transactions, products, 'main_group', "Amount of transactions per main group", "Main group")
	# Subgroup
	plot_property(transactions, products, 'subgroup', "Amount of transactions per sub group", "Subgroup")
	# Season (release)
	plot_property(transactions, products, 'season', "Amount of transactions per season of release", "Season")
	# Category (No data)
	# plot_property(transactions, products, 'category', "Amount of transactions per category", "Category")
	# Material
	plot_property(transactions, products, 'material', "Amount of transactions per material", "Material")
	# Fit
	plot_property(transactions, products, 'fit', "Amount of transactions per fit", "Fit")
	# Material inside
	plot_property(transactions, products, 'material_inside', "Amount of transactions per inside material", "Inside material")
	# Material outside
	plot_property(transactions, products, 'material_inside', "Amount of transactions per outside material", "Outside material")
	# Material inner sole
	plot_property(transactions, products, 'material_inner_sole', "Amount of transactions per inner sole material", "Innner sole material")
	# Material outer sole
	plot_property(transactions, products, 'material_outer_sole', "Amount of transactions per outer sole material", "Outer sole material")
	# Shaft height
	plot_property(transactions, products, 'shaft_height', "Amount of transactions per shaft height", "Shaft height")
	# Shaft width
	plot_property(transactions, products, 'shaft_width', "Amount of transactions per shaft width", "Shaft width")
	# Heel height
	plot_property(transactions, products, 'heel_height', "Amount of transactions per heel height", "Heel height")
	# Heel shape
	plot_property(transactions, products, 'heel_shape', "Amount of transactions per heel shape", "Heel shape")
	# Removable foothead
	plot_property(transactions, products, 'removable_footbed', "Amount of transactions vs. removable footbed", "Removable footbed")
	# Size
	plot_sizes(transactions)

# Input: List of transactions, list of products, name of property in dataframe, graph description, property description
# Output: Plot of frequencies of values of property
# Determines the frequency of every value of an article property and plots histogram of these frequencies.
def plot_property(transactions, products, property, graph_name, property_name, id_type='article_id', show=False):
	ids = get_descriptions(products, property, id_type)
	property_counts, _ = counts.get_frequencies(transactions, ids, id_type)
	plot_histogram(property_counts, property, graph_name, property_name, show)

# Input: List of transactions
# Ouput: Plot of frequencies of values of size.
# Determines the frequency of every different size and plots a histogram of these frequencies. Works similar to plot_property,
# but the size can be used directly from the transaction file.
def plot_sizes(transactions, show=False):
	size_counts = transactions['size'].value_counts()
	plot_histogram(size_counts, 'size', 'Amount of transactions per size.', 'Size', show)
	
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

# Input: Counts of item, graph name, label for x axis
# Output: Histogram of frequencies	
def plot_histogram(counts, property, graph_label, x_label, show=False):
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Code/Output/"
	filename = path + property + '.png'
	
	counts.plot(kind='bar',logy=True)
	
	plt.title(graph_label)
	plt.xlabel(x_label)
	plt.ylabel("Frequency in transaction")
	
	plt.tight_layout()
	plt.savefig(filename)
	
	if show == True:
		plt.show()