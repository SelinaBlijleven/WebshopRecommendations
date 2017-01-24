import numpy as np
import matplotlib
import matplotlib.pyplot as plt

path = "C:/Users/Acer/Documents/Universiteit/Afstudeerproject/Code/Output/"
filename = path + 'evaluation_experiments.png'

N = 4
menMeans = (3.5, 12.5, 13, 14)

ind = np.arange(N)
width = 0.5

fig, ax = plt.subplots()
rects1 = ax.bar(ind, menMeans, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Shared features')
ax.set_title('Shared features per experiment')
ax.set_xticks(ind + width)
ax.set_xticklabels(('50k random', '50k first', '100k first', '1 mil first'))

plt.savefig(filename)