# Source: plot.ly/matplotlib/bar-charts
import matplotlib.pyplot as plt

y = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
N = len(y)
x = range(N)
width = 1/1.5
plt.bar(x, y, width, color="blue")


fig = plt.gcf()
plt.show()