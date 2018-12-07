import numpy as np


def mapping(points,x):
	xs, ys = points.T
	coefficients = np.polyfit(xs,ys,2)
	return (coefficients[0] * (x**2) + coefficients[1] * x + coefficients[2])
	
