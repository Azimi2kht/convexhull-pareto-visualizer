import numpy as np
from utility import get_points
from hull import graham_scan, pareto
from my_plot import my_plot


points = get_points()
hull = graham_scan(points)
p = pareto(hull)
my_plot(np.array(points), hull, p)
