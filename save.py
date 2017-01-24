import numpy as np

# Input: File name, array, write mode
# Output: Written file with specified name and data from array.
def array(name, array, write_mode="a"):
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Code/Output/"
	fname = path + name + ".csv"

	with open(fname, write_mode) as myfile:
		txt = str(array).strip('[]') + "\n"
		myfile.write(txt)
		
# Input: File name, dataframe
# Output: Written file with specified name and data from dataframe.
def dataframe(name, df):
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Data/"
	fname = path + name + ".csv"
	
	df.to_csv(fname)