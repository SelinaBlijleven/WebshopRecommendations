import csv

def save_array(name, array):
	path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Code/Output/"
	fname = path + name
	numpy.savetxt(fname, array, delimiter=',')